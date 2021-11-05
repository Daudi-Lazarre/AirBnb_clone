#!/usr/bin/python3
from models.base_model import BaseModel
"""
    File: user.py
"""


class User(BaseModel):
    """User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes User with empty values"""
        super().__init__(*args, **kwargs)