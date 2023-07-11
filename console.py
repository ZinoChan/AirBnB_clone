#!/usr/bin/python3
import cmd
""" This Module contains the entry point of the command interpreter

"""


class HBNBCommand(cmd.Cmd):
    """ Command Interpreter

    Args:
        cmd (ob): object of the module cmd
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Quit Command to exit the program
        """
        return True

    def do_EOF(self, line):
        """ Ctr-D exit the program
        """
        return True

    def emptyline(self):
        """Ensures that empty line + ENTER doesn't execute anything
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
