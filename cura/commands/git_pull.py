"""The hello command."""

from subprocess import PIPE, Popen as popen

from .base import Base


class GitPull(Base):
    """Pull repos from GIT"""

    def run(self):
        name = self.options['--name']
        url = self.options['--url']

        if name == 'web-react':
            self.__pull_repo(url or 'git@bitbucket.org:curatech/webcorecomponents.git')
        elif name == 'server-main':
            self.__pull_repo(url or 'git@bitbucket.org:curatech/cura_server.git')
        elif name == 'ios-diabetes':
            self.__pull_repo(url or 'git@bitbucket.org:curatech/diabetes2.0.git')
        elif name == 'ios-cardiac':
            self.__pull_repo(url or 'git@bitbucket.org:curatech/cardiac_ios.git')

    def __pull_repo(self, url):
        popen(['git', 'clone', url], stdout=PIPE).communicate()
