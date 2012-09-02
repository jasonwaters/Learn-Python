#http://learnpythonthehardway.org/book/ex10.html

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t*Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

for i in ["/","-","|","\\","|"]:
    print "%s\t\t%r\r" % (i,i)

    # %r is for debugging
    # %s is for people

print '''
is be am are was
were been has have
had do did 'does'
may can might
must shall will
would should "could"
'''