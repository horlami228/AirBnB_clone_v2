#!/usr/bin/python3
"""
Defines the Place class that inherits from BaseModel.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import Relationship
from os import getenv
import models
from models.review import Review


class Place(BaseModel, Base):
    """
    Represents a place.

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    # reviews = Relationship("Review", backref="place",
    #                        cascade="all, delete-orphan")
    #
    # if getenv("HBNB_TYPE_STORAGE") != "db":
    #     @property
    #     def reviews(self):
    #         """
    #         This is a getter attribute
    #         Returns: A list of Review instances with place_id
    #         equal current place.id
    #         """
    #         all_reviews = []
    #         city_instance = models.storage.all(Review)
    #         for review in city_instance.values():
    #             if review.place_id == self.id:
    #                 all_reviews.append(review)
    #         return all_reviews
