import os
import logging
from flask import Flask, redirect, Response
from collector import MesosStateCollector
from prometheus_client import PROCESS_COLLECTOR
from prometheus_client.core import REGISTRY
from prometheus_client.exposition import generate_latest

MESOS_ENDPOINT=os.environ.get('MESOS_ENDPOINT', 'http://leader.mesos:5050')
REGISTRY.unregister(PROCESS_COLLECTOR)
REGISTRY.register(MesosStateCollector(MESOS_ENDPOINT))
app = Flask(__name__)


@app.route('/')
def home():
    return redirect('/metrics')


@app.route('/metrics')
def metrics():
    prom_metrics = generate_latest(REGISTRY)
    return Response(prom_metrics, content_type='text/plain')


if __name__ == '__main__':
    log_format = u'[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d}' \
                 u' %(levelname)s - %(message)s'
    logging.basicConfig(
            level=logging.INFO,
            format=log_format,
    )
    app.run(debug=True)
