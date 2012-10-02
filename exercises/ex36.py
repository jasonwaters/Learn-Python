#!/usr/bin/env python

#http://learnpythonthehardway.org/book/ex36.html

something = 10

if True:
    something = 20

print "it's %s" % something

arr = [1,2,3,4,5,6,7,8,9,0]

for num in arr:
    print num


done = False
i = 0

print "="*20

while not done:
    print arr[i]
    i+=1
    if i == len(arr):
        done = True
