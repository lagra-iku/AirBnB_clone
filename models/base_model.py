#!/usr/bin/python3
"""Model that defines all common attributes/methods for other classes"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """A class that defines common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """Update the 'updated_at' attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary with key-value pairs from the object's attr.

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
        # obj_dict["created_at"] = self.created_at.isoformat()
        # obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Returns a human-readable string representation of the object.
            Returns:
            str: A string containing the class name, id, and attr of the obj.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.to_dict()
        )
