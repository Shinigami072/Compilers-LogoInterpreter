#!/usr/bin/env python

from setuptools import setup, find_packages, find_namespace_packages

setup(
    name='interpreter',
    version='1.0',
    description='Python Distribution Utilities',
    author='Shinigami072',
    author_email='krzys.stasiowski@gmail.com',
    url='www.github.com/Shinigami072',
    setup_requires=['setuptools-antlr'],
    install_requires=['antlr4-python3-runtime'],
    zip_safe=False,
    tests_require=['unittest2'],
    test_suite='tests.test_main',
    packages=find_packages(exclude="tests")
)
