#!/usr/bin/python3
'''
Command line interpreter for the Airbnb cmd interface
'''

import cmd
import shlex

import models
from models.base_model import BaseModel
from models.user import User

CLASSES = [
    "BaseModel",
    "User",
    "City",
    "Place",
    "State",
    "Amenity",
    "Review"
]


class HBNBCommand(cmd.Cmd):
    """Airbnb command processor/interpreter."""

    prompt = '(hbnb) '
    storage = models.storage

    def do_EOF(self, line):
        '''End the program on EOF'''
        return True

    def do_quit(self, line):
        '''End the program when quit cmd is typed'''
        return True

    def emptyline(self):
        '''Do nothing when an empty line is entered'''
        pass

    def do_create(self, line):
        '''Create a new instance of BaseModel, saves it (to the JSON file) and prints the id.'''
        arr = shlex.split(line)
        if len(arr) == 0:
            print('** class name missing **')
            return None
        if arr[0] not in CLASSES:
            print("** class doesn't exist **")
            return None

        '''Code that does actual work'''
        print(eval(arr[0])().id)
        self.storage.save()

    def do_show(self, line):
        '''Print the string representation of an instance based on the class name and id'''
        arr = shlex.split(line)
        if len(arr) == 0:
            print('** class name missing **')
            return None
        if arr[0] not in CLASSES:
            print("** class doesn't exist **")
            return None
        if len(arr) < 2:
            print("** instance id missing **")
            return None

        '''Code that deos the main work'''
        key = "{}.{}".format(arr[0], arr[1])
        if key not in self.storage.all():
            print("** no instance found **")
        else:
            print(self.storage.all()[key])

    def do_destroy(self, line):
        ''' Delete an instance based on the class name and id (save the change into the JSON file).'''
        arr = shlex.split(line)
        if len(arr) == 0:
            print('** class name missing **')
            return None
        if arr[0] not in CLASSES:
            print("** class doesn't exist **")
            return None
        if len(arr) < 2:
            print("** instance id missing **")
            return None

        key = "{}.{}".format(*arr)
        if key in self.storage.all():
            del self.storage.all()[key]
            self.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        '''Print all string representation of all instances based or not on the class name.'''
        arr = shlex.split(line)
        objects = self.storage.all().values()
        if not arr:
            print([str(obj) for obj in objects])
        else:
            if len(arr) > 0 and arr[0] not in CLASSES:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                       if arr[0] in str(obj)])

    def do_update(self, line):
        '''
        Update an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file)
        '''
        arr = shlex.split(line)
        if len(arr) == 0:
            print('** class name missing **')
            return None
        if arr[0] not in CLASSES:
            print("** class doesn't exist **")
            return None
        if len(arr) < 2:
            print("** instance id missing **")
            return None
        if len(arr) < 3:
            print("** attribute name missing **")
            return None
        if len(arr) < 4:
            print("** value missing **")
            return None

        instance_id = "{}.{}".format(arr[0], arr[1])

        if instance_id in self.storage.all():
            obj = self.storage.all()[instance_id]
            if arr[2] in type(obj).__dict__:
                v_type = type(obj.__class__.__dict__[arr[2]])
                setattr(obj, arr[2], v_type(arr[3]))
            else:
                setattr(obj, arr[2], arr[3])
        else:
            print("** no instance found **")

        self.storage.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
