argparse2
=========

[![Build Status](https://travis-ci.org/cjerdonek/python-argparse.svg?branch=master)](https://travis-ci.org/cjerdonek/python-argparse)
[![Coverage Status](https://img.shields.io/coveralls/cjerdonek/python-argparse.svg)](https://coveralls.io/r/cjerdonek/python-argparse?branch=master)

This is a fork of Python's [`argparse`][argparse] module.

Some of the purposes of the fork are to improve the extensibility of
the module, to simplify the code and improve its maintainability,
and to add features, while preserving backwards compatibility for the
most part.  The main work being done so far is refactoring in an effort
to simplify the code base.

Up to this point, all of the test cases in the original CPython
implementation still pass.  We anticipate breaking backwards compatibility
only in the case of warts and "documented bugs."

The PyPI page for the project is [here][argparse2-pypi].


Background
----------

The code in the original argparse module is complicated.  Moreover,
as part of the CPython code base, the pace of change to the module
is slow.  This makes major refactorings impractical or not possible.
As Guido van Rossum is fond of saying (partly with tongue-in-cheek),
code in the standard library has "one foot in the grave."

This project was started to break free of those constraints and breathe
new life into argparse.  The module was forked from the tip of the
CPython tree (Python 3.5.0 alpha 1) on November 27, 2014.  See the
[`CHANGELOG`](CHANGELOG) file for more details.


Requirements
------------

* Python 3.4 or higher.


Install
-------

    $ pip install argparse2


Testing
-------

Setup:

    $ pip install coveralls

From the repo root:

    $ python -m unittest


Author
------

The author of the fork is Chris Jerdonek (<chris.jerdonek@gmail.com>).
The original author of argparse is Steven J. Bethard.


License
-------

This project is licensed under a BSD 3-Clause License.  For complete
license information, see the [`LICENSE`](LICENSE) file.


Copyright
---------

Copyright (c) 2014 Chris Jerdonek.  All rights reserved.

Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
2011, 2012, 2013, 2014 Python Software Foundation.  All rights reserved.

Copyright (c) 2000 BeOpen.com.  All rights reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All rights reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum.  All rights
reserved.


[argparse]: https://docs.python.org/3/library/argparse.html
[argparse2-pypi]: https://pypi.python.org/pypi/argparse2