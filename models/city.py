#!/usr/bin/python3
"""Defines the City class."""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import Base
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Represent a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities")

    def __init__(self, *args, **kwargs):
        """
        Initialize clss user with kwargs
        Args:
            *args(positional arg): strings
            **kwargs(keyword arg): dictionary
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
