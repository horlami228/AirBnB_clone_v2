#!/usr/bin/python3

"""web flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(close):
    """close all current  session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def get_states():
    """return html page with all states"""
    states = storage.all(State).values()
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def get_state_id(id):
    """return html page with state with id
    and all cities with relationship with the state"""
    found_state = None
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            found_state = state

    return render_template("9-states.html", state=found_state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
