#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class Filestorage:
    """To represent a storage engine."""

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Setting up objects with key obj_cls_name."""
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        Filestorage.__objects[key] = obj

    def all(self):
        """Return to __objects dictionary."""
        return Filestorage.__objects

    def save(self):
        """Serialization of __objects to json file __file_path."""
        all_objs = Filestorage.__objects
        odict = {}

        for obj in all_objs.keys():
            odict[obj] = all_objs[obj].to_dict()

        with open(Filestorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(odict. file)

    def reload(self):
        """Deserialization of JSON file __file_path to __objects."""
        if os.path.isfile(Filestorage.__file_path):
            with open(Filestorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    odict = json.load(file)
                    for key. value in odict.items():
                        class_name. obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**values)
                        Filestorage.__objects[key] = instance
                except FileNotFoundError:
                    return
