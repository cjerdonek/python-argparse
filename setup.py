# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import os


PACKAGE_NAME = "argparse2"


setup(
    name='argparse2',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version='0.5.0-alpha1',
    license='Python Software Foundation License',
    # The project homepage.
    url='https://github.com/cjerdonek/python-argparse',

    description="Fork of Python's argparse to add features and simplify its code",
    keywords='argparse argparse2 command line parser parsing',

    author='Chris Jerdonek',
    author_email='chris.jerdonek@gmail.com',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
    ],

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=[]),

    # To install dependencies for an extra from a source distribution,
    # you can do the following, for example:
    #
    #   $ pip install -e .[dev,test]
    #
    extras_require = {
        'dev':  [
            'check-manifest',
            'twine >=1.3,<1.4',
        ],
        'test':  [
            'coverage',
        ],
    },

)
