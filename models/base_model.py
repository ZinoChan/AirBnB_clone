#!/usr/bin/env python3
import uuid
from datetime import datetime

class BaseModel:
    """
    Defines all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"
                        )
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            from models import storage
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance for serialization.
        """
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = dict_rep["created_at"].isoformat()
        dict_rep["updated_at"] = dict_rep["updated_at"].isoformat()
        return dict_rep

