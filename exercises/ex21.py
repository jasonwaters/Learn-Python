#!/usr/bin/env python

#http://learnpythonthehardway.org/book/ex21.html

def add(a,b):
    result = a+b
    print "%d + %d = %d" % (a,b,result)
    return result

def subtract(a,b):
    result = a-b
    print "%d - %d = %d" % (a,b,result)
    return result

def multiply(a,b):
    result = a*b
    print "%d * %d = %d" % (a,b,result)
    return result

def divide(a,b):
    result = a/b
    print "%d / %d = %d" % (a,b,result)
    return result

print "Let's do some math with just functions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"