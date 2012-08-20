__author__ = 'jasonwaters'
print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'
print "-------------------------------"

print "hens", 25+30 /6
print "roosters", 100-25*3%4

print 3+2+1-5+4%2-1/4+6

print "Is it true that 3+2 < 5 -7?"
print "-------------------------------"

cars=100
space_in_a_car= 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven,"empty cars today."
print "-------------------------------"

name = "Jason Waters"
age = 29 #truth
height = 60
weight = 260
eyes = "blue"
teeth = "White"
hair = 'Brown'

print "Let's talk about %s" % name
print "He's %d inches tall." % height
print "he's %d lbs" % weight
print "He's got %s eyes and %s hair." % (eyes, hair)
print "If I add %d, %d, and %d I get %d." % (age,height,weight,age+height+weight)

print "-------------------------------"

x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." %x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side"

print w + e

print "EX7-------------------------------"
