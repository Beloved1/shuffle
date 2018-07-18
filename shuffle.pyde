from random import *
# Note: Check console for result

songs = [
    "My Song",
    "Bekfast",
    "Cholla",
    "Lust",
    "In the air",
    "Clocks",
    "Fireflies",
]

def play(track):
   print(track) 


for i in range(8):
    track = randint(0, len(songs)-1)
    play(songs[track])
