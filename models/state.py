#!/usr/bin/python3
"""Defines the State class."""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """Represent a state.

    Attributes:
        name (str): The name of the state.
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """
            This is a getter attribute
            Returns: A list of City instances with state.id
            equal current state.id
            """
            all_city = []
            city_instance = models.storage.all(City)
            for city in city_instance.values():
                if city.state_id == self.id:
                    all_city.append(city)
            return all_city
