
numbers = []
def topBottom(x, step):
    i = 0
    while i < x:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i = i + step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

print "How big of a list?"
listsize = raw_input("> ")
print "How big of a step?"
stepsize = raw_input("> ")

topBottom(int(listsize), int(stepsize))


print "The numbers: "

for num in numbers:
    print num
