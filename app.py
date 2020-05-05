from flask import Flask, url_for, render_template, send_file
import os
import glob

from os import listdir
from os.path import isfile, join

app = Flask(__name__)


def make_tree(path):
    tree = dict(name=path, children=[])
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=fn))
    return tree


@app.route('/')
def dirtree():
    path = os.getcwd() + "/business-license-downloads/"
    return render_template('index.html', tree=make_tree(path))


@app.route('/files')
def files():
    return send_file()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
