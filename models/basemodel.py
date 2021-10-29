#!/usr/bin/python3
""" Base class: AirBnb """

import uuid
from uuid import uuid4
from datetime import datetime

# Classes are real-world objects
# I like cars, so think of a car
# In the class, there are different pieces of data that 
# make up the wheels, suspension, engine, etc.

class BaseModel(object):
    """ Initializing the base class """

    def __init__(self, *args, **kwargs):
        """ Start building the basemodel """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    