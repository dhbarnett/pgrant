#!/usr/bin/env python

import json

from config import Config
from flask import Flask, Response, send_file, render_template
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
        for category in notebook.get_category().split('|'):
            category = category.strip()
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


app = Flask(__name__)


@app.route('/images/<string:img_file>')
def return_img(img_file):
    return send_file('images/{}'.format(img_file), mimetype='img/jpeg')


@app.route('/css/<string:css_file>')
def return_css(css_file):
    return Response(open('templates/{}.css'.format(css_file), 'r').read(), mimetype='text/css')


@app.route('/favicon.ico')
def dummy():
    return Response('')


@app.route('/notebooks/<string:notebook>')
def serve_notebook(notebook):
    return send_file('notebooks/{}'.format(notebook))


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def run_pgrant(path):
    pg = Pgrant()
    pg.process_notebooks()
    if path == '':
        category_path = []
    else:
        category_path = path.rstrip('/').split('/')
    subcategories = None
    current = pg.notebooks
    for path in category_path:
        current = current.subcategories.get(path, {})
    if current:
        subcategories = current.subcategories
        notebook_data = dict([(x.notebook_name, x.get_text().get('results', {}).get('msg', {})[0].get('data', '')) for x in current.notebooks])
    else:
        notebook_data = {}

    return render_template('pgrant.html', category_path=category_path, subcategories=subcategories,
                           notebook_data=notebook_data)
