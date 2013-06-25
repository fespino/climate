CliMate 0.1-dev
---------------

A tiny CLI builder that can be used with [docopt](http://docopt.org/).

## Examples:

    """
        SayWorld

        Usage:
            say hello [--shout] <name>...
            say bye [--times=<times>]
            say (-h | --help)
            say --version

        Options:
            -h --help           Show this screen.
            --version           Show version.
            --shout             Shout out loud.
            --times=<times>     Bye * <times> [default: 2].
    """

    from docopt import docopt
    from climate import Climate

    cli = Climate()

    @cli.command('--shout', '<name>')
    def hello(shout, names):
        greeting = "Hello " + ", ".join(names)
        print(greeting.upper() if shout else greeting)

    @cli.command('--times')
    def bye(times):
        print("Bye " * int(times))

    cli(docopt(__doc__, version='SayWorld 1.0'))

You can merge multiple Climate instances (namespaced or not):

    """
        SayWorld

        Usage:
            say hello [--shout] <name>...
            say bye [--times=<times>]
            say something (useful | stupid)
            say whatever
            say (-h | --help)
            say --version

        Options:
            -h --help           Show this screen.
            --version           Show version.
            --shout             Shout out loud.
            --times=<times>     Bye * <times> [default: 2].
    """

    from docopt import docopt
    from climate import Climate

    cli = Climate()

    @cli.command('--shout', '<name>')
    def hello(shout, names):
        greeting = "Hello " + ", ".join(names)
        print(greeting.upper() if shout else greeting)

    @cli.command('--times')
    def bye(times):
        print("Bye " * int(times))

    second_cli = Climate()

    @second_cli.command()
    def useful():
        print("Screwdriver")

    @second_cli.command()
    def stupid():
        print("SOPA")

    third_cli = Climate()

    @third_cli.command()
    def whatever():
        print("Whatever...")

    cli.merge(second_cli, namespace='something')
    cli.merge(third_cli)

    cli(docopt(__doc__, version='SayWorld 2.0'))

By default the command name is the decorated function name but it can be changed:

    """
        SayWorld

        Usage:
            say hi [--shout] <name>...
            say (-h | --help)
            say --version

        Options:
            -h --help           Show this screen.
            --version           Show version.
            --shout             Shout out loud.
    """

    from docopt import docopt
    from climate import Climate

    cli = Climate()

    @cli.command('--shout', '<name>', name='hi')
    def hello(shout, names):
        greeting = "Hello " + ", ".join(names)
        print(greeting.upper() if shout else greeting)

    cli(docopt(__doc__, version='SayWorld 3.0'))

If you want to pass the entire argument dictionary you can use the wildcard, `*` as the parameter name in the decorator.


