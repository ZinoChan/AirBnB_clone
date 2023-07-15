#!/usr/binn/python3
""" Defines City Class """
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherites from BaseModel class

    Args:
        BaseModel (class): A Base Class for sub classes
    """

    name = ""
    state_id = ""
