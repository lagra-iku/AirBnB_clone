#!/usr/bin/python3
"""Defines class cmd"""

import cmd


class HBNBCommand(cmd.Cmd):
    """command line interpreter class"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Quit when at EOF"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Override default emptyline behaviour"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
