#!/usr/bin/python3
"""
Console the pain of working alone
"""

import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """
    Quit, eof and empty line implementations
    """

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
        Exit the terminal
        """
        sys.exit()

    def do_EOF(self, arg):
        """
        End of file (ctrl + d)
        """
        return True

    def empty_line(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()