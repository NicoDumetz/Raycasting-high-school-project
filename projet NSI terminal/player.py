from parametre import *
from map import *
import pygame as pg
import math
import sys
from time import sleep
import son
from sprite import *
class Player:
    def __init__(self, jeux):
        self.jeux = jeux
        self.x, self.y = player_pos
        self.angle= player_angle
        self.rel=1
        self.munition=30
        self.munition_font = pg.font.SysFont('Verdana',50)
        self.energie=energie_max
        self.vie=vie_max
        self.vie_vector=pg.font.SysFont('Verdana',20)
        self.energie_vector=pg.font.SysFont('Verdana',20)
        self.key=0

    def draw(self): # methode quisert que pour la 2D
        #pg.draw.line(self.jeux.screen,jaune, (int(self.x*100), int(self.y*100)), (self.x*100 + width * math.cos(self.angle), self.y*100 + width * math.sin(self.angle)),2) # faire apparaitre coeficient directeur
        #pg.draw.circle(self.jeux.screen,vert,(int(self.x*100), int(self.y*100)), 15) # fais apparaitre le joeuur
        self.jeux.screen.blit(self.munition_font.render(str(self.munition)+"/30",True, (255, 255, 255)), (1400,800))
        self.jeux.screen.blit(self.vie_vector.render("Health:",True, (255, 255, 255)), (10,760))
        self.jeux.screen.blit(self.energie_vector.render("Energie:",True, (255, 255, 255)), (10,800))
        self.vie_bar()
        self.energie_bar()
    def souris_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < souris_bordure_gauche or mx > souris_bordure_droite:
            pg.mouse.set_pos([half_width, half_height])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-souris_max, min(souris_max, self.rel))
        self.angle += self.rel*souris_sensibilité*self.jeux.delta


    def update(self):
        self.movement()
        self.souris_control()
        self.munition_ay()
        self.porte()
        ##print(int(self.x),int(self.y))
    def movement(self):
        nsin = math.sin(self.angle)
        ncos = math.cos(self.angle)
        dx=0
        dy=0
        speed= player_speed* self.jeux.delta # vitesse * le temps que la touche est presser
        keys= pg.key.get_pressed()
        speed_sin= speed * nsin
        speed_cos= speed * ncos
        marche_cos = 10/16*(speed_cos)
        marche_sin = 10/16*(speed_sin)

        if self.energie>1:
            if keys[pg.K_w] and keys[pg.K_LSHIFT] :   # selon la touche presser on ajoute ou enleve a x y du joueur selon la postion du coefficient directeur
                dx+= speed_cos
                dy+= speed_sin
                self.energie-=1
            if keys[pg.K_s] and keys[pg.K_LSHIFT]:
                dx+= -speed_cos
                dy+= -speed_sin
                self.energie-=1
            if keys[pg.K_d] and keys[pg.K_LSHIFT]:
                dx+= -speed_sin
                dy+= speed_cos
                self.energie-=1
            if keys[pg.K_a] and keys[pg.K_LSHIFT]:
                dx+= speed_sin
                dy+= -speed_cos
                self.energie-=1
        if self.energie < energie_max:
            self.energie+=0.5



        if keys[pg.K_w] and not keys[pg.K_LSHIFT]:   # selon la touche presser on ajoute ou enleve a x y du joueur selon la postion du coefficient directeur
            dx+=  marche_cos
            dy+= marche_sin
        if keys[pg.K_s] and not keys[pg.K_LSHIFT]:   # selon la touche presser on ajoute ou enleve a x y du joueur selon la postion du coefficient directeur
            dx+=  -marche_cos
            dy+= -marche_sin
        if keys[pg.K_d] and not keys[pg.K_LSHIFT]:   # selon la touche presser on ajoute ou enleve a x y du joueur selon la postion du coefficient directeur
            dx+=-marche_sin
            dy+=  marche_cos
        if keys[pg.K_a] and not keys[pg.K_LSHIFT]:   # selon la touche presser on ajoute ou enleve a x y du joueur selon la postion du coefficient directeur
            dx+= marche_sin
            dy+=  -marche_cos


        self.wall_colision(dx,dy) # check si y a un mur avant d'ajouter les nouvelles coordonnées

##        if keys[pg.K_LEFT]: # pour l'instant avec les fléches objectif bouger avec la souris
##            self.angle -= player_rot_speed * self.jeux.delta # le cercle trigo
##        if keys[pg.K_RIGHT]:
##            self.angle += player_rot_speed * self.jeux.delta
        self.angle = self.angle% math.tau # tau = 2pi (cercle trigo)
    def check_wall(self,x,y):
        return (x,y) not in self.jeux.map.world_map # si pas dans le dico des pos mur

    def wall_colision(self, dx, dy):
        scale = taille_player/ self.jeux.delta
        if self.check_wall(int(self.x +dx*scale), int(self.y)): #si false on avance
            self.x+= dx
        if self.check_wall(int(self.x), int(self.y+dy*scale)):
            self.y+= dy

    def munition_ay(self):
        keys= pg.key.get_pressed()
        for event in pg.event.get():
            if keys[pg.K_r] or self.munition==0:
                self.munition=30


    def porte(self):
        if int(self.x)==18 and int(self.y)==25 and self.key<1:
            self.key+=1
            self.jeux.gestion_sprite.sprite_liste.pop()
        if int(self.x)==27 and int(self.y)==30 and self.key<2:
            self.key+=1
            self.jeux.gestion_sprite.sprite_liste.pop()


        if self.key>=1:
            self.jeux.screen.blit(pg.image.load("sprites/anime/0.png").convert_alpha(),(10,850))
            if self.key >= 2:
                self.jeux.screen.blit(pg.image.load("sprites/anime/cle ble/0.png").convert_alpha(),(40,850))

        if mini_map[int(self.y)][int(self.x)+1] ==2.5 and self.key >=1:
            mini_map[int(self.y)][int(self.x)+1] = False
            self.jeux.map = Map(self)


        if mini_map[int(self.y)][int(self.x)+1] ==2.6 and self.key >=2:
            mini_map[int(self.y)][int(self.x)+1] = False
            self.jeux.map = Map(self)


        if mini_map[int(self.y)][int(self.x)+1] == 2.4:
            mini_map[int(self.y)][int(self.x)+1] = False
            self.jeux.map = Map(self)



    def energie_bar(self):
        bar_color=(255, 195, 0)
        back_bar_color=(255,5,1)
        bar_position=[100,800,self.energie,30]
        back_bar_position=[100,800,energie_max,30]
        pg.draw.rect(self.jeux.screen,back_bar_color,back_bar_position) #affiche la barre arrière
        pg.draw.rect(self.jeux.screen,bar_color,bar_position) #affiche la barre avant

    def vie_bar(self):
        vie_bar_color=(71, 197, 38)
        vie_back_bar_color=(255,5,1)
        vie_bar_position=[100,750,self.vie,30]
        vie_back_bar_position=[100,750,vie_max,30]
        pg.draw.rect(self.jeux.screen,   vie_back_bar_color,   vie_back_bar_position) #affiche la barre arrière
        pg.draw.rect(self.jeux.screen,  vie_bar_color,   vie_bar_position) #affiche la barre avant

    def pos(self):
        return self.x, self.y
    def map_pos(self):
        return int(self.x),int(self.y)