import sys, os, feedparser, BeautifulSoup

if len(sys.argv) >1:
    print "first argument is: %s" % sys.argv[1]
else:
	print "no agument was supplied"
print '================='


if True:
    print "it's true"
else:
    print "it's false"


count=1
max=15
your_mom_is_dumb=True

while count <= max:
    print 'number',count
    count+=1

if your_mom_is_dumb:
    print "your mom is dumb!!"

def wtf(something):
    print "wtf %s" % something

wtf("bobbo!")
wtf("blip!")




print '================='
myList = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']
myList.sort()
for item in myList:
    print item