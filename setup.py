#!/usr/bin/env python

"""Setup script for 'yapps'"""

from distutils.core import setup

description = "Yet Another Python Parser System"
long_description = \
"""
This module implements a recursive-descent parser in Python.
"""

setup (name = "python-shellwords",
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
