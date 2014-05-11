cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_cap = cars_driven * space_in_a_car
ave_pass_per_car = passengers / cars_driven

print "there are", cars, "cars availalbe."
print "there are only", drivers, "drivfers avail."
print "there will be", cars_not_driven, "emptys today."
print "we can take", carpool_cap, "today."
print "we have", passengers, "today."
print "we need to put", ave_pass_per_car, "in each car."
