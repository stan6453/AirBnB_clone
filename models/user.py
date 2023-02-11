#!/usr/bin/python3
'''
Module For User Class
'''
import models
from models.base_model import BaseModel

class User(BaseModel):
    '''User Class that inherits from BaseModel'''
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    @classmethod
    def all(cls):
        return [cls(**obj.__dict__) for obj in models.storage.all().values() if obj.__class__.__name__ == cls.__name__] 
