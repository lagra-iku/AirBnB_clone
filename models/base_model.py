#!/usr/bin/python3
"""Model that defines all common attributes/methods for other classes"""
from datetime import datetime
from uuid import uuid4
import models
from models import storage


class BaseModel:
    """A class that defines common attributes/methods for other classes"""
    instances = []

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (keyword arguments): Key/value pairs of attributes.
        """
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    dtime = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, dtime)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Update the 'updated_at' attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary with key-value pairs from the obj's attributes

        Returns:
            dict: A dictionary with all the instance attributes and values.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                obj_dict[key] = value.isoformat()
            else:
                obj_dict[key] = value
        return obj_dict

    def __str__(self):
        """Returns a human-readable string representation of the object.
        Returns:
            str: A string with the class name, id, & attributes of the obj.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def count(cls):
        """count the no of instances"""
        return len(cls.instances)
