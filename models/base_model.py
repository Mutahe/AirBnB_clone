#!/bin/usr/python3
"""defines the BaseModel class"""
from datetime import datetime
from uuid import uuid4
import models
class BaseModel:
    """this is the base model of the HBnB project"""

    def __init__(self, *args, **kwargs):
        """initializing the base model"""

        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k == "created_at" or k == "updated_at":
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

        mydict = self.__dict__.copy()
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["__class__"] = self.__class__.__name__

        return mydict

    def __str__(self):
        """returns the print/str represenation of the basemodel instance"""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
