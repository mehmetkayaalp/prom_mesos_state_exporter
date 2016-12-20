# Prometheus Target Exporter

Exporting metrics scraped from mesos state, added reserved task related metrics so far:

```
reserved_tasks_count
used_reservations_count
unrunning_reserved_tasks_count
```

## Using Docker

You can deploy this exporter using the [ekesken/prom-mesos-state-exporter](https://registry.hub.docker.com/u/ekesken/prom-mesos-state-exporter/) Docker image.

For example:

```bash
docker run -d -e PROM_TARGET_ENDPOINT=http://server-prom.marathon.mesos:9090/mesos-states -p 9099:9099 ekesken/prom-mesos-state-exporter
# try it
# curl http://localhost:9099/metrics
```

## Deploy on Marathon

You can deploy this exporter on marathon via following curl command:

```bash
curl -XPOST -H 'Content-Type: application/json;' marathon.mesos:8080/v2/apps -d '{
  "cpus": 0.01,
  "mem": 100,
  "id": "/prom/mesos-state-exporter",
  "instances": 1,
  "env": {
    "MESOS_ENDPOINT": "http://leader.mesos:5050"
  },
  "container": {
    "type": "DOCKER",
    "docker": {
      "image": "ekesken/prom-mesos-state-exporter",
      "network": "BRIDGE",
      "privileged": true,
      "portMappings": [{"containerPort": 9099}]
    }
  },
  "healthChecks": [{"protocol": "HTTP", "path": "/metrics"}]
}'
```

## Scrape config on prometheus

A sample prometheus mesos-state yaml example if you already have have mesos-dns:

```
  - job_name: 'mesos-state'
    dns_sd_configs:
      - names: ['_mesos-state-exporter-prom._tcp.marathon.mesos']
```
