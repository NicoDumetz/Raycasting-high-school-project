import pygame as pg
import sys
from parametre import *
from map import *
from player import *
from raycastring import *
from objetrender import *
from sprite import *
from sprite_gestion import *


class Jeux:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(res)
        self.clock = pg.time.Clock() #fps
        self.new_game() # map
        self.delta= 1

    def new_game(self):
        self.map = Map(self) # importe la map
        self.player = Player(self) # importe le joueur
        self.objetrender = Objetrendu(self)
        self.raycastring = Raycastring(self)
        self.gestion_sprite = Gestion_sprite(self)



    def update(self):
        self.raycastring.update()
        self.player.update()
        self.gestion_sprite.update()
        pg.display.flip()
        self.delta= self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() : .1f}') # affiche les fps comme nom de fenetre


    def draw(self):
        #self.screen.fill(black)
        self.objetrender.draw()
        #self.map.draw() # dessine la map en 2d
        self.player.draw() # dessine le perso 2d
        #self.screen.blit(cursor,(half_width,half_height))

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                print("caca")
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()



    def run(self):
        while True:
            self.check_events()
            self.draw()
            self.update()



if __name__ == '__main__': # si ce code est exécuté en tant que script principal (appelé directement avec Python et pas importé), alors exécuter cette fonction.
    game = Jeux()
    game.run()

