# use argv module from system modules
from sys import argv

# assign argv propertoes to two variables
# this allows you to pass arguments from the CLI and store them as vars
script, filename = argv

# open filename specified in argument.  assign contents to var
txt = open(filename)

# use read() subcommand to display contents of txt variable
print "Here's your file %r:" % filename
print txt.read()

txt.close()
