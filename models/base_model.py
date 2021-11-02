#!/usr/bin/python3
""" Base class: AirBnb """

import uuid
from uuid import uuid4
from datetime import datetime

import models

class BaseModel(object):
    """ Initializing the base class
    Classes are real-world objects
    Like a car... the pieces that make a car
    are in a class """

    date_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """ Start building the basemodel
        Accepted data types include self, argument pointers and 
        keyword arg pointers
        Remember: self allows access to attributes and methods
         """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            """ Keyword args to parse time """
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def str(self):
        """ String representation of base model """
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """ Saves basemodel with the date """
        self.updated_at = datetime.now()
        models.storage.save()
        
    
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
        
        return to_dictionary_and_beyond
