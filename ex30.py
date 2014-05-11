people = 30
cars = 40
buses = 15


if cars > people:
    print "We should take cars."
elif cars < people:
    print "We should not take carts."
else:
    print "We can't decide."

if buses > cars:
    print "Too many buses."
elif buses < cars:
    print "Buses"
else:
    print "Cant' decide."

if people > buses:
    print "Alright, buses.."
else:
    print "Fine, stay home"
