TODO
====

* Expose a way to customize the help header for a particular action:
  http://stackoverflow.com/questions/9234258/in-python-argparse-is-it-possible-to-have-paired-no-something-something-arg
* Get docs working with Sphinx.
* Fix up long description.
* DRY up the indenting used in the first and second passes.
  - Include subcommand groups in the determination of `_compute_max_action_length()`.
* Make sure `__version__` in `__init__.py` is synched.
* Support adding a parser instance for sub-commands.
