#http://learnpythonthehardway.org/book/ex16.html
from sys import argv

filename = argv[1] if len(argv) >= 2 else "ex15_sample.txt"

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, "w")

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

def writeLine(tgt, line):
    tgt.write(line)
    tgt.write("\n")

writeLine(target, line1)
writeLine(target, line2)
writeLine(target, line3)

print "And finally, we close it."
target.close()
