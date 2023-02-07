#!/usr/bin/python3
'''
Command line interpreter for the Airbnb cmd interface
'''

import cmd

models = ['BaseModel']

class HBNBCommand(cmd.Cmd):
    """Airbnb command processor/interpreter."""

    prompt = '(hbnb) '

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
        arr = line.split()
        if len(arr) == 0:
            print('** class name missing **')
            return None
        if arr[0] not in models:
            print("** class doesn't exist **")
            return None

        #Create an instance of BaseModel

        #Save to the json file

        #Print its id

    def do_show(self, line):
        '''Print the string representation of an instance based on the class name and id'''
        arr = line.split()
        if len(arr) == 0:
            print('** class name missing **')
            return None
        if arr[0] not in models:
            print("** class doesn't exist **")
            return None
        if len(arr) < 2:
            print("** instance id missing **")
            return None

            #Search and print instace

            #if no instance id is fount, print error(edit)
            if False:
                print("** no instance found **")
                return None

    def do_destroy(self, line):
        ''' Delete an instance based on the class name and id (save the change into the JSON file).'''
        arr = line.split()
        if len(arr) == 0:
            print('** class name missing **')
            return None
        if arr[0] not in models:
            print("** class doesn't exist **")
            return None
        if len(arr) < 2:
            print("** instance id missing **")
            return None

        #load json from file

        #search for object based on its id

        #delete the object fom the array

        #save the remeaining back to json file

        #if no instance id is fount, print error(edit)
        if False:
            print("** no instance found **")
            return None

    def do_all(self, line):
        '''Print all string representation of all instances based or not on the class name.'''
        arr = line.split()
        if len(arr) > 0 and arr[0] not in models:
            print("** class doesn't exist **")
            return None

        #print string repesentaion based on selected Model
        if len(arr) > 0:
            model = arr[0]

        #print all insatnces if the Model is not given


    def do_update(self, line):
        '''
        Update an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file)
        '''
        arr = line.split()
        if len(arr) == 0:
            print('** class name missing **')
            return None
        if arr[0] not in models:
            print("** class doesn't exist **")
            return None
        if len(arr) < 2:
            print("** instance id missing **")
            return None

        #if id object not found, print error and return (edit)
        if False:
            print("** no instance found **")
            return None

        if len(arr) < 3:
            print("** attribute name missing **")
            return None
        if len(arr) < 4:
            print("** value missing **")
            return None

        #load json

        #search for entrey with the particular id
        for i in arr:
            print(i)

        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
