YAPPS is an easy to use parser generator that is written in Python and generates
Python code.
There are several parser generator systems already available for Python, but
this parser has different goals: Yapps is simple, very easy to use, and produces
human-readable parsers.

It is not the fastest or most powerful parser.
Yapps is designed to be used when regular expressions are not enough and other
parser systems are too much: situations where you might otherwise write your own
recursive descent parser.

This package contains several upward-compatible enhancements to the original
YAPPS source:

* Handle stacked input ("include files").
* Augmented ignore-able patterns (can parse multi-line C comments correctly).
* Better error reporting.
* Read input incrementally.
