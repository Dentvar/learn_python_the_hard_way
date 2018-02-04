class song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = [  "Happy birthday to you",
                "I don't want to get sued.",
                "So I'll stop right there"]

bulls_on_parade = [ "They rally around tha family",
                    "With pockets full of shells"]

song1 = song(happy_bday)
song2 = song(bulls_on_parade)

print("\n")
song1.sing_me_a_song()
print("\n")
song2.sing_me_a_song()
print("\n")