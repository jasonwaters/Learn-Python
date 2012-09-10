#!/usr/bin/env python

#http://learnpythonthehardway.org/book/ex5.html
my_name = 'Jason Waters'
my_age = 30 # not a lie
my_height = 70 # inches
my_weight = 399 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds fat." % my_weight
print "that's pretty heavy!"
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the diet coke." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# %s = String (converts any Python object using str()).
# %d = Signed integer decimal.
# %r = String (converts any Python object using repr()). (%r will give you the "raw programmer's" version of variable, also known as the "representation")
# see http://docs.python.org/library/stdtypes.html#string-formatting-operations