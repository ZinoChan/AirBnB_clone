#!/usr/binn/python3
""" Defines Amenity Class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherites from BaseModel class

    Args:
        BaseModel (class): A Base Class for sub classes
    """

    name = ""
