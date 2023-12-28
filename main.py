import pygame
from random import choice, randint
from os import listdir
from sys import exit
from time import sleep
from pydub import AudioSegment
from math import ceil

pitch = 0.25
music_path = "C:/Users/odeni/OneDrive/Documentos/Programas/Python/mmp/"

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

def get_ogg_duration(file_path):
    # Load the OGG file
    audio = AudioSegment.from_file(file_path, format="ogg")

    # Get the duration in seconds
    duration_seconds = len(audio) / 1000.0

    return duration_seconds

def set_songs(song1, song2=None):
    global songs
    if song1 is None:
        sys.exit(0)
    if song2 is None:
        songs = music[song1]
        return
    
    songs = music[song1] + music[song2]
def play_ogg(file_path, volume=1.0, velocity=1.0):
    pygame.init()
    pygame.mixer.init(int(44100 * pitch))

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        pygame.mixer.music.set_volume(volume)
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    
    finally:
        pygame.mixer.quit()
        pygame.quit()

music = [
    ['background.ogg', 'calm1.ogg', 'calm2.ogg', 'calm3.ogg', 'calm4.ogg', 'calm5.ogg', 'calm6.ogg', 'droopy1.ogg', 'droopy2.ogg', 'far_lands.ogg', 'hal1.ogg', 'hal2.ogg', 'hal3.ogg', 'hal4.ogg', 'infinite_amethyst.ogg', 'moog1.ogg', 'nocturne.ogg', 'nuance1.ogg', 'nuance2.ogg', 'piano1.ogg', 'piano2.ogg', 'piano3.ogg', 'flake.ogg', 'ki.ogg', 'kyoto.ogg', 'intro.ogg', 'eleven.ogg'],

    ['background.ogg', 'calm1.ogg', 'calm2.ogg', 'calm3.ogg', 'calm4.ogg', 'calm5.ogg', 'creative1.ogg', 'creative2.ogg', 'creative3.ogg', 'creative4.ogg', 'creative5.ogg', 'creative6.ogg', 'calm6.ogg', 'droopy1.ogg', 'droopy2.ogg', 'far_lands.ogg', 'hal1.ogg', 'hal2.ogg', 'hal3.ogg', 'hal4.ogg', 'infinite_amethyst.ogg', 'moog1.ogg', 'nocturne.ogg', 'nuance1.ogg', 'nuance2.ogg', 'otherside.ogg', 'piano1.ogg', 'piano2.ogg', 'piano3.ogg', 'shuniji.ogg', 'flake.ogg', 'ki.ogg', 'kyoto.ogg', 'intro.ogg', 'eleven.ogg'],

    ['cat.ogg', 'chirp.ogg', 'far.ogg', 'mall.ogg', 'otherside.ogg',  'stal.ogg', 'strad.ogg', 'wait.ogg'],

    ['axolotl.ogg', 'shuniji.ogg'],

    ['axolotl.ogg', 'background.ogg', 'calm1.ogg', 'calm2.ogg', 'calm3.ogg', 'calm4.ogg', 'calm5.ogg', 'calm6.ogg', 'cat.ogg', 'chirp.ogg', 'droopy1.ogg', 'droopy2.ogg', 'far.ogg', 'far_lands.ogg', 'hal1.ogg', 'hal2.ogg', 'hal3.ogg', 'hal4.ogg', 'infinite_amethyst.ogg', 'mall.ogg', 'moog1.ogg', 'nocturne.ogg', 'nuance1.ogg', 'nuance2.ogg', 'otherside.ogg', 'piano1.ogg', 'piano2.ogg', 'piano3.ogg', 'shuniji.ogg', 'stal.ogg', 'strad.ogg', 'wait.ogg', 'flake.ogg', 'ki.ogg', 'kyoto.ogg', 'intro.ogg', 'eleven.ogg']
]

print("""[1] Survival
[2] Creative
[3] Music Discs
[4] Underwater
[5] All
[6] Music Discs + Survival
[7] Music Discs + Creative
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
]


set_songs(*options[option])


while True:
    chosen_song = choice(songs)
    print(music_path + "assets/" + chosen_song)
    duration = ceil(get_ogg_duration(music_path + "assets/" + chosen_song))
    rnd_duration = randint(1,180)
    total_duration = duration + rnd_duration
    print(str(total_duration//60)+"m "+str(total_duration%60)+"s")
    play_ogg(music_path + "assets/" + chosen_song)
    sleep(rnd_duration)
