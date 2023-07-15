#!/usr/binn/python3
""" Defines Review Class """
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherites from BaseModel class

    Args:
        BaseModel (class): A Base Class for sub classes
    """

    user_id = ""
    place_id = ""
    text = ""
