#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

this_directory = os.path.abspath(os.path.dirname(__file__))

setup_requirements = ['pytest-runner', ]


def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(
    author="Han Zhichao",
    author_email='superhin@126.com',
    description='Get and load testdata in pytest projects',
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.7',
    ],
    license="MIT license",
    include_package_data=True,
    keywords=[
        'pytest', 'py.test', 'relative path', 'datetime format path'
    ],
    name='pytest-testdata',
    packages=find_packages(include=['pytest_testdata']),
    setup_requires=setup_requirements,
    url='https://github.com/hanzhichao/pytest-testdata',
    version='0.1.0',
    zip_safe=True,
    install_requires=[
        'pytest',
        'pytest-runner',
        'filez'
    ],
    entry_points={
        'pytest11': [
            'pytest-testdata = pytest_testdata.plugin',
        ]
    }
)
