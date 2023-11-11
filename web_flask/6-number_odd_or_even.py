#!/usr/bin/python3
"""
    This is a script that starts a Flask
    web application
"""
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/", strict_slashes=False)
def hello():
    """ Home page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ HBNB page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text=None):
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python_text(text="is_cool"):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def is_num(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_temp(n):
    """
        html template
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    return render_template("6-number_odd_or_even.html", num=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
