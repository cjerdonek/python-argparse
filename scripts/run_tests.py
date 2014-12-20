
import sys
import unittest

def main(argv=None):
    if argv is None:
        argv = sys.argv
    # The following is what `python -m unittest` does in Python 3.4.
    unittest.TestProgram(module=None)

if __name__ == '__main__':
    main()
