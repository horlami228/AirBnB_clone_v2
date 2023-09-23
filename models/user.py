#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """Represent a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """
        Initialize class User with kwargs.

        Args:
            *args (tuple): Positional arguments.
            **kwargs (dict): Keyword arguments.
        """
        super().__init__(*args, **kwargs)
