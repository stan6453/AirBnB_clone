#!/usr/bin/python3

class FileStorage:
    '''Class for Serialization and Deserialization'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f'{obj.__class.__name}.{obj.id}'] = obj
    def save(self):
