# Set x equal to a string, including a decimal formatter
x = "There are %d types of people." % 10
# Set variable binary equal to a string
binary = "binary"
# Contract "do not" using a variable
do_not = "don't"
# Set variable y equal to a string including multiple formatters
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# Print a string including a formatter inside another string with formatter
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_eval = "Isn't that joke so funny?! %r"

print joke_eval % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# Concattanate
print w + e
