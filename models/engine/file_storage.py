#!/usr/bin/python3

"""
    This module represents the storage system for
    this project. The storage method of choice here is
    serialization and deserialization of JSON(Javascript object Notation)
    objects
"""
import json
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State


class FileStorage:
    """
        This class represents a File storage class
    """

    __file_path = "file.json"  # file path to JSON file
    __objects = {}  # stores all dictionary objects by the class name id

    def all(self):
        """
            This public method returns the dictionary stored in
            '__objects' if any
        """
        return self.__objects

    def new(self, obj):
        """
            Add the objects to the __objects dictionary
            by using the objects id as the key
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
            This method serializes __objects dictionary
            to a JSON string and saves it to the
            file according to the file path
        """
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            base_dic = {}
            for (key, value) in self.__objects.items():
                base_dic[key] = value.to_dict()

            json.dump(base_dic, file)  # write json data to file

    def reload(self):
        """
            This method deserializes the JSON file to
            __objects
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:

                original_dic = json.load(file)  # get the json string
                # deserialize the json string to its original
                # structure

            """
                loop through the dictionary by getting key, value pairs
                and use the value to create a new object instance
            """
            for key, value in original_dic.items():
                new_object = key.split(".")
                class_name = new_object[0]
                """ split and get the class name"""
                self.new(eval("{}".format(class_name))(**value))
        except FileNotFoundError:
            pass
