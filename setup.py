#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # None
]

test_requirements = [
    'tox',
]

setup(
    name='generalwords',
    version='1.0',
    description='A somewhat curated collection of words to use in nonce generation.',
    long_description=readme + '\n\n' + history,
    author='Christopher Petrilli',
    author_email='petrilli@amber.org',
    url='https://github.com/petrilli/generalwords',
    packages=[
        'generalwords',
    ],
    package_dir={'generalwords':
                 'generalwords'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD Simplified",
    zip_safe=False,
    keywords='generalwords',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
