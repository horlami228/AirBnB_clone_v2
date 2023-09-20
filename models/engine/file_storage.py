#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        selected = {}
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    selected[key] = value
            return selected
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):

        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
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
                """ split and get the class name"""
                class_name = new_object[0]

                self.new(eval("{}".format(class_name))(**value))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj is None:
            pass
        else:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            del self.__objects[key]
            self.save()
