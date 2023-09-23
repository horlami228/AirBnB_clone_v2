#!/usr/bin/python3
"""
    This module defines a class BaseModel where all other classes will
    inherit from
"""

import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
# import the uuid module for the id
from uuid import uuid4
import datetime

# import module to show the date and time for instances created
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"  # formatted date and time

# Any class that inherits from this Base will make
# SQLAlchemy to map it to a table
Base = declarative_base()


class BaseModel:
    """
        Defining a class BaseModel
    """
    """
        This attribute are used by SQLAlchemy
    """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.datetime.utcnow())
    updated_at = Column(DateTime,
                        nullable=False, default=datetime.datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance object of
        the BaseModel

        Args:
            *args(positional arg): Positional argument
            **kwargs(keyword arg): key value pair arguments
        """
        self.id = str(uuid4())
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()
        """
            looping through the keyword argument
            for the purpose of initializing a new instance with
            it
        """
        if kwargs:
            for (key, value) in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    # convert date string to datetime object
                    date_string = value
                    date_object = datetime.datetime.strptime(date_string,
                                                             DATE_FORMAT)

                    # strptime() to convert to object
                    value = date_object
                    setattr(self, key, value)
                    # set the created_at or updated_at attributes
                setattr(self, key, value)
                # set every other passed argument

    def __str__(self):
        """
        This magic method returns a string representation
        of the BaseModel class
        """
        del self.__dict__["_sa_instance_state"]
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
            This public method updates the updated_at attribute
            with the updated date and time
        """
        self.updated_at = datetime.datetime.now()
        # add the object to the object dictionary in file_storage
        models.storage.new(self)
        models.storage.save()  # serialize objects

    def to_dict(self):
        """
            This public method returns a new dictionary containing the
            keys and values from the __dict__ which is a special attribute
        """

        dic = {}
        for (key, value) in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dic[key] = value.isoformat(sep='T')
            elif key == "_sa_instance_state":   # ignore
                pass
            else:
                dic[key] = value
        dic["__class__"] = self.__class__.__name__

        return dic

    def delete(self):
        """
        This method deletes the current instance from the storage
        """
        models.storage.delete(self)
