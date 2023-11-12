#!/usr/bin/python3

"""
  Database Storage Engine
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """
    This class represents the functionality for
    our DataBase
  """

    __engine = None  # serves as the engine for connection to mysql server
    __session = None  # session that we use in performing database operations

    def __init__(self):
        self.user = getenv("HBNB_MYSQL_USER")
        self.password = getenv("HBNB_MYSQL_PWD")
        self.host = getenv("HBNB_MYSQL_HOST")
        self.database = getenv("HBNB_MYSQL_DB")

        """
        create a engine that connects to a MySQL database
        """

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(self.user, self.password,
                                             self.host, self.database),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        This method returns a dictionary of objects with the passed
        class as argument or if no argument returns every class
        Args:
            cls: Class name

        Returns: A dictionary

        """

        class_dict = {}

        if cls is None or cls == "":
            result = self.__session.query(State, City, User,
                                          Place, Amenity, Review).all()
            for column in result:
                for row in column:
                    key = "{}.{}".format(row.__class__.__name__, row.id)
                    value = row
                    class_dict[key] = value
                return class_dict
        else:
            if type(cls) == str:
                cls = eval(cls)
            result = self.__session.query(cls).all()
        for row in result:
            key = "{}.{}".format(row.__class__.__name__, row.id)
            value = row
            class_dict[key] = value
        return class_dict

    def new(self, obj):
        """
        Add the object to the DataBase record
        Args:
            obj: instances
        """

        self.__session.add(obj)

    def save(self):
        """
        commit the changes to the DataBase to reflect the updated
        change
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete an instance record in the DB
        Args:
            obj: objectC
        """
        if obj is None:
            pass
        else:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """
        create all tables in the database

        """
        Base.metadata.create_all(self.__engine, checkfirst=True)
        # """
        #     use the session maker to create a session that we can use for
        #     operations and give it a scoped_session to make sure our session
        #     is thread-safe
        # """
        DB_Factory = scoped_session(sessionmaker(bind=self.__engine,
                                                 expire_on_commit=False))
        self.__session = DB_Factory()

    def close(self):
        """close current session
        """
        self.__session.close_all()
