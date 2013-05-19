#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(name='enzyme',
    version='0.3',
    license=open('LICENSE').read(),
    description='Python video metadata parser',
    long_description=open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),
    keywords='parser video metadata mkv',
    url='https://github.com/Diaoul/enzyme',
    author='Antoine Bertin',
    author_email='diaoulael@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    package_data={'enzyme.parsers.ebml': ['specs/*.xml'], 'enzyme.tests': ['parsers/ebml/*.yml']},
    classifiers=['Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Multimedia :: Video',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    test_suite='enzyme.tests.suite',
    tests_require=['requests', 'PyYAML'])
