#!/usr/bin/env python

#http://learnpythonthehardway.org/book/ex31.html

prompt = "> "

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input(prompt)

if door == "1":
    print """
    There's a giant bear here eating a cheese cake. What do you do?
    1. Take the cake.
    2. Scream at the bear.
    """

    bear = raw_input(prompt)

    if bear == "1":
        print "The bear eats your face off. Good Job!"
    elif bear == "2":
        print "The bear eats your legs of. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print """
    You stare into the endless abyss at Cthulhu's retina.
    1. Blueberries.
    2. Yellow jacket clothespins.
    3. Understanding revolvers yelling melodies.
    """
    insanity = raw_input(prompt)

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good Job!"
else:
    print "You stumble around and fall on a knife and die. Good job!"
