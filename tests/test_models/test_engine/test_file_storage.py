#!/usr/bin/python3
'''
Unittests for FileStorage Class
'''
import unittest
import json
from models import base_model, storage
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    '''Class to run unittests for FileStorage'''

    def setup(self):
        '''Setup instance of BaseModel to run tests'''
        base = base_model.BaseModel()

    def delete_file(self):
        '''Delete file if it exists'''
        storage._FileStorage__objects = {}
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_attr_check(self):
        '''Check for necessary attributes'''
        self.assertTrue(hasattr(storage, '_FileStorage__objects'))
        self.assertTrue(hasattr(storage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(storage, 'all'))
        self.assertTrue(hasattr(storage, 'new'))
        self.assertTrue(hasattr(storage, 'save'))
        self.assertTrue(hasattr(storage, 'reload'))

    def test_type(self):
        '''Check for relevant types'''
        self.assertEqual(type(storage), FileStorage)
        self.assertEqual(type(storage._FileStorage__file_path), str)
        self.assertEqual(type(storage._FileStorage__objects), dict)
        self.assertEqual(type(storage.all()), dict)

    def test_all(self):
        '''Tests for all method'''
        self.delete_file()
        self.assertEqual(storage.all(), {})
        with self.assertRaises(TypeError):
            storage.all(1)
            storage.all('string')
            storage.all(None)

    def test_new(self):
        '''Tests for new method'''
        self.delete_file()
        base = base_model.BaseModel()
        storage.new(base)
        base_id = f'{base.__class__.__name__}.{base.id}'
        self.assertEqual(storage.all(), {base_id: base})
        self.assertEqual(len(storage.all()), 1)
        with self.assertRaises(TypeError):
            storage.new(base, 1)
            storage.new('test.json')
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_save(self):
        '''Tests for save method'''
        self.delete_file()
        base = base_model.BaseModel()
        storage.new(base)
        base_id = f'{base.__class__.__name__}.{base.id}'
        storage.save()
        with open('file.json', 'r') as file:
            self.assertEqual(json.load(file), {base_id: base.to_dict()})
        with self.assertRaises(TypeError):
            storage.save(1)
            storage.save('string')
            storage.save(None)

    def test_reload(self):
        '''Tests for reload method'''
        self.delete_file()
        base = base_model.BaseModel()
        storage.new(base)
        base_id = f'{base.__class__.__name__}.{base.id}'
        storage.save()
        storage.reload()
        self.assertEqual(storage.all()[base_id].to_dict(), base.to_dict())
        with self.assertRaises(TypeError):
            storage.reload(1)
            storage.reload('string')
            storage.reload(None)


if __name__ == '__main__':
    unittest.main()
