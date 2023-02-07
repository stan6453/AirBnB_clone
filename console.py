#!/usr/bin/python3
'''
Command line interpreter for the Airbnb cmd interface
'''

import cmd

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

    def do_show(self, line):
        '''Print the string representation of an instance based on the class name and id'''

    def do_destroy(self, line):
        ''' Delete an instance based on the class name and id (save the change into the JSON file).'''

    def do_all(self, line):
        '''Print all string representation of all instances based or not on the class name.'''

    def do_update(self, line):
        '''
        Update an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file)
        '''



if __name__ == '__main__':
    HBNBCommand().cmdloop()
