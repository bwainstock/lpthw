class Song(object):

        def __init__(self, lyrics):
                self.lyrics = lyrics

        def sing_me_a_song(self):
                for line in self.lyrics:
                        print line

lyrics_happy = ["Happy birthday to you", "I dont", "So I' stop"]
happy_bday = Song(lyrics_happy)

lyrics_bulls = ["Rally around", "Shelllllls"]
bulls_on_parade = Song(lyrics_bulls)

print "Lyrics:"
print bulls_on_parade.lyrics

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

