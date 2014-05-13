"""
Direction words: north, south, east, west, down, up, left, right, back.
Verbs: go, stop, kill, eat.
Stop words: the, in, of, from, at, it
Nouns: door, bear, princess, cabinet.
Numbers: any string of 0 through 9 characters.
"""
#Class Scanner(object):

#        def __init__(self):
#                pass
def scan(stuff):
        direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
        verb = ['go', 'stop', 'kill', 'eat']
        stop = ['the', 'in', 'of', 'from', 'at', 'it']
        noun = ['door', 'bear', 'princess', 'cabinet']

       # stuff = raw_input('> ')
        words = stuff.split()
        print "WORDS: ", words
        sentence = []
        nextWord = ()
        wordIndex = 0

        for word in words:
                if word in direction:
                        nextWord = ('direction', word)
                elif word in verb:
                        nextWord = ('verb', word)
                elif word in stop:
                        nextWord = ('stop', word)
                elif word in noun:
                        nextWord = ('noun', word)
                else:
                        try:
                                nextWord = ('number', int(word))
                        except ValueError:
                                nextWord = ('error', word)
                
                sentence.append(nextWord)

        #print sentence
        return sentence
#scan()

