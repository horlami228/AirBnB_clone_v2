#!/usr/bin/python3
"""
    This is a script that starts a Flask
    web application
"""
from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
