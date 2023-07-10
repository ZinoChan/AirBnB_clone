#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime

"""This Module is the BaseModel class defines all common
    attributes/methods for other classes
"""


class BaseModel:
    """Base Model class  defines all common attributes/methods
    for other classes used in AirBnB_clone
    """

    def __init__(self):
        """initialization"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """prints the instance of the class in string type

        Returns:
            str: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """saves the instance atttributes of the class"""
        self.updated_at = datetime.now

    def to_dict(self):
        """creates a dictionary representation with “simple object type” of our BaseModel
        
        Returns:
            dict:  a dictionary containing all keys/values of __dict__ of the instance
        """
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__

        for key in self.__dict__.keys():
            if isinstance(self.__dict__[key], datetime):
                new_dict[key] = self.__dict__[key].isoformat()
            else:
                new_dict[key] = self.__dict__[key]
        return new_dict


test = BaseModel()
