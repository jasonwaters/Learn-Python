#!/usr/bin/env python

#http://learnpythonthehardway.org/book/ex18.html

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothin'."

def print_alot(*args):
    i = 1
    for arg in args:
        print "[alot] arg %d: %s" % (i,arg)
        i+=1

print_two("Jason", "Waters")
print_two_again("Jason","Waters")
print_one("Uno!")
print_none()
print_alot("one","two",'Three',"four",'five',"six","seven",'eight','nine','TEN')