import re
import logging
import requests
import collections
from prometheus_client.core import GaugeMetricFamily


LOGGER = logging.getLogger(__name__)


class MesosStateCollector(object):

    def __init__(self, mesos_endpoint):
        self.mesos_endpoint = mesos_endpoint;
        self.slaves_info = None
        self.slaves_by_task = collections.defaultdict(list)

    def get_slaves_info(self):
        self.slaves_by_task = collections.defaultdict(list)
        resp = requests.get('%s/slaves' % self.mesos_endpoint)
        return resp.json()

    def get_resources_full_tasks(self, key):
        resources_full = set()
        for slave in self.slaves_info['slaves']:
            reservations = slave[key]
            if 'marathon' in reservations:
                reservations = reservations['marathon']
            for reservation in reservations:
                if 'reservation' in reservation:
                    reservation = reservation['reservation']
                if 'labels' in reservation:
                    labels = reservation['labels']
                else:
                    continue
                if 'labels' in labels:
                    labels = labels['labels']
                for label in labels:
                    if label['key'] == 'marathon_task_id':
                        resources_full.add(label['value'])
                        self.slaves_by_task[label['value']].append(slave['hostname'])
        return resources_full

    def get_reserved_resources_full_tasks(self):
        return self.get_resources_full_tasks('reserved_resources_full')

    def get_used_resources_full_tasks(self):
        return self.get_resources_full_tasks('used_resources_full')

    def check_reservation_duplicates(self):
        self.slaves_info = self.get_slaves_info()
        reserved_tasks = self.get_reserved_resources_full_tasks()
        used_reservations = self.get_used_resources_full_tasks()
        LOGGER.info('Found %d reserved tasks.' % len(reserved_tasks))
        LOGGER.info('Found %d used reservations.' % len(used_reservations))
        unrunning_reserved_tasks = reserved_tasks - used_reservations
        unrunning_reserved_apps = collections.Counter()
        if len(unrunning_reserved_tasks) > 0:
            LOGGER.warn('Found %d unrunning reserved tasks:' % len(unrunning_reserved_tasks))
            for t in unrunning_reserved_tasks:
                t_app = t.split('.')[0]
                unrunning_reserved_apps[t_app] += 1
                LOGGER.warn('[unrunning_reserved_tasks] %s at %s' % (t, ','.join(self.slaves_by_task[t])))
        else:
            LOGGER.info('All reserved tasks are running.')
        return {
            'reserved_tasks_count': len(reserved_tasks),
            'used_reservations_count': len(used_reservations),
            'unrunning_reserved_tasks_count': unrunning_reserved_apps,
        }

    def collect(self):
        reservations = self.check_reservation_duplicates()
        for mkey, mval in reservations.iteritems():
            if isinstance(mval, dict):
                for lkey, lval in mval.iteritems():
                    metric = self.convert_gauge_metric(
                        mkey, lval, labels=['marathon_app_id'], label_values=[lkey])
                    yield metric
            else:
                metric = self.convert_gauge_metric(mkey, mval)
                yield metric

    @classmethod
    def convert_gauge_metric(cls, metric_key, metric_value, labels=None, label_values=None):
        if labels is None:
            gm = GaugeMetricFamily(
                name=metric_key,
                documentation='from %s' % metric_key,
                value=metric_value,
            )
        else:
            gm = GaugeMetricFamily(
                name=metric_key,
                documentation='from %s' % metric_key,
                labels=labels,
            )
            gm.add_metric(label_values, metric_value)
        return gm
