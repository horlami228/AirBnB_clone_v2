#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Amenity(BaseModel, Base):
    """Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
