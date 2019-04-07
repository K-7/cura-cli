"""
cura

Usage:
  cura hello
  cura -h | --help
  cura --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  cura hello

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/rdegges/cura-cli
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import cura.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items(): 
        if hasattr(cura.commands, k) and v:
            module = getattr(cura.commands, k)
            cura.commands = getmembers(module, isclass)
            command = [command[1] for command in cura.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
