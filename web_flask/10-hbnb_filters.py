#!/usr/bin/python3

"""web flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def close_session(close):
    """close all current  session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_home():
    """display the home page of HBNB"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()

    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
