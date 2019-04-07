"""
cura

Usage:
  cura git_pull --name=<name> [--url=<url>]
  cura react_component --name=<name> [--path=<path> --sf]
  cura -h | --help
  cura --version

Options:
  -sf| --singlefile  If only a single file component required then pass this parameter


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
