#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='alfred',
      version='0.1',
      description='Alfred home automation app.',
      author='LukeR',
      url='https://github.com/lukeryannetnz/alfred/',
      packages=find_packages(),
      license='License :: Public Domain',

      # Enable django-setuptest
      test_suite='setuptest.setuptest.SetupTestSuite',
      tests_require=(
        'django-setuptest',
        # Required by django-setuptools on Python 2.6
        'argparse'
      ),
)
