#!/usr/bin/python3
"""
In this module we combine flask with sqlAlchemy to render a template.
Run this script from AirBnB_clone_v4 directory for imports
"""
from models import storage
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from flask import Flask
from flask import render_template
import uuid
app = Flask(__name__)


@app.route('/2-hbnb/')
def hbnb():
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    places_tmp = storage.all("Place").values()
    owners = storage.all("User")
    places = []
    cache_id = uuid.uuid4();

    for k, v in owners.items():
        for place in places_tmp:
            if k == place.user_id:
                places.append(["{} {}".format(
                    v.first_name, v.last_name), place])
    places.sort(key=lambda x: x[1].name)
    return render_template("2-hbnb.html",
                           amenities=amenities, result=states, places=places,
                           cache_id=cache_id)


@app.teardown_appcontext
def close_session(exception):
    """Remove the db session or save file"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
