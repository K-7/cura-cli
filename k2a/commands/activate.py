"""The hello command."""

from subprocess import PIPE, Popen as popen

from .base import Base


class Activate(Base):
    """Activate the virtual env in the folder"""

    def run(self):
        popen(['source', 'env/bin/activate'], stdout=PIPE).communicate()
