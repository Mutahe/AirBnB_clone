#!/bin/usr/python3
"""defines the BaseModel class"""
import models
from datetime import datetime
from uuid import uuid4

class BaseModel:
    """this is the base model of the HBnB project"""

    def __init__(self, *args, **kwargs):
        """initializing the base model"""

        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k = "created_at" or k = "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timeformat)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """saves updated_at with the current datetime it was changed"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns the dictionary representation of the basemodel"""

        mdict = self.__dict__.copy()
        mdict["created_at"] = self.created_at.isoformat()
        mdict["updated_at"] = self.updated_at.isoformat()
        mdict["__class__"] = self.__class__.__name__

        return mdict

    def __str__(self):
        """returns the print/str represenation of the basemodel instance"""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
