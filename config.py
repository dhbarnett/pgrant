#!/usr/bin/env python

import json


class Config(object):
    def __init__(self, configdir='config.json'):
        self.config = json.load(open(configdir, 'rb'))

    def get_zeppelin_dirs(self):
        return self.config['zeppelin_dirs']
