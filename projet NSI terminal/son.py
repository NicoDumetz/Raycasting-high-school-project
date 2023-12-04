# Créé par mourchiaym, le 05/05/2023 en Python 3.7
import pygame as pg
from pygame.locals import *

pg.init()

def son(sound):
    pg.mixer.music.set_volume(1.0)
    #temps_actuel=pg.mixer.music.get_pos()
    pg.mixer.music.load(sound)
    pg.mixer.music.play(0)
    #pg.mixer.music.set_pos(temps_actuel)
    #print(temps_actuel)
    while pg.mixer.music.get_busy():
        pass
    pg.mixer.music.set_volume(0.4)
    pg.mixer.music.load(jetpack)
    pg.mixer.music.play(-1)

jetpack="fantome.mp3"
pg.mixer.music.load(jetpack)
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.4)