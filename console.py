#!/usr/bin/python3
"""Defines class cmd"""

import cmd


class HbnbCmd(cmd.Cmd):
    """command line interpreter class"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Quit when at EOF"""
        return True

    def do_quit(self, line):
        """Exit the CLI."""
        return True

    def emptyline(self):
        """Override default emptyline behaviour"""
        pass


if __name__ == '__main__':
    HbnbCmd().cmdloop()
