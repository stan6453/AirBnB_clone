#!/usr/bin/python3

import json

class FileStorage:
    '''Class for Serialization and Deserialization'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj
        
    def save(self):
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items() if hasattr(v, 'to_dict')}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for k, v in obj_dict.items():
                    obj_dict[k] = eval(f'{v.__class__.__name__}(**v)')
                    self.__objects = obj_dict
        except FileNotFoundError:
            pass

