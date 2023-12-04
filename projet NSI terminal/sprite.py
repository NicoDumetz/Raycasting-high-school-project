import pygame as pg
from parametre import *
import os
from collections import deque

class Sprite_objet:
    def __init__(self, jeux, chemin="sprites/objet/JBfin.png", pos=(4,23), scale=0.7 ,shift=0.27):
        self.jeux = jeux
        self.player = jeux.player
        self.x, self.y = pos
        self.image = pg.image.load(chemin).convert_alpha()
        self.image_width = self.image.get_width() #
        self.image_half_width = self.image.get_width() // 2
        self.image_ratio = self.image_width / self.image.get_height() #hauteur
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0,0,0,0,1,1
        self.sprite_half_width = 0
        self.scale = scale
        self.height_shift = shift

    def get_sprite_projection(self):
        proj = screen_dist / self.norm_dist * self.scale
        proj_width = proj*self.image_ratio
        proj_height = proj

        image = pg.transform.scale(self.image, (int(proj_width), int(proj_height)))

        self.sprite_half_width = proj//2
        height_shift = proj_height* self.height_shift
        pos= self.screen_x - self.sprite_half_width, half_height - proj_height // 2 +height_shift

        self.jeux.raycastring.objet_rendu.append((self.norm_dist, image, pos))

    def get_sprite(self):
        dx = self.x - self.player.x # on cherche l'angle theta grâce a atan
        dy = self.y - self.player.y
        self.dx, self.dy = dx,dy
        self.theta = math.atan2(dy,dx) # maitenant que nous savons l'angle, on cherche difference entre angle delta et angle joueur

        delta = self.theta - self.player.angle
        if (dx >0 and self.player.angle > math.pi ) or (dx<0 and dy <0):
            delta +=math.tau #rajoute 2pi dans delta

        delta_ray = delta / delta_angle #nombre de rayon dans delta
        self.screen_x = (half_num_ray + delta_ray)*scale # on sait ou se situe sur l'ecran, milieu + difference fois echelle
        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.image_half_width < self.screen_x < (width + self.image_half_width) and self.norm_dist > 0.5: #collision eviter bug si sup a taille ecran
            self.get_sprite_projection()


    def update(self):
        self.get_sprite()

class Sprite_anime(Sprite_objet):
    def __init__(self,jeux,chemin='sprites/anime/lampe_rouge/0.png',pos=(2,20), scale=0.8,shift=0.15, animation_time=120):
        super().__init__(jeux,chemin,pos,scale,shift)
        self.animation=animation_time
        self.chemin = chemin.rsplit("/",1)[0] #accés aux dossiers
        self.images = self.get_images(self.chemin)
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_declanche = False
    def update(self):
        super().update()
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images):
        if self.animation_declanche:
            images.rotate(-1)
            self.image = images[0]

    def check_animation_time(self):
        self.animation_declanche = False
        temps_act = pg.time.get_ticks()
        if temps_act - self.animation_time_prev > self.animation:
            self.animation_time_prev= temps_act
            self.animation_declanche = True

    def get_images(self,chemin):
        images = deque() #stock image
        for file_name in os.listdir(chemin):
            if os.path.isfile(os.path.join(chemin,file_name)):
                img = pg.image.load(chemin + "/" + file_name).convert_alpha()
                images.append(img)
        return images














