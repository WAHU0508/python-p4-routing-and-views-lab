#!/usr/bin/env python3

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = "<br>".join(str(i) for i in range(1, parameter + 1))
    print numbers
    return numbers


if __name__ == '__main__':
    app.run(port=5555, debug=True)
