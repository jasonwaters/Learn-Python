#http://learnpythonthehardway.org/book/ex15.html
from sys import argv

filename = argv[1] if len(argv) >= 2 else "ex15_sample.txt"

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()
txt_again.close()
