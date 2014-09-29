#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import simplecontent

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = simplecontent.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-simple-content',
    version=version,
    description=""""Basic app to manage contents inside a django project"""",
    long_description=readme + '\n\n' + history,
    author='Andres Gonzalez',
    author_email='andresgz@gmail.com',
    url='https://github.com/andresgz/django-simple-content',
    packages=[
        'simplecontent',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-simple-content',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)