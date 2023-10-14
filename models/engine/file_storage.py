#!/usr/bin/python3
"""A class FileStorage that serializes to and from JSON"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """A class filestorage"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """serializes objects to json file"""
        new = {}
        for obj in self.__objects:
            new[obj] = self.__objects[obj].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(new, file)

    def reload(self):
        """deserializes the json file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as fd:
                deserialized_data = json.load(fd)
                for value in deserialized_data.values():
                    class_Name = value["__class__"]
                    self.new(eval(class_Name)(**value))
