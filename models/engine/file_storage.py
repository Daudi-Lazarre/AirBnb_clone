#!/usr/bin/python3
""" This is file storage """

from models.base_model import BaseModel
import json

class FileStorage:
    """ Stores file data """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return all of the data """
        return FileStorage.__objects

    def new(self, obj):
        """ Store new data """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ Save the data. """
        stored_saves = {}
        for key, value in FileStorage.__objects.items():
            stored_saves[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as fd:
            json.dump(stored_saves, fd, indent=2)

    def reload(self):
        """ Deserialize JSON """
        try:
            with open(FileStorage.__file_path, mode="r", encoding="UTF-8") as fd:
                deserialize = json.load(fd)
        except FileNotFoundError:
            pass
