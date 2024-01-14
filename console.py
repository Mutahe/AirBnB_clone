#!/bin/usr/python3
"""this function will contain the entry point of the commandline interpreter"""

import cmd
import json
import re
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """tokenizes the commands"""
    curly_brackets = re.search(r"\{(.*?)\}", arg)
    square_brackets = re.search(r"\[(.*?)\]", arg)
    if curly_brackets is None:
        if square_brackets is None:
            return [a.strip for a in split(arg)]
        else:
            lexer = split(arg[:square_brackets.span()[0]])
            elements = [a.strip(", ") for i in lexer]
            elements.append(square_brackets.group())
            return elememts

    else:
        lexer = split(arg[:curly_brackets.span()[0]])
        elements = [i.strip(",") for i in lexer]
        elements.append(curly_brackets.group())
        return elements


class HBNBCommand(cmd.Cmd):
    """entry point of the command line interpreter"""
    prompt = "(hbnb) "

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """do not nothing when an empty line is received"""
        pass
    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            ArgumentOne = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [ArgumentOne[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """uses quit command to exit the program"""
        return True
    def help_quit(self, arg):
        """
        """
        print("type Quit to exit the program")

    def do_EOF(self, arg):
        """uses EOF signal to exit the program"""
        print("")
        return True

    def do_create(self, arg):
        """creates a new instance of the base model and prints its id"""
        ArgumentOne = shlex.split(arg)

        if len(ArgumentOne) == 0:
            print("** class name missing **")

        elif ArgumentOne[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        ArgumentOne = shlex.split(arg)

        if len(ArgumentOne) == 0:
            print("** class name missing **")
        elif ArgumentOne[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(ArgumentOne) == 1:
            print("** instance id missing **")
        else:
            odict = storage.all()

            key = "{}.{}".format(argl[0], ArgumentOne[1])
            if key in odict:
                print(odict[key])
            else:
                print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        ArgumentOne = parse(arg)
        objdict = storage.all()

        if len(ArgumentOne) == 0:
            print("** class name missing **")
            return False
        if ArgumentOne[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(ArgumentOne) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(ArgumentOne[0], ArgumentOne[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(ArgumentOne) == 2:
            print("** attribute name missing **")
            return False
        if len(ArgumentOne) == 3:
            try:
                type(eval(ArgumentOne[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(ArgumentOne) == 4:
            obj = objdict["{}.{}".format(ArgumrntOne[0], ArgumentOne[1])]
            if ArgumrntOne[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[ArgumentOne[2]])
                obj.__dict__[ArgumentOne[2]] = valtype(ArgumentOne[3])
            else:
                obj.__dict__[ArgumentOne[2]] = ArgumrntOne[3]
        elif type(eval(ArgumentOne[2])) == dict:
            obj = objdict["{}.{}".format(ArgumentOne[0], ArgumentOne[1])]
            for k, v in eval(ArgumentOne[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        ArgumentOne = parse(arg)

        objdict = storage.all()

        if len(ArgumentOne) == 0:
            print("** class name missing **")
        elif ArgumentOne[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(ArgumentOne) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(ArgumentOne[0], ArgumentOne[1]) not in objdict.keys():
            print("** instance id missing **")
        elif "{}.{}".format(ArgumentOne[0], ArgumentOne[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(ArgumentOne[0], ArgumentOne[1])]
            storage.save()

    def do_count(self, arg):
        """Retrieve the number of instances of a given class."""
        ArgumentOne = parse(arg)
        count = 0
        for obj in storage.all().values():
            if ArgumentOne[0] == obj.__class__.__name__:
                count += 1
        print(count)
    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        ArgumentOne = parse(arg)
        if len(ArgumentOne) > 0 and ArgumentOne[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(ArgumentOne) > 0 and ArgumentOne[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(ArgumentOne) == 0:
                    objl.append(obj.__str__())
            print(objl)






if __name__ == "__main__":
    HBNBCommand().cmdloop()
        
