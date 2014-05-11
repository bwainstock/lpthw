# Create a mapping of state to abbreviation

states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
        }

# create a basic set of states and some cities in them
cities = {
        'CA': 'San Francisco',
        'FL': 'Jacksonville',
        'MI': 'Detroit'
        }

# add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print '-' * 10
print "Michigan's abb is: ", states['Michigan']
print "Florida's abb is: ", states['Florida']

print '-' * 10
for state, abbrev in states.items():
        print "%s is abbreviated %s" % (state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
        print "%s has the city %s" % (abbrev, city)

print '-' * 10
for state, abbrev in states.items():
        print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
state = states.get('Texas', None)

if not state:
        print "sorry, no Texas."

city = cities.get('TX', 'Does Not Exist')
print "the city for the state TX is: %s" % city
