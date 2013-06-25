from functools import wraps

class Command(object):

    def __init__(self, name, func, arg_names):
        self.name = name
        self.func = func
        self.arg_names = arg_names

    def __call__(self, arg_dict):
        values = []
        for name in self.arg_names:
            if name == '*':
                values.append(arg_dict)
            else:
                values.append(arg_dict.get(name, None))
        return self.func(*values)

    def __repr__(self):
        return "<Command {0}({1})>".format(self.name, ", ".join(self.arg_names))


class CommandExists(Exception):
    """ Duplicated command name """
    pass


class CommandNotFound(Exception):
    """ Couldn't find any command to execute """
    pass


class Climate(object):

    def __init__(self):
        self.commands = dict()

    def __call__(self, arg_dict):
        for cmd_name in self.commands.keys():
            if arg_dict.get(cmd_name, False):
                return self.commands[cmd_name](arg_dict)
        raise CommandNotFound

    def add_command(self, name, func, arg_names):
        if name not in self.commands.keys():
            self.commands[name] = Command(name, func, arg_names)
        else:
            raise CommandExists

    def command(self, *args, **kwargs):
        def wrapped_cmd(func):
            cmd_name = kwargs.get('name', None) or func.__name__
            self.add_command(cmd_name, func, args)

            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper

        return wrapped_cmd

    def merge_commands(self, commands):
        for cmd in commands.values():
            self.add_command(cmd.name, cmd.func, cmd.arg_names)

    def merge(self, cli, namespace=None):
        if not namespace:
            self.merge_commands(cli.commands)
        elif namespace not in self.commands.keys():
            self.commands[namespace] = cli
        else:
            raise CommandExists

