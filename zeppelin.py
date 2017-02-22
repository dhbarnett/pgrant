#!/usr/bin/env python

import json


class Zeppelin(object):
    """
    This class represents everything we need to know about a zeppelin notebook. This class also contains all of the
    tools to parse said information from a notebook.
    """
    def __init__(self, notebook_name):
        self.notebook_name = notebook_name
        self.notebook_file = open(self.notebook_name, 'r')
        self.notebook_data = json.load(self.notebook_file)
        self.notebooks = {}

    def get_category(self):
        if 'text' not in self.notebook_data['paragraphs'][0]:
            return ''
        first_paragraph_data = self.notebook_data['paragraphs'][0]['text'].split('\n')
        if first_paragraph_data[0].strip() != '%md':
            return ''
        else:
            categories = filter(lambda x: x.lstrip(' #').lower().startswith('category:'), first_paragraph_data)
            if categories:
                return categories[0].split(':', 1)[1]
            else:
                return ''

    def get_team(self):
        if 'text' not in self.notebook_data['paragraphs'][0]:
            return ''
        first_paragraph_data = self.notebook_data['paragraphs'][0]['text'].split('\n')
        if first_paragraph_data[0].strip() != '%md':
            return ''
        else:
            teams = filter(lambda x: x.strip().startswith('team:'), first_paragraph_data)
            if teams:
                return teams[0].split(':', 1)[1]
            else:
                return ''

