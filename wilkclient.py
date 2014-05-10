#!/usr/bin/env python

import multiprocessing
import getopt
import yaml
import requests
import json
import operator
import itertools

# Some quick vocabulary
# `job` is a portion of a test that runs on a remote server (triggered via http)
# `test` is a meaningful collection of jobs that must run together
# `host` is a hostname/ip:port combination running the job server


def load_config(self, config_file)
    user_config = {}
    config = {'hosts': ['localhost:8080'],
                      'tests': ['scripts/simple_noop.yml'],
                      'error_file': 'error.txt'}
    if config_file is not None:
        with open(config_file, 'r') as f:
            user_config = yaml.load(f, Loader=yaml.Loader)
        default_config.update(user_config)
    config['hosts'] = [standardize_host(h) for h in config['hosts']]
    config['tests'] = [load_test_from_file(test) for test in config['tests']]
    config['max_instances'] = config.get('max_instances',
                                         len(config['hosts'] * 4))
    return config


def standardize_host(s):
    return s if ':' in s else "%s:8080" % (s)


def load_test_from_file(test):
    with open(test, 'r') as f:
        test_info = yaml.load(f, Loader=yaml.Loader)


def json_payload_for_job(test_id, node_id, script):
    return json.dumps({'test_id': str(test_id),
                       'node_id': str(node_id),
                       'script': script})


def run_test(pool, test):



def run_job(host, job, test_id, node_id, script):
    r = requests.post('http://%s' % (host),
                      data=json_payload_for_job(test_id, node_id, script))
    return (r.status_code, r.json())
