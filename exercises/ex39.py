#!/usr/bin/env python

#http://learnpythonthehardway.org/book/ex39.html

stuff = {
    'name': "Jason Waters",
    'age':  30,
    'location': "Utah",
    'favorite color': "Orange",
}

print stuff['name']
print stuff['age']
print stuff['location']
print stuff['favorite color']

del stuff['location']
print "="*40

for key,value in stuff.iteritems():
    print "%s : %s" % (key,value)

print "="*40

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville', 'NY': 'New York', 'OR': 'Portland'}

# add some more cities

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city