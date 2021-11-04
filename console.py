#!/usr/bin/python3
"""
Console the pain of working alone
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Quit and help implementations
    """

    prompt = "(hbnb)"

    def do_quit(self, *args):
        """
        Exit the terminal
        """
        return True

    def do_EOF(self, arg):
        """
        End of file (ctrl + d)
        """
        return True

    def empty_line(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()