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
    return "\n".join(str(i) for i in range(parameter)) + "\n"

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    a = int(num1)
    b = int(num2)
    if operation == '+':
        result = a + b
    if operation == '-':
        result = a - b
    if operation == '*':
        result = a * b
    if operation == 'div':
        result = a / b
    if operation == '%':
        result = a % b
    return str(result)
if __name__ == '__main__':
    app.run(port=5555, debug=True)
