#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dictentry = self.__dict__.copy()
        dictentry['__class__'] = self.__class__.__name__
        dictentry['created_at'] = datetime.now().isoformat()
        dictentry['updated_at'] = datetime.now().isoformat()
        return dictentry
