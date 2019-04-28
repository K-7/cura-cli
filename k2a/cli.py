"""
k2a

Usage:
  k2a git_pull --name=<name> [--url=<url>]
  k2a react_component --name=<name> [--path=<path> --sf]
  k2a activate
  k2a -h | --help
  k2a --version

Options:
  -sf| --singlefile  If only a single file component required then pass this parameter


"""

from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import k2a.commands
    options = docopt(__doc__, version=VERSION)
    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(k2a.commands, k) and v:
            module = getattr(k2a.commands, k)
            k2a.commands = getmembers(module, isclass)
            command = [command[1] for command in k2a.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
