#!/usr/bin/env python

from config import Config
from glob import glob
from zeppelin import Zeppelin


class Category(object):
    def __init__(self, category_name):
        self.category_name = category_name
        # This list is a list of Category types.
        self.subcategories = {}
        # This is a list of notebooks
        self.notebooks = []




class Pgrant():
    def __init__(self, config=None):
        self.config = config
        if self.config is None:
            self.config = Config()
        else:
            self.config = Config(config)
        self.notebooks = Category('Undefined')

    def add_notebook(self, notebook):
        current = self.notebooks
        foo = notebook.get_category()
        foo == foo
        for category in notebook.get_category().split('|'):
            if category == '':
                break
            if category in current.subcategories:
                current = current.subcategories[category]
            else:
                current.subcategories[category] = Category(category)
                current = current.subcategories[category]

        current.notebooks.append(notebook)

    def process_notebooks(self):
        notebook_files = []
        for directory in self.config.get_zeppelin_dirs():
            notebook_files.extend(glob("{}/*.json".format(directory)))

        for notebook in notebook_files:
            self.add_notebook(Zeppelin(notebook))
