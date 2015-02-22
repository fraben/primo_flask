from flask import Flask
from flask import render_template
from flask import make_response
from flask import request
import datetime
import os
import json
import time
import urllib2
from flask.ext.bootstrap import Bootstrap
import pprint
import collections

app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/')
@app.route('/<path:pathname>')
def index(pathname=None):
    root_dir_requested = not(bool(pathname))
    pathname = '/' if not pathname else '/' + pathname
    parent_dir = ''

    dict_of_files = {fl: os.path.isdir(os.path.join(pathname or '', fl))
                     for fl in os.listdir(pathname) if not fl.startswith('.')}
    if not root_dir_requested:
        dict_of_files['..'] = True
        parent_dir = os.path.dirname(pathname)

    dict_of_files = collections.OrderedDict(sorted(dict_of_files.items()))

    return render_template('index.html', dict_of_files=dict_of_files,
                           pathname=pathname, parent_dir=parent_dir)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)