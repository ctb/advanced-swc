#! /usr/bin/env python
import doctest
import sys

for filename in sys.argv[1:]:
    print '... running doctests on', filename
    doctest.testfile(filename)

print '*** SUCCESS ***'
