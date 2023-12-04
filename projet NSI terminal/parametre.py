# toutes les variables
import math
import pygame as pg
res = width, height = 1600,900
FPS = 60
half_width= width // 2 #moitié
half_height= height // 2

blanc=(255,255,255)
black = (0,0,0)
darkgray = (64,64,64)
jaune = (255,255,0)
vert= (0,255,0)

player_pos= 2,24 # de la minimap (quadrillage) ou 1 représente 100 px
player_angle= 1440
player_speed= 0.004
player_rot_speed = 0.002
taille_player=60

souris_sensibilité = 0.0003
souris_max = 40
souris_bordure_gauche= 100
souris_bordure_droite= width-souris_bordure_gauche


# formule donnée
fov= math.pi / 2  # 60 degrées
half_fov = fov / 2 #milieu du fov
num_ray = width // 2  # nombre de rayon
half_num_ray = num_ray // 2 # milieu des rayons
delta_angle = fov/num_ray # chaque rayon l'angle augmente de delta
max_long = 50
screen_dist = half_width / math.tan(half_fov)
scale = width // num_ray # résolution de l'écran est superieur au nombre de rayon

# image texture
taille_texture= 256
milieu_texture= taille_texture //2





sol_couleur= (30,30,30)

# perso
energie_max= 300
vie_max = 300



