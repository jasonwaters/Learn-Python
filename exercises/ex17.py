#!/usr/bin/env python

#http://learnpythonthehardway.org/book/ex17.html

from sys import argv
from os.path import exists

script, from_file, to_file = argv

if exists(from_file):
    indata = open(from_file).read()
    open(to_file, 'w').write(indata)
    print "Congratulations! '%s' ( %d bytes ) was Copied to '%s'" % (from_file, len(indata), to_file)
else:
    print "Sorry, '%s' does not exist." % from_file