argparse2
=========

[![Build Status](https://travis-ci.org/cjerdonek/python-argparse.svg?branch=master)](https://travis-ci.org/cjerdonek/python-argparse)
[![Coverage Status](https://img.shields.io/coveralls/cjerdonek/python-argparse.svg)](https://coveralls.io/r/cjerdonek/python-argparse?branch=master)
[![Documentation Status](https://readthedocs.org/projects/argparse2/badge/?version=latest)](https://readthedocs.org/projects/argparse2/?badge=latest)


This is a fork of the the Python standard library's [`argparse`][argparse]
module.  The [project page][argparse2_github] is on GitHub.

``argparse2`` is distributed for free on [PyPI][argparse2_pypi] and the
source code is hosted on [GitHub][argparse2_github].  Project documentation
is hosted on [Read the Docs][argparse2_docs].

The purposes of the fork include--

* improving the extensibility of argparse,
* simplifying the code and improving its maintainability, and
* adding features.

We aim to preserve backwards compatibility for the most part.  We
anticipate breaking backwards compatibility only in the case of warts
and "documented bugs."

The main work being done so far is simplifying the code base.  Up to
this point, all of the test cases in the original CPython implementation
continue to pass.


Background
----------

The code in the original argparse module is complicated.  Moreover, being
part of CPython, the pace of change to the module is slow.  This
makes major refactorings impractical or not possible.
As Guido van Rossum is fond of saying, modules in the standard library
have "one foot in the grave."

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


Contributing
------------

For information on developing and contributing to `argparse2`, see
the [development docs][argparse2_docs_dev]


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


[argparse]: https://docs.python.org/library/argparse.html
[argparse2_docs]: http://argparse2.readthedocs.org/en/latest/index.html
[argparse2_docs_dev]: http://argparse2.readthedocs.org/en/latest/developing.html
[argparse2_github]: https://github.com/cjerdonek/python-argparse
[argparse2_pypi]: https://pypi.python.org/pypi/argparse2
