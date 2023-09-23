#!/usr/bin/python3
"""Define the FileStorage class"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

list_of_classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
}


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""

        with open(self.__file_path, "w") as f:
            json_dict = {key: value.to_dict() for key,
                         value in self.__objects.items()}
            json.dump(json_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                json_dict = json.load(f)
            self.__objects = {}
            for key, value in json_dict.items():
                class_name = value["__class__"]
                value.pop("__class__", None)
                if class_name in list_of_classes:
                    cls = list_of_classes[class_name]
                    obj = cls(**value)
                    self.__objects[key] = obj
        else:
            return
