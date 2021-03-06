"""Tests for our `k2a hello` subcommand."""

import os
from subprocess import PIPE
from subprocess import Popen as popen
from unittest import TestCase


class TestReactComponent(TestCase):
    def test_component_creation(self):
        popen(['k2a', 'react_component', '--name=testComp'], stdout=PIPE).communicate()
        if not os.path.isdir("./TestComp"):
            self.assertTrue(True, msg='Failed to create component !!')

        popen(['rm', '-rf', 'testComp'], stdout=PIPE).communicate()
