
import argparse
import os.path
import sys
import unittest

# This is a hack to work around this coverage bug:
# https://bitbucket.org/ned/coveragepy/issue/348
sys.path.insert(0, os.getcwd())

import argparse2.test

def main(argv=None):
    if argv is None:
        argv = sys.argv

    # Set the argparse module to test.
    # TODO: make this toggleable with a command-line argument.
    argparse2.test.module_under_test = argparse2
    # The following is what `python -m unittest` does in Python 3.4.
    unittest.TestProgram(module=None)

if __name__ == '__main__':
    main()
