Contributing to argparse2
=========================

This page contains information for those contributing to ``argparse2``.


Setting up
----------

To develop locally, clone the repo.

Then run the following from the repo root in a new virtualenv_::

    $ pip install -e .[dev,test]


Running tests
-------------

To run tests::

    $ ./tests.sh

The test runner allows tests to be run with either ``argparse`` or
``argparse2`` as the argparse module.  This makes it easy to see what
test cases the two differ on.


Writing tests
-------------

The repository contains two types of tests: the original unit tests
carried over from CPython's ``argparse`` and new ``argparse2``-specific
tests.

The original ``argparse`` tests are in a single file copied from the CPython
repository (and modified slightly to support importing ``argparse2`` instead
of ``argparse``.   New tests should not be added to this file. This simplifies
keeping the upstream tests in synch with this project.


Building documentation
----------------------

To build and view documentation locally::

    $ cd docs
    $ make html
    $ open _build/html/index.html


.. _virtualenv: https://packaging.python.org/en/latest/installing.html#virtual-environments
