#!/usr/bin/python3
<<<<<<< HEAD
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if pline[0] is '{' and pline[-1] is'}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, args):
        """ Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method to show an individual object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        # guard against trailing args
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """ Destroys a specified object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage._FileStorage__objects.items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                print_list.append(str(v))

        print(print_list)

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        for k, v in storage._FileStorage__objects.items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def do_update(self, args):
        """ Updates a certain object with new info """
        c_name = c_id = att_name = att_val = kwargs = ''

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # class name not present
            print("** class name missing **")
            return
        if c_name not in HBNBCommand.classes:  # class name invalid
            print("** class doesn't exist **")
            return

        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # id not present
            print("** instance id missing **")
            return

        # generate key from class and id
        key = c_name + "." + c_id

        # determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] is '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name was not quoted arg
            if not att_name and args[0] is not ' ':
                att_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] is '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # retrieve dictionary of current objects
        new_dict = storage.all()[key]

        # iterate through attr names and values
        for i, att_name in enumerate(args):
            # block only runs on even iterations
            if (i % 2 == 0):
                att_val = args[i + 1]  # following item is value
                if not att_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:  # check for att_value
                    print("** value missing **")
                    return
                # type cast as necessary
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                # update dictionary with name, value pair
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # save updates to file

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")

if __name__ == "__main__":
=======
"""
    This module defines the shell
    interactive console
"""

import cmd
import re
import models
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
        Defines a class HBNBCommand that inherits
        from the Cmd Class
    """
    prompt = "(hbnb) "

    list_of_models = ["BaseModel", "User", "State",
                      "Review", "City", "Amenity", "Place"]

    def onecmd(self, line):
        sp = (line.split(" "))
        print(sp)
        print(sp[0])
        """I will be updating the way the arguments are passed"""
        if "." in line and "(" in line and ")"\
                in line and '"' in line and "," in line:
            pattern = r"(\w+).(\w+)\(\"?(\w+-?\w+-?" \
                      r"\w+-?\w+-?\w+)\"?,?\s\"?(\w+)\",?\s\"?(\w+)\"?\)"
            replacement = r"\2 \1 \3 \4 \5"

            line = re.sub(pattern=pattern, repl=replacement, string=line)

        elif "." in line and "(" in line and ")" in line and '"' in line:
            pattern = r"(\w+).(\w+)\(\"(\w+-\w+-\w+-\w+-\w+)\"\)"
            replacement = r"\2 \1 \3"

            line = re.sub(pattern=pattern, repl=replacement, string=line)

        elif "." in line:
            pattern = r"(\w+).(\w+)\(\)"
            replacement = r"\2 \1"

            line = re.sub(pattern=pattern, repl=replacement, string=line)
        return cmd.Cmd.onecmd(self, line)

    def do_quit(self, line):
        """quit program"""
        return True

    def do_EOF(self, line):
        """ end with a new line"""
        print()
        return True

    def help_quit(self):
        """helper for quit"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """helper for EOF"""
        print("EOF command to exit the program")

    def emptyline(self):
        """do nothing for empty line"""
        pass

    def validate_line(self, line):
        """ Validate not empty line"""
        if line == "":
            print("** class name missing **")
            return False

    def validate_base_model(self, line):
        """validate class name"""
        parts = line.split(" ")
        if parts[0] not in self.list_of_models:
            print("** class doesn't exist **")
            return False
        elif len(parts) == 1 and parts[0] in self.list_of_models:
            print("** instance id missing **")
            return False

    def validate_id(self, line):
        """validate the id"""
        parts = line.split(" ")
        model_id = "{}.{}".format(parts[0], parts[1])
        all_object = models.storage.all()
        if model_id not in all_object.keys():
            print("** no instance found **")
            return False

    def validate_attribute_value(self, line):
        """ validate the attribute and value"""
        parts = line.split(" ")
        if len(parts) == 2:
            print("** attribute name missing **")
            return False
        elif len(parts) == 3:
            print("** value missing **")
            return False

    def do_create(self, line):
        """ create new class instance"""
        split_pm = line.split(" ")
        print(split_pm)
        check = self.validate_line(split_pm[0])
        if check is False:
            return
        if line in self.list_of_models:
            model = eval(line)()
            #model.save()
            #print(model.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """helper function for create doc"""
        print("Create command to make a new Model Instance")

    def do_show(self, line):
        """Show object string representation"""
        check = self.validate_line(line)
        if check is False:
            return
        check = self.validate_base_model(line)
        if check is False:
            return
        check = self.validate_id(line)
        if check is False:
            return
        else:
            parts = line.split(" ")
            model_id = "{}.{}".format(parts[0], parts[1])
            get_obj = models.storage.all()
            print(get_obj[model_id])

    def help_show(self):
        """helper function for show"""
        print("Show Command to"
              " Print the string repr of an instance based"
              " on the class name and id")

    def do_destroy(self, line):
        """Destroy an object"""
        check = self.validate_line(line)
        if check is False:
            return

        check = self.validate_base_model(line)
        if check is False:
            return

        check = self.validate_id(line)
        if check is False:
            return

        else:
            parts = line.split(" ")
            model_id = "{}.{}".format(parts[0], parts[1])
            get_obj = models.storage.all()
            del get_obj[model_id]
            models.storage.save()

    def help_destroy(self):
        """Helper function for destroy"""
        print("destroy command"
              " deletes an instance based on the"
              " class name and id")

    def do_all(self, line):
        """print all objects available"""
        get_obj = models.storage.all()
        if line == "":
            all_obj = ["{}".format(value) for value in get_obj.values()]
            print(all_obj)
        elif line in self.list_of_models:
            for key, value in get_obj.items():
                found_key = key.split(".")
                if found_key[0] == line:
                    print(value)
        else:
            print("** class doesn't exist **")

    def help_all(self):
        """helper for all"""
        print("all command prints all instances"
              " in a list format")

    def do_update(self, line):
        """update <class name> <id> <attribute name> '<attribute value>'"""

        check = self.validate_line(line)
        if check is False:
            return

        check = self.validate_base_model(line)
        if check is False:
            return

        check = self.validate_id(line)
        if check is False:
            return

        check = self.validate_attribute_value(line)
        if check is False:
            return

        else:
            parts = line.split(" ")
            model_id = "{}.{}".format(parts[0], parts[1])
            attr_name = parts[2]
            attr_val = parts[3].strip(' "')  # remove the forward slash

            if attr_val.isdigit():
                attr_val = int(attr_val)
            else:
                try:
                    attr_val = float(attr_val)
                except Exception:
                    pass

            get_obj = models.storage.all()
            setattr(get_obj[model_id], attr_name, attr_val)
            get_obj[model_id].save()

    def help_update(self):
        """helper for update"""
        print("command update to update with attribute")

    def do_count(self, line):
        """This command for counting the number
        of instances of a class"""
        count = 0
        if line == "":
            return
        elif line in self.list_of_models:
            get_obj = models.storage.all()
            for key in get_obj.keys():
                found_key = key.split(".")
                if found_key[0] == line:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def help_count(self):
        """helper for count"""
        print("count command to see the "
              "number of instances available for the class")


if __name__ == '__main__':
>>>>>>> 91310892488144876cc4d5934e96d6128e29871d
    HBNBCommand().cmdloop()
