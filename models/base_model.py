#!/usr/bin/env python3
'''
Module for BaseModel
'''
from uuid import uuid4
from datetime import datetime


class BaseModel:
    '''
    BaseModel Class: All future classes subclasses it. \
    Contains attributes common to all classes
    '''
    def __init__(self):
        '''
        Intanstiation of the class.
        Args: (self)
        '''
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        '''
        String Representation of the class.
        Args: (self)
        '''
        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        '''
        Updates the public instance attribute\
        updated_at with the current datetime.
        Args: (self)
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        returns a dictionary containing all keys/values\
        of __dict__ of the instance.
        Args: (self)
        '''
        dictentry = self.__dict__.copy()
        dictentry['__class__'] = self.__class__.__name__
        dictentry['created_at'] = datetime.now().isoformat()
        dictentry['updated_at'] = datetime.now().isoformat()
        return dictentry
