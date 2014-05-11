print ("You enter a dark room with two doors.  Do you go through door #1"
        "or door #2 or go through the hatch?")

door = raw_input(" >")

if door =="1":
    print "There's a giant bear eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear =="1":
        print "The bear eats your face off.  Good job!"
    elif bear == "2":
        print "the bear eats your legs off.  Good jobs!"
    else:
        print "Well, doing %s is probably better." % bear

elif door =="2":
    print "You stare into the endless abyss."
    print "1. Blueberries."
    print "2. Crazy guys eyes."
    print "3. Depressed like a bitch."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives."
    else:
        print "The insanity rots your eyes."

elif door == "hatch":
    print "You jumped into a hole in the floor.  That was a weird choice."
    print "1.  Well, I had nothing better to do."
    print "2.  Help me, I can't find my dog!"
    print "3. Fuck you buddy.  You don't know me!"

    weirdo = raw_input("> ")

    if weirdo == "1":
        print "Perhaps you'd like to answer more questions."
        print "1.  What's your favorite color?"
        print "2.  What's your favorite team?"
        
        favorite = raw_input("> ")

        if favorite == "1" or favorite == "2":
            print "I don't give a shit, I'm not asking you that!"
        else:
            print "Hey, fuck nut, you forgot to answer. Get out!"
    
    elif weirdo == "2":
        print "I didn't see a dog.  Go away."
    else:
        print "Who cares anymore.  This is working."

else:
    print "You are an idiot.  Die!"
