#!/usr/bin/python3
""" This Module contains the entry
    point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, args):
        """
        Creates a new instance of BaseModel
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
            return
        new_instance = self.allowed_classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of
        an instance based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        instance = storage.all()
        if key in instance:
            print(instance[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based
        on the class name and id.
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        instances = storage.all()
        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Displays all instances, or all
        instances of a class if specified.
        """
        args = arg.split()

        instances = storage.all()

        display_list = []

        if len(args) > 0:
            class_name = args[0]

            if class_name not in self.allowed_classes:
                print("** class doesn't exist **")
                return

            for key, instance in instances.items():
                if class_name in key:
                    display_list.append(str(instance))
        else:
            for instance in instances.values():
                display_list.append(str(instance))

        print(display_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        instances = storage.all()

        if key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        if attribute_name in ["id", "created_at", "updated_at"]:
            return

        attr_value = args[3].strip("\"")
        try:
            attr_value = int(attr_value)
        except ValueError:
            try:
                attr_value = float(attr_value)
            except ValueError:
                pass

        setattr(instances[key], attribute_name, attr_value)
        instances[key].save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
