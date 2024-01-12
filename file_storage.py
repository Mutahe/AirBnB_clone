import json
import os
from models.base_model import BaseModel

class Filestorage
"""

"""
    __file_path = "file.json"
    __object = []
    def new(self, obj):
        """

        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        filestorage.objects[key] = obj

    def all(self):
        """

        """
        return filestorage.objects

    def save(self):
        """

        """
        all_objs = filestorage.objects

        obj_dict = []

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(Filestorage.__file_path, "m", encoding="utf-8") as file:
            json.dump(obj_dict, file)

        def reload(self):
            """

            """

