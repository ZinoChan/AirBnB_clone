#!/usr/bin/python3
""" This Module contains the entry
    point of the command interpreter
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    allowed_classes = {"BaseModel": BaseModel}

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_quit(self, args):
        """Quits the command line"""
        return True

    def do_EOF(self, args):
        """End of File"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
