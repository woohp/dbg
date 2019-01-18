#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='dbg',
    version='0.1',
    packages=find_packages(exclude=('tests',)),
)
