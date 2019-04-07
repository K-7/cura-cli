#!/usr/bin/python
"""
Python script to generate React Component Template which follows style guideline
command: python cgenerator.py -p ./ -n filename -sf
-sf indicates whether its a single file component
-p indicates the path
-n indicates the component & file/folder name
"""

import os
import re

from .base import Base


class ReactComponent(Base):
    def run(self):
        name = self.options['--name']
        single_file = self.options['--sf']
        path = self.options.get('--path', './')
        absolute_path = os.path.join(os.getcwd(), path)
        directory_path = os.path.join(path, name)

        tsx_content = """import React, {{ Component }} from 'react';
import {{ connect }} from 'react-redux';
class {0} extends Comkponent<any,any> {{
  constructor(props:any){{
    super(props);
  }}
  render() {{
    return <div>
    Replace the content
    </div>
  }}
}}"""
        scss_content = ''
        test_content = ''

        self.execute(
            name,
            single_file,
            absolute_path,
            directory_path,
            tsx_content,
            scss_content,
            test_content
        )

    def execute(self, name, single_file, absolute_path, directory_path, tsx_content, scss_content, test_content):
        if single_file:
            with open(self.__get_file_path(absolute_path, '{0}.tsx'.format(name)), 'w+') as fp:
                fp.write(tsx_content.format(name))
        else:
            self.__create_directory(directory_path)
            with open(self.__get_file_path(directory_path, 'index.tsx'), 'w+') as fp:
                fp.write(tsx_content.format(name))

            with open(self.__get_file_path(directory_path, 'index.scss'), 'w+') as fp:
                fp.write(scss_content)

            with open(self.__get_file_path(directory_path, 'index.test.ts'), 'w+') as fp:
                fp.write(test_content)

        print
        '=================================='
        print
        '{0} component got created at {1}'.format(name, absolute_path)
        print
        '=================================='

    def __create_directory(self, path):
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)

    def __pascal_case(self, chars):
        word_regex_pattern = re.compile('[^A-Za-z]+')
        words = word_regex_pattern.split(chars)
        return ''.join(w.title() for i, w in enumerate(words))

    def __get_file_path(self, path, filename):
        return path + "/" + filename
