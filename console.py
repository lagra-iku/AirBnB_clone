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

    def do_all(self, args):
        """Prints all string rep of all insts based or not on the class name"""
        argv = args.split()
        objs = storage.all()
        instances = []
        if len(argv) > 0 and argv[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            for obj in objs.values():
                if len(argv) == 0 or argv[0] == obj.__class__.__name__:
                    instances.append(obj.__str__())
            print(instances)

    def do_count(self, args):
        """Retrieve the number of instances of a class"""
        argv = args.split()

        if len(argv) == 0:
            print("** class name missing **")
        else:
            class_name = argv[0]
            if class_name not in self.__classes:
                print("** class doesn't exist **")
            else:
                count = eval(class_name).count()
                print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
