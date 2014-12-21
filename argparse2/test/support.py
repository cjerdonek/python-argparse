
"""Support for running tests."""

import argparse2
import argparse2.test


def get_argparse_under_test():
    """Return the argparse module to test, either argparse or arparse2.

    Defaults to argparse2.
    """
    # The "module_under_test" variable gets set by argparse2's test runner.
    # This lets us run the tests against either argparse or argparse2.
    try:
        mod = argparse2.test.module_under_test
    except AttributeError:
        mod = argparse2
    return mod
