#!/usr/bin/python3
"""A class Review that inherits from Base_Model"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class Review"""
    place_id = ''
    user_id = ''
    text = ''
