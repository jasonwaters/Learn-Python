#!/usr/bin/env python

#http://learnpythonthehardway.org/book/ex40.html
import ex40stuff

mystuff = {'apple': 'I AM APPLES!'}
print mystuff['apple']

ex40stuff.apple()
print ex40stuff.tangerine

class MyStuff(object):
    tangerine = 'alf'
    bunk = "bUNK"
    def __init__(self):
        self.tangerine = "orange orange orange"

    def apple(self):
        print "I AM RED APPLES!"

s = MyStuff()
s.apple()
print s.tangerine
print s.bunk

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()