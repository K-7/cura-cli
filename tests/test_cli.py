"""Tests for our main k2a CLI module."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase

from k2a import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['k2a', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)

        output = popen(['k2a', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['k2a', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(output.strip(), VERSION)
