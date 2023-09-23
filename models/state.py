#!/usr/bin/python3
"""Defines the State class."""
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.city import City
from models import storage


class State(BaseModel):
    """Represent a state."""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    # For DBStorage
    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    # For FileStorage
    else:
        @property
        def cities(self):
            return [city for city in list(storage.all(City).values())
                    if city.state_id == self.id]

    def __init__(self, *args, **kwargs):
        """
        Initialize class user with kwargs
        Args:
            *args(positional arg): strings
            **kwargs(keyword arg): dictionary
        """
        super().__init__(*args, **kwargs)
        self.name = ""
