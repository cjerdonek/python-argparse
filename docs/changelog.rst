``argparse2`` — Summary of changes
==================================

This page contains a summary of ``argparse2`` changes.


Next version (TBD)
------------------

* Simplified and refactored some formatting-related code (e.g. parts
  of the ``HelpFormatter`` class).
* [CPython `issue #14037`_]: Added an ``add_parser_group()`` method to let
  subcommands be organized in groups.


0.1.0
-----

* Forked the following files from CPython version 3.5.0 alpha 1 on
  November 27, 2014 (changeset ``93622:167d51a54de2`` from the
  `CPython repository`_):

    * ``Lib/argparse.py``
    * ``Lib/test_argparse.py``
    * ``Doc/library/argparse.rst``


.. _CPython repository: https://hg.python.org/cpython/
.. _issue #14037: http://bugs.python.org/issue14037
