#!/bin/env python3

from flask import Flask
from flask import request
from flask import send_from_directory

from markdown import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension

from matrix import Matrix

app = Flask(__name__)

def get_params():
    A = eval("%s" % request.args.get('A'))
    B = eval("%s" % request.args.get('B'))
    k = eval("%s" % request.args.get('k'))
    A = Matrix(A) if A else None
    B = Matrix(B) if B else None
    k = k if k else None
    return (A, B, k)

@app.get('/')
def index():
    file = open("README.md", "r") 
    html = markdown(file.read())
    return html

@app.route('/api/add')
def add():
    A, B, k = get_params()
    try:
        ans = A + B
        return str(ans)
    except Exception as e:
        return "error: addition: %s" % e

@app.route('/api/sub')
def sub():
    A, B, k = get_params()
    try:
        ans = A - B
        return str(ans)
    except Exception as e:
        return "error: subtraction: %s" % e

@app.route('/api/mul')
def mul():
    A, B, k = get_params()
    try:
        ans = A * (k if k != None else B)
        return str(ans)
    except Exception as e:
        return "error: multiplication: %s" % e

@app.route('/api/pow')
def pow():
    A, B, k = get_params()
    try:
        if isinstance(k, int):
            ans = A ** k
        else:
            return "error: exponent: power should be int"
        return str(ans)
    except Exception as e:
        return "error: exponent: %s" % e

@app.route('/api/det')
def det():
    A, B, k = get_params()
    try: 
        return str(abs(A))
    except Exception as e:
        return "error: determinant: %s" % e

@app.route('/api/trn')
def trn():
    A, B, k = get_params()
    try: 
        return str(A.transpose())
    except Exception as e:
        return "error: transpose: %s" % e

@app.route('/api/adj')
def adj():
    A, B, k = get_params()
    try: 
        return str(A.adjoint())
    except Exception as e:
        return "error: adjoint: %s" % e

@app.route('/api/inv')
def inv():
    A, B, k = get_params()
    try: 
        return str(A ** -1)
    except Exception as e:
        return "error: inverse: %s" % e


@app.get('/<path:dir>/')
def serve_dir(dir):
    return send_from_directory('res', dir + '/index.html')

if __name__ == '__main__':
    app.run()
