#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Represent a city inheriting
    from BaseModel and Base"""
    """
        check the type of storage specified
    """
    __tablename__ = "cities"  # name of the table
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities",
                          cascade="all, delete-orphan")
