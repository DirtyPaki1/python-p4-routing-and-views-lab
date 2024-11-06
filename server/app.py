# server/app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print to the terminal
    return parameter  # Display in the browser

@app.route('/count/<int:parameter>')
def count(parameter):
    return "<br>".join(str(i) for i in range(parameter))  # Display each number on a new line

@app.route('/math/<int:num1><operation><int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400

    return str(result)  # Return the result as a string
