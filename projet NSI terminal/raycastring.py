import pygame as pg
import math
from parametre import *
from map import *


class Raycastring:
    def __init__(self, jeux):
        self.jeux = jeux
        self.ray_casting_result= []
        self.objet_rendu= []
        self.textures =  self.jeux.objetrender.wall_texture

    def get_objet(self):
        self.objet_rendu=[]
        for ray, values in enumerate(self.ray_casting_result): #tout les rayons avec pos text ect
            long, proj_height, texture, offset = values


            if proj_height < height: # limite collision pour eviter bug
                wall_collone = self.textures[texture].subsurface(offset*(taille_texture-scale),0,scale,taille_texture)
                wall_collone = pg.transform.scale(wall_collone, (scale, int(proj_height)))
                wall_pos= (ray*scale, half_height-proj_height//2)
            else:
                texture_height= taille_texture*height/proj_height
                wall_collone= self.textures[texture].subsurface(offset*(taille_texture-scale),milieu_texture-texture_height//2,scale,texture_height)
                wall_collone= pg.transform.scale(wall_collone, (scale, height))
                wall_pos=(ray*scale, 0)


            self.objet_rendu.append((long, wall_collone, wall_pos))

    def ray_cast(self):
        self.ray_casting_result=[]
        ox, oy= self.jeux.player.pos() # coor du joueur
        x_map, y_map= self.jeux.player.map_pos() # quadrillage carte

        ray_angle = self.jeux.player.angle  - half_fov + 0.0001 # premier rayon, angle - fov //2 - distance entre rayon ( 0.0001)

        for ray in range(num_ray): #boucle pour calculer angle de chaque rayon
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)
            #vertical
            if cos_a > 0: # si superieur a 0 intersection a droite
                x_vert, dx = (x_map + 1, 1)
            else: # sinon a gauche
                x_vert, dx = (x_map - 1e-6, -1)

            long_vert = (x_vert - ox) /cos_a # longueur = ( coor tuile - coor joueur) / cos :formule donnée
            y_vert = oy + long_vert * sin_a # premiere intersection

            delta_long = dx / cos_a # avoir longueur de la prochaine intersection, formule donnée
            dy = delta_long * sin_a


            for i in range(max_long): # maximum longueur donc 20
                tuile_vert = int(x_vert), int(y_vert) #coor tuile
                if tuile_vert in self.jeux.map.world_map: # si dans la map alors on casse car il ya un mur
                    texture_vert = self.jeux.map.world_map[tuile_vert]
                    break
                x_vert += dx
                y_vert += dy
                long_vert += delta_long

            #horizontale même principe
            if sin_a > 0: # si sinus superieur alors segment en haut
                y_hor, dy = (y_map + 1, 1)
            else: #sinon en bas
                y_hor, dy = (y_map - 1e-6, -1) # puissance -6


            long_hor = (y_hor - oy) /sin_a # longueur = ( coor tuile - coor joueur) / cos
            x_hor = ox + long_hor * cos_a # donc la premiere intersection


            delta_long = dy / sin_a # donc longueur prochaine intersection
            dx = delta_long * cos_a
            for i in range(max_long):
                tuile_hor = int(x_hor), int(y_hor) # coor tuile
                if tuile_hor in self.jeux.map.world_map:
                    texture_hor = self.jeux.map.world_map[tuile_hor]
                    break
                x_hor += dx
                y_hor += dy
                long_hor += delta_long

            # on prend la plus petite long pour verifier, et texture mur
            if long_vert < long_hor:
                long= long_vert
                texture = texture_vert
                y_vert %=1
                if cos_a >0:
                    offset = y_vert
                else:
                    offset = (1 - y_vert)
            else:
                long = long_hor
                texture= texture_hor
                x_hor %= 1
                if sin_a > 0:
                    offset = (1-x_hor)
                else:
                    offset= x_hor


            #projection
            proj_height = screen_dist / (long +0.0001)
            #mur

            #resultat
            self.ray_casting_result.append((long, proj_height, texture, offset))

            #pg.draw.rect(self.jeux.screen, blanc, (ray*scale, half_height - proj_height //2,scale,proj_height)) # rect 1= placez en fonction du rayon, 2= centre de l'écran, 3= largeur, 4= hauteur




            ray_angle += delta_angle # change de rayon


    def update(self):
        self.ray_cast()
        self.get_objet()