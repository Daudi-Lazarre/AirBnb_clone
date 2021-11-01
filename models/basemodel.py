#!/usr/bin/python3
""" Base class: AirBnb """

import uuid
from uuid import uuid4
from datetime import date as datetime

# Classes are real-world objects
# I like cars, so think of a car
# In the class, there are different pieces of data that 
# make up the wheels, suspension, engine, etc.

class BaseModel(object):
    """ Initializing the base class """

    date_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """ Start building the basemodel """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def str(self):
        """ String representation of base model """
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """ Saves basemodel with the date """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """ Returns dictionary of base model
        ISO format returns date, time format
         """
        to_dictionary_and_beyond = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                to_dictionary_and_beyond[key] = value.isoformat()
            else:
                to_dictionary_and_beyond[key] = value
                to_dictionary_and_beyond["__class__"] = type(self).__name__
