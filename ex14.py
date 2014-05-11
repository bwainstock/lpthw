from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Nor where that is.
And you havc a %r computer.
""" % (likes, lives, computer)
