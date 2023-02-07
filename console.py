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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
