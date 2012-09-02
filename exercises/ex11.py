#http://learnpythonthehardway.org/book/ex11.html
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh (lbs)?",
weight = raw_input()

print "\n\nSo, you're %s old, %s tall and %s lbs." % (age, height, weight)

daddy = raw_input("Who is your daddy?")
do = raw_input("What does he do?")

print "\n\nYour daddy is %s, and he %s." % (daddy, do)