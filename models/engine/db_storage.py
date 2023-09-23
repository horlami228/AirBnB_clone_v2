from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        # Create the engine linked to the MySQL database using environment variables
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        # Query all objects depending on the class name (cls)
        # from the current database session (self.__session)
        pass

    def new(self, obj):
        # Add the object to the current database session (self.__session)
        pass

    def save(self):
        # Commit all changes of the current database session (self.__session)
        pass

    def delete(self, obj=None):
        # Delete an object from the current database session (self.__session) if it's not None
        pass

    def reload(self):
        # Create all tables in the database and create the current database session (self.__session)
        pass
