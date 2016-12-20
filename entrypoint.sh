#!/bin/bash

sed -i "s/processes=1/processes=$PROCESSES/g" /prom_mesos_state_exporter/uwsgi.ini
supervisord && uwsgi --ini /prom_mesos_state_exporter/uwsgi.ini
