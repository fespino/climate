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
