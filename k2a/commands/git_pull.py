"""The hello command."""

from subprocess import PIPE, Popen as popen

from .base import Base


class GitPull(Base):
    """Pull repos from GIT"""

    def run(self):
        name = self.options['--name']
        url = self.options['--url']

        if name == 'socket-redis':
            self.__pull_repo(url or 'git@github.com/K-7/socket_redis_implementation')
        elif name == 'dicom-ios':
            self.__pull_repo(url or 'git@github.com/K-7/dicom-ios')

    def __pull_repo(self, url):
        popen(['git', 'clone', url], stdout=PIPE).communicate()
