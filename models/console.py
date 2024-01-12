#!/bin/usr/python3
import cmd

"""this function will contain the entry point of the commandline interpreter"""

class HBNBCommand(cmd.Cmd):
    """entry point of the command line interpreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """do not nothing when an empty line is received"""
        pass

    def do_quit(self, arg):
        """uses quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """uses EOF signal to exit the program"""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
        
