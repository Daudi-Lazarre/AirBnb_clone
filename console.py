#!/usr/bin/python3
"""
Console the pain of working alone
"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.place import Place

class HBNBCommand(cmd.Cmd):
    """
    Quit, eof and empty line implementations
    """

    prompt = "(hbnb)"
    class_list = {
        "BaseModel": BaseModel, "User": User, "State": State,
        "Review": Review, "City": City, "Amenity": Amenity, "Place": Place
    }

    def do_quit(self, arg):
        """
        Exit the terminal
        """
        return True

    def do_EOF(self, arg):
        """
        End of file (ctrl + d)
        """
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """ Create new basemodel with new info """
        # Split separates string into a list
        new_argument = arg.split()
        if len(new_argument) == 0:
            print("** class name missing **")
        elif new_argument[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            new_model = self.class_list[new_argument[0]]()
            new_model.save()
            print(new_model.id)
    
    def do_show(self, arg):
        """ Print strrep of objects """
        new_argument = arg.split()
        class_id = ""
        if len(new_argument) >= 2:
            class_id = new_argument[0] + "." + new_argument[1]
        if not arg:
            return print("** class name missing **")
        elif len(new_argument) == 1:
            return print("** instance id missing **")
        elif new_argument[0] not in self.class_list:
            return print("** class doesn't exist **")
        try:
            x = models.storage.all()[class_id]
            print(x)
        except Exception:
            return print("** no instance found **")

    def do_destroy(self, arg):
        """
        Removes object from class
        """
        new_argument = arg.split()
        if len(new_argument) == 0:
            print("** class name missing **")
        elif len(new_argument) == 1:
            print("** instance id missing **")
        elif new_argument[0] not in models.available_classes:
            print("** class doesn't exist **")
        else:
            stored_data = models.storage.all()

            for i in stored_data:

                if i == "{}.{}".format(new_argument[0], new_argument[1]):
                    del stored_data[i]
                    models.storage.save()
                    return
            print("** no instance found **")
            models.storage.save()

    def do_all(self, arg):
        """
        Output everything as a string
        """
        new_argument = arg.split()
        if len(new_argument) >= 1:
            if new_argument[0] not in self.available_classes:
                print("** class doesn't exist **")
            else:
                for i in models.storage.all():
                    print(i)
        else:
            for i in models.storage.all():
                print(i)

    def do_update(self, arg):
        new_argument = arg.split()
        class_id = ""
        if len(new_argument) >= 2:
            class_id = new_argument[0] + "." + new_argument[1]
        if not arg:
            return print("** class name missing **")
        elif new_argument[0] not in self.class_list:
            return print("** class doesn't exist **")
        elif len(new_argument) < 2:
            return print("** instance id missing **")
        elif len(new_argument) < 3:
            return print("** attribute name missing **")
        elif len(new_argument) < 4:
            return print("** value missing **")
        try:
            setattr(models.storage.all()[class_id],
                    new_argument[2], new_argument[3])
            models.storage.save()
        except Exception:
            return print("** no instance found **")

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
