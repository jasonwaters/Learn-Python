#!/usr/bin/env python

#http://learnpythonthehardway.org/book/ex28.html

def jAssert(expected, result):
    if expected != result:
        print "FAIL"
        exit(0)


jAssert(True, True and True)
jAssert(False, False and True)
jAssert(False, 1 == 1 and 2 == 1)
jAssert(True, "test" == "test")
jAssert(True, 1 == 1 or 2 != 1)
jAssert(True, True and 1 == 1)
jAssert(False, False and 0 != 0)
jAssert(True, True or 1 == 1)
jAssert(False, "test" == "testing")
jAssert(False, 1 != 0 and 2 == 1)
jAssert(True, "test" != "testing")
jAssert(False, "test" == 1)
jAssert(True, not (True and False))
jAssert(False, not (1 == 1 and 0 != 1))
jAssert(False, not (10 == 1 or 1000 == 1000))
jAssert(False, not (1 != 10 or 3 == 4))
jAssert(True, not ("testing" == "testing" and "Zed" == "Cool Guy"))
jAssert(True, 1 == 1 and not ("testing" == 1 or 1 == 0))
jAssert(False, "chunky" == "bacon" and not (3 == 4 or 3 == 3))
jAssert(False, 3 == 3 and not ("testing" == "testing" or "Python" == "Fun"))

print "PASS!"