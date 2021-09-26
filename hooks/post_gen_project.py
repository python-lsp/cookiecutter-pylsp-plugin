#!/usr/bin/env python
import os
import shutil


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        os.remove('LICENSE')

    if 'Github' != '{{ cookiecutter.repository_type }}':
        remove_file('.github')

    if 'pytest' != '{{ cookiecutter.test_type }}':
        os.remove('test/conftest.py')
        os.remove('test/test_plugin.py')
