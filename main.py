import pygame
from random import choice, randint
from os import listdir
from sys import exit
from time import sleep
from pydub import AudioSegment
from pydub.utils import mediainfo

def set_songs(song1, song2=None):
    global songs
    if song1 is None:
        sys.exit(0)
    if song2 is None:
        songs = music[song1]
        return
    
    songs = music[song1] + music[song2]

def get_file_seconds(file_path):
    audio = AudioSegment.from_ogg(file_path)
    duration_seconds = audio.duration_seconds
    return duration_seconds

def play_ogg(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    
    finally:
        pygame.mixer.quit()
        pygame.quit()

music = [
    ['background.ogg', 'calm1.ogg', 'calm2.ogg', 'calm3.ogg', 'calm4.ogg', 'calm5.ogg', 'calm6.ogg', 'droopy1.ogg', 'droopy2.ogg', 'far_lands.ogg', 'hal1.ogg', 'hal2.ogg', 'hal3.ogg', 'hal4.ogg', 'infinite_amethyst.ogg', 'moog1.ogg', 'nocturne.ogg', 'nuance1.ogg', 'nuance2.ogg', 'piano1.ogg', 'piano2.ogg', 'piano3.ogg'],

    ['axolotl.ogg', 'background.ogg', 'calm1.ogg', 'calm2.ogg', 'calm3.ogg', 'calm4.ogg', 'calm5.ogg', 'creative1', 'creative2', 'creative3', 'creative4', 'creative5', 'creative6', 'calm6.ogg', 'droopy1.ogg', 'droopy2.ogg', 'far_lands.ogg', 'hal1.ogg', 'hal2.ogg', 'hal3.ogg', 'hal4.ogg', 'infinite_amethyst.ogg', 'moog1.ogg', 'nocturne.ogg', 'nuance1.ogg', 'nuance2.ogg', 'otherside.ogg', 'piano1.ogg', 'piano2.ogg', 'piano3.ogg', 'shuniji.ogg'],

    ['cat.ogg', 'chirp.ogg', 'far.ogg', 'mall.ogg', 'otherside.ogg',  'stal.ogg', 'strad.ogg', 'wait.ogg'],

    ['axolotl.ogg', 'shuniji.ogg'],

    ['axolotl.ogg', 'background.ogg', 'calm1.ogg', 'calm2.ogg', 'calm3.ogg', 'calm4.ogg', 'calm5.ogg', 'calm6.ogg', 'cat.ogg', 'chirp.ogg', 'droopy1.ogg', 'droopy2.ogg', 'far.ogg', 'far_lands.ogg', 'hal1.ogg', 'hal2.ogg', 'hal3.ogg', 'hal4.ogg', 'infinite_amethyst.ogg', 'mall.ogg', 'moog1.ogg', 'nocturne.ogg', 'nuance1.ogg', 'nuance2.ogg', 'otherside.ogg', 'piano1.ogg', 'piano2.ogg', 'piano3.ogg', 'shuniji.ogg', 'stal.ogg', 'strad.ogg', 'wait.ogg']
]

print("""[1] Survival
[2] Creative
[3] Music Discs
[4] Underwater
[5] All
[6] Music Discs + Survival
[7] Music Discs + Creative
[8] Underwater + Survival
[0] Quit
""")

option = int(input("Enter what playlist you want to play: "))
songs = []

options = [
    (None,),
    (0,),
    (1,),
    (2,),
    (3,),
    (4,),
    (5, 0),
    (5, 1),
    (4, 0),
]

# option recebe o input

set_songs(*options[option])


while True:
    chosen_song = choice(songs)
    print("assets/" + chosen_song)
    play_ogg("assets/" + chosen_song)
    time = randint((180 + get_file_seconds("assets/" + chosen_song)))
    sleep(time)
    print(time)
