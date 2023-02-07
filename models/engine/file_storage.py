#!/usr/bin/python3

import json
from models.base_model import BaseModel
class FileStorage:
    '''Class for Serialization and Deserialization'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f'{obj.__class.__name}.{obj.id}'] = obj
    def save(self):
        obj_dict = (v.to_dict() for k, v in self.__objects.items())
        with open(self.__file_path, 'w') as file:
            json.dumps(obj_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                json.load(file)
        except FileNotFoundError:
            pass

