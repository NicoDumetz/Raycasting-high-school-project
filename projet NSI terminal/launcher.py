# Créé par lerouxjul, le 03/03/2023 en Python 3.7
import pygame as pg
from main import *

fps = 60

pg.init()

pg.display.set_caption("NiCommando Launcher")

taille_ecran = (840, 536)
ecran = pg.display.set_mode(taille_ecran)

icon = pg.image.load("jule/icon.png").convert_alpha()
pg.display.set_icon(icon)

fenetre_en_cours = True

horloge_fps = pg.time.Clock()


image_fond = pg.image.load("jule/bg3.jpg")
image_fond = pg.transform.scale(image_fond, (840, 536))
fond = image_fond.convert_alpha()
ecran.blit(fond,(0,0))

bouton_jouer = pg.image.load("jule/play.png")
boutongame= bouton_jouer.convert_alpha()
bouton_rect = bouton_jouer.get_rect()
ecran.blit(boutongame,(700, 400))

"""
bouton_jouer = pg.image.load("images/boutonjouer.png")
boutongame= bouton_jouer.convert()
bouton_rect = bouton_jouer.get_rect()
ecran.blit(boutongame,(0, 0))
"""

titre = pg.image.load("jule/logo.png")
titreimage = titre.convert_alpha()
ecran.blit(titreimage, (200,0))

pg.display.flip()



pg.mixer.music.load("jule/musique.mp3")
pg.mixer.music.play()
pg.mixer.music.set_volume(0.1)



while fenetre_en_cours:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fenetre_en_cours = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                jeu_en_cours = False


        if pg.mouse.get_focused():

            x, y = pg.mouse.get_pos()

            pressed = pg.mouse.get_pressed()
            if pressed[0] and (x>=700 and x <= 825) and (y>=400 and y <= 525) :
                fenetre_en_cours = False #A changer, il faut ouvrir le main.py du mode libre ici
                jeux = Jeux()
                jeux.run()


    pg.display.update()

    horloge_fps.tick(fps)


pg.quit()


