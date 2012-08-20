import sys, os, feedparser, BeautifulSoup

__author__ = 'jasonwaters'

count=1
max=15
your_mom_is_dumb=1

while count <= max:
    print 'number',count
    count+=1

if your_mom_is_dumb:
    print "your mom is dumb!!"

def wtf(something):
    print "wtf %s" % something

wtf("bobbo!")
wtf("blip!")

if len(sys.argv) >1:
    print "first argument is: %s" % sys.argv[1]