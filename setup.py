#!/usr/bin/env python

"""Setup script for 'yapps'"""

from distutils.core import setup

description = "Yet Another Python Parser System"
long_description = \
"""
YAPPS is an easy to use parser generator that is written in Python and
generates Python code.  There are several parser generator systems
already available for Python, but this parser has different goals:
Yapps is simple, very easy to use, and produces human-readable parsers.

It is not the fastest or most powerful parser.  Yapps is designed to be
used when regular expressions are not enough and other parser systems
are too much: situations where you might otherwise write your own
recursive descent parser.

This package contains several upward-compatible enhancements to the
original YAPPS source:
- Handle stacked input ("include files")
- augmented ignore-able patterns (can parse multi-line C comments correctly)
- better error reporting
- read input incrementally
"""

setup (name = "python-yapps",
       version = "2.1.1",
       description = description,
       long_description = long_description,
       author = "Amit J. Patel",
       author_email = "amitp@cs.stanford.edu",
       maintainer = "Matthias Urlichs",
       maintainer_email = "smurf@debian.org",
       url = "http://theory.stanford.edu/~amitp/yapps/",
       license = 'MIT',
       platforms = ['POSIX'],
       keywords = ['parsing'],
       packages = ['yapps'],
       #cmdclass = {'bdist_rpm': MyBDist_RPM},
      )
