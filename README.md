YAPPS: Yet Another Python Parser System
----------------------------------------

For the most complete and excellent documentation (e.g. [manual with
examples](http://theory.stanford.edu/~amitp/yapps/yapps2/manual/)) and info,
please see original project website: http://theory.stanford.edu/~amitp/yapps/

YAPPS is an easy to use parser generator that is written in Python and generates
Python code.
There are several parser generator systems already available for Python, but
this parser has different goals: Yapps is simple, very easy to use, and produces
human-readable parsers.

It is not the fastest or most powerful parser.
Yapps is designed to be used when regular expressions are not enough and other
parser systems are too much: situations where you might otherwise write your own
recursive descent parser.

This fork contains several upward-compatible enhancements to the original
YAPPS source, originally included in [debian package](http://packages.debian.org/sid/yapps2):

 * Handle stacked input ("include files").
 * Augmented ignore-able patterns (can parse multi-line C comments correctly).
 * Better error reporting.
 * Read input incrementally.


Installation
----------------------------------------

It's a regular package for Python 2.7 (not 3.X, but there are links to 3.X
patches listed on the [original author
website](http://theory.stanford.edu/~amitp/yapps/)), but not in pypi, so can be
installed from a checkout with something like that:

	% python setup.py install

Better way would be to use [pip](http://pip-installer.org/) to install all the
necessary dependencies as well:

	% pip install 'git+https://github.com/mk-fg/yapps.git#egg=yapps'

Note that to install stuff in system-wide PATH and site-packages, elevated
privileges are often required.
Use "install --user",
[~/.pydistutils.cfg](http://docs.python.org/install/index.html#distutils-configuration-files)
or [virtualenv](http://pypi.python.org/pypi/virtualenv) to do unprivileged
installs into custom paths.

Alternatively, `./yapps2` can be run right from the checkout tree, without any
installation, just run "python setup.py build" beforehand.

No extra package dependencies.
