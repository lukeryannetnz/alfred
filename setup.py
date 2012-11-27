#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='travis-demo',
      version='0.1',
      description='Travis Django app demo.',
      author='Mathijs de Bruin',
      author_email='mathijs@mathijsfietst.nl',
      url='https://github.com/visualspace/travis-demo/',
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
