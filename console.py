#!/usr/bin/python3
"""Defines class cmd"""

import cmd
import json
import models
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sys


class HBNBCommand(cmd.Cmd):
    """command line interpreter class"""
    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_EOF(self, line):
        """Quit when at EOF"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Override default emptyline behaviour"""
        pass

    def do_create(self, args):
        """creates a new instance of base model"""
        if len(args) < 2:
            print("** class name missing **")
        elif args in self.__classes:
            new_instance = eval(str(args) + "()")
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Print the string representation of an instance"""
        argv = args.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] in self.__classes:
            if len(argv) == 1:
                print("** instance id missing **")
            else:
                objs = storage.all()
                check_id = str(argv[0]) + "." + str(argv[1])
                if check_id in objs:
                    print(objs[check_id])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        argv = args.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] in self.__classes:
            if len(argv) == 1:
                print("** instance id missing **")
            else:
                objs = storage.all()
                check_id = str(argv[0]) + "." + str(argv[1])
                if check_id in objs:
                    del(objs[check_id])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
