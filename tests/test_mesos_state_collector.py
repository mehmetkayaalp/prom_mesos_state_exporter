import unittest
from collector import MesosStateCollector
from prometheus_client import generate_latest


class TestMesosStateCollector(unittest.TestCase):

    def setUp(self):
        self.mesos_state_collector = MesosStateCollector('')

    @staticmethod
    def generate_mock_json_with_unrunning_reserved_tasks():
        return {
          "slaves": [
            {
              "hostname": "172.40.194.193",
              "reserved_resources": {
                "marathon": {
                  "mem": 8192.0,
                  "gpus": 0.0,
                  "disk": 4.0,
                  "cpus": 0.04
                }
              },
              "used_resources": {
                "mem": 13692.0,
                "gpus": 0.0,
                "disk": 4.0,
                "cpus": 0.15
              },
              "used_resources_full": [
                {
                  "role": "marathon",
                  "scalar": {
                    "value": 0.01
                  },
                  "type": "SCALAR",
                  "name": "cpus",
                  "reservation": {
                    "labels": {
                      "labels": [
                        {
                          "value": "19ba4f36-9afc-4b14-b021-32d810f85dd2-0000",
                          "key": "marathon_framework_id"
                        },
                        {
                          "value": "infra_marathon-lb.5afe53cc-a473-11e6-8f26-eeeeeeeeeeee",
                          "key": "marathon_task_id"
                        }
                      ]
                    },
                    "principal": "marathon"
                  }
                },
                {
                  "role": "marathon",
                  "scalar": {
                    "value": 256.0
                  },
                  "type": "SCALAR",
                  "name": "mem",
                  "reservation": {
                    "labels": {
                      "labels": [
                        {
                          "value": "19ba4f36-9afc-4b14-b021-32d810f85dd2-0000",
                          "key": "marathon_framework_id"
                        },
                        {
                          "value": "infra_marathon-lb.5afe53cc-a473-11e6-8f26-eeeeeeeeeeee",
                          "key": "marathon_task_id"
                        }
                      ]
                    },
                    "principal": "marathon"
                  }
                },
                {
                  "name": "disk",
                  "scalar": {
                    "value": 1.0
                  },
                  "role": "marathon",
                  "reservation": {
                    "labels": {
                      "labels": [
                        {
                          "value": "19ba4f36-9afc-4b14-b021-32d810f85dd2-0000",
                          "key": "marathon_framework_id"
                        },
                        {
                          "value": "infra_marathon-lb.5afe53cc-a473-11e6-8f26-eeeeeeeeeeee",
                          "key": "marathon_task_id"
                        }
                      ]
                    },
                    "principal": "marathon"
                  },
                  "disk": {
                    "volume": {
                      "container_path": "fake_volume_for_dynamic_reservation_of_infra_marathon_lb}}",
                      "mode": "RW"
                    },
                    "persistence": {
                      "id": "infra_marathon-lb#fake_volume_for_dynamic_reservation_of_infra_marathon_lb}}#5afe53cb-a473-11e6-8f26-eeeeeeeeeeee",
                      "principal": "marathon"
                    }
                  },
                  "type": "SCALAR"
                }
              ],
              "reserved_resources_full": {
                "marathon": [
                  {
                    "role": "marathon",
                    "scalar": {
                      "value": 0.01
                    },
                    "type": "SCALAR",
                    "name": "cpus",
                    "reservation": {
                      "labels": {
                        "labels": [
                          {
                            "value": "19ba4f36-9afc-4b14-b021-32d810f85dd2-0000",
                            "key": "marathon_framework_id"
                          },
                          {
                            "value": "infra_marathon-lb.5afe53cc-a473-11e6-8f26-eeeeeeeeeeee",
                            "key": "marathon_task_id"
                          }
                        ]
                      },
                      "principal": "marathon"
                    }
                  },
                  {
                    "name": "mem",
                    "type": "SCALAR",
                    "scalar": {
                      "value": 256
                    },
                    "role": "marathon",
                    "reservation": {
                      "principal": "marathon",
                      "labels": {
                        "labels": [
                          {
                              "key": "marathon_framework_id",
                              "value": "19ba4f36-9afc-4b14-b021-32d810f85dd2-0000"
                          },
                          {
                              "key": "marathon_task_id",
                              "value": "infra_marathon-lb.5afe53cc-a473-11e6-8f26-eeeeeeeeeeee"
                          }
                        ]
                      }
                    }
                  },
                  {
                    "role": "marathon",
                    "scalar": {
                      "value": 0.01
                    },
                    "type": "SCALAR",
                    "name": "cpus",
                    "reservation": {
                      "labels": {
                        "labels": [
                          {
                            "value": "19ba4f36-9afc-4b14-b021-32d810f85dd2-0000",
                            "key": "marathon_framework_id"
                          },
                          {
                            "value": "infra_marathon-lb.9f7f4c9b-c2c3-11e6-8f1d-eeeeeeeeeeee",
                            "key": "marathon_task_id"
                          }
                        ]
                      },
                      "principal": "marathon"
                    }
                  },
                  {
                    "role": "marathon",
                    "scalar": {
                      "value": 256.0
                    },
                    "type": "SCALAR",
                    "name": "mem",
                    "reservation": {
                      "labels": {
                        "labels": [
                          {
                            "value": "19ba4f36-9afc-4b14-b021-32d810f85dd2-0000",
                            "key": "marathon_framework_id"
                          },
                          {
                            "value": "infra_marathon-lb.9f7f4c9b-c2c3-11e6-8f1d-eeeeeeeeeeee",
                            "key": "marathon_task_id"
                          }
                        ]
                      },
                      "principal": "marathon"
                    }
                  },
                  {
                    "name": "disk",
                    "scalar": {
                      "value": 1.0
                    },
                    "role": "marathon",
                    "reservation": {
                      "labels": {
                        "labels": [
                          {
                            "value": "19ba4f36-9afc-4b14-b021-32d810f85dd2-0000",
                            "key": "marathon_framework_id"
                          },
                          {
                            "value": "infra_marathon-lb.9f7f4c9b-c2c3-11e6-8f1d-eeeeeeeeeeee",
                            "key": "marathon_task_id"
                          }
                        ]
                      },
                      "principal": "marathon"
                    },
                    "disk": {
                      "volume": {
                        "container_path": "fake_volume_for_dynamic_reservation_of_infra_marathon_lb}}",
                        "mode": "RW"
                      },
                      "persistence": {
                        "id": "infra_marathon-lb#fake_volume_for_dynamic_reservation_of_infra_marathon_lb}}#9f7ed76a-c2c3-11e6-8f1d-eeeeeeeeeeee",
                        "principal": "marathon"
                      }
                    },
                    "type": "SCALAR"
                  }
                ]
              }
            }
          ]
        }

    @staticmethod
    def generate_mock_json_without_unrunning_reserved_tasks():
        return {
          "slaves": [
            {
              "hostname": "172.40.194.193",
              "reserved_resources": {
                "marathon": {
                  "mem": 4596.0,
                  "gpus": 0.0,
                  "disk": 3.0,
                  "cpus": 0.03
                }
              },
              "used_resources": {
                "mem": 6096.0,
                "gpus": 0.0,
                "disk": 3.0,
                "cpus": 0.07
              },
              "used_resources_full": [
                {
                  "role": "marathon",
                  "scalar": {
                    "value": 0.01
                  },
                  "type": "SCALAR",
                  "name": "cpus",
                  "reservation": {
                    "labels": {
                      "labels": [
                        {
                          "value": "dc155b12-18a1-4f4c-ba76-3e15de570778-0000",
                          "key": "marathon_framework_id"
                        },
                        {
                          "value": "automotive_corporate_mongo_primary.76ce643d-c2b7-11e6-ad8a-eeeeeeeeeeee",
                          "key": "marathon_task_id"
                        }
                      ]
                    },
                    "principal": "marathon"
                  }
                },
                {
                  "role": "marathon",
                  "scalar": {
                    "value": 2048.0
                  },
                  "type": "SCALAR",
                  "name": "mem",
                  "reservation": {
                    "labels": {
                      "labels": [
                        {
                          "value": "dc155b12-18a1-4f4c-ba76-3e15de570778-0000",
                          "key": "marathon_framework_id"
                        },
                        {
                          "value": "automotive_corporate_mongo_primary.76ce643d-c2b7-11e6-ad8a-eeeeeeeeeeee",
                          "key": "marathon_task_id"
                        }
                      ]
                    },
                    "principal": "marathon"
                  }
                },
                {
                  "name": "disk",
                  "scalar": {
                    "value": 1.0
                  },
                  "role": "marathon",
                  "reservation": {
                    "labels": {
                      "labels": [
                        {
                          "value": "dc155b12-18a1-4f4c-ba76-3e15de570778-0000",
                          "key": "marathon_framework_id"
                        },
                        {
                          "value": "automotive_corporate_mongo_primary.76ce643d-c2b7-11e6-ad8a-eeeeeeeeeeee",
                          "key": "marathon_task_id"
                        }
                      ]
                    },
                    "principal": "marathon"
                  },
                  "disk": {
                    "volume": {
                      "container_path": "fake_volume_for_dynamic_reservation_of_automotive_corporate_mongo_primary",
                      "mode": "RW"
                    },
                    "persistence": {
                      "id": "automotive_corporate_mongo_primary#fake_volume_for_dynamic_reservation_of_automotive_corporate_mongo_primary#76ce643c-c2b7-11e6-ad8a-eeeeeeeeeeee",
                      "principal": "marathon"
                    }
                  },
                  "type": "SCALAR"
                }
              ],
              "reserved_resources_full": {
                "marathon": [
                  {
                    "role": "marathon",
                    "scalar": {
                      "value": 0.01
                    },
                    "type": "SCALAR",
                    "name": "cpus",
                    "reservation": {
                      "labels": {
                        "labels": [
                          {
                            "value": "dc155b12-18a1-4f4c-ba76-3e15de570778-0000",
                            "key": "marathon_framework_id"
                          },
                          {
                            "value": "automotive_corporate_mongo_primary.76ce643d-c2b7-11e6-ad8a-eeeeeeeeeeee",
                            "key": "marathon_task_id"
                          }
                        ]
                      },
                      "principal": "marathon"
                    }
                  },
                  {
                    "role": "marathon",
                    "scalar": {
                      "value": 2048.0
                    },
                    "type": "SCALAR",
                    "name": "mem",
                    "reservation": {
                      "labels": {
                        "labels": [
                          {
                            "value": "dc155b12-18a1-4f4c-ba76-3e15de570778-0000",
                            "key": "marathon_framework_id"
                          },
                          {
                            "value": "automotive_corporate_mongo_primary.76ce643d-c2b7-11e6-ad8a-eeeeeeeeeeee",
                            "key": "marathon_task_id"
                          }
                        ]
                      },
                      "principal": "marathon"
                    }
                  },
                  {
                    "name": "disk",
                    "scalar": {
                      "value": 1.0
                    },
                    "role": "marathon",
                    "reservation": {
                      "labels": {
                        "labels": [
                          {
                            "value": "dc155b12-18a1-4f4c-ba76-3e15de570778-0000",
                            "key": "marathon_framework_id"
                          },
                          {
                            "value": "automotive_corporate_mongo_primary.76ce643d-c2b7-11e6-ad8a-eeeeeeeeeeee",
                            "key": "marathon_task_id"
                          }
                        ]
                      },
                      "principal": "marathon"
                    },
                    "disk": {
                      "volume": {
                        "container_path": "fake_volume_for_dynamic_reservation_of_automotive_corporate_mongo_primary",
                        "mode": "RW"
                      },
                      "persistence": {
                        "id": "automotive_corporate_mongo_primary#fake_volume_for_dynamic_reservation_of_automotive_corporate_mongo_primary#76ce643c-c2b7-11e6-ad8a-eeeeeeeeeeee",
                        "principal": "marathon"
                      }
                    },
                    "type": "SCALAR"
                  }
                ]
              }
            }
          ]
        }

    def test_collect_with_unrunning_reserved_tasks(self):
        # used generate_latest method for easy assert
        self.mesos_state_collector.get_slaves_info = self.generate_mock_json_with_unrunning_reserved_tasks
        prom_metrics_text = generate_latest(self.mesos_state_collector)
        expected_text = '''# HELP unrunning_reserved_tasks_count from unrunning_reserved_tasks_count
# TYPE unrunning_reserved_tasks_count gauge
unrunning_reserved_tasks_count{marathon_app_id="marathon_app_id"} 1.0
# HELP used_reservations_count from used_reservations_count
# TYPE used_reservations_count gauge
used_reservations_count 1.0
# HELP reserved_tasks_count from reserved_tasks_count
# TYPE reserved_tasks_count gauge
reserved_tasks_count 2.0
'''
        self.assertEqual(expected_text, prom_metrics_text)

    def test_collect_without_unrunning_reserved_tasks(self):
        # used generate_latest method for easy assert
        self.mesos_state_collector.get_slaves_info = self.generate_mock_json_without_unrunning_reserved_tasks
        prom_metrics_text = generate_latest(self.mesos_state_collector)
        expected_text = '''# HELP used_reservations_count from used_reservations_count
# TYPE used_reservations_count gauge
used_reservations_count 1.0
# HELP reserved_tasks_count from reserved_tasks_count
# TYPE reserved_tasks_count gauge
reserved_tasks_count 1.0
'''
        self.assertEqual(expected_text, prom_metrics_text)

if __name__ == '__main__':
    unittest.main()
