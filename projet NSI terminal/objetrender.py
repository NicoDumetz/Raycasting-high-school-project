import pygame as pg
from parametre import *

class Objetrendu:
    def __init__(self, jeux):
        self.jeux = jeux
        self.screen = jeux.screen
        self.wall_texture = self.load_wall()
        self.nuages = self.get_texture("textures/nuages.jpg", (width, half_height))
        self.nuages_offset= 0


    def draw(self):
        self.background()
        self.rendu_jeux()

    def background(self):
        self.nuages_offset = (self.nuages_offset + 4.5 * self.jeux.player.rel) % width
        self.screen.blit(self.nuages, (-self.nuages_offset, 0))
        self.screen.blit(self.nuages, (-self.nuages_offset + width, 0))
        pg.draw.rect(self.screen, sol_couleur, (0,half_height, width,height) )


    def rendu_jeux(self): #affiche mur avec image a la pos
        liste_objet = sorted(self.jeux.raycastring.objet_rendu, key=lambda t: t[0], reverse=True)
        for long, image,pos in liste_objet:
            self.screen.blit(image, pos)


    @staticmethod
    def get_texture(chemin, res=(taille_texture, taille_texture)):
        texture = pg.image.load(chemin).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall(self):
        return {
    #placeholder
        1.0: self.get_texture("textures/placeholder/0.jpeg"),
    #mur dehor
    #herbe
        2.0: self.get_texture("textures/exterieur/20.png"),
        2.1: self.get_texture("textures/exterieur/21.png"),
    #brique
        2.2: self.get_texture("textures/exterieur/22.png"),
        2.3: self.get_texture("textures/exterieur/23.png"),
    #porte
        2.4: self.get_texture("textures/exterieur/24.png"),
        2.5: self.get_texture("textures/exterieur/25.png"),
        2.6: self.get_texture("textures/exterieur/26.png"),
    #labo gris
        3.0: self.get_texture("textures/labo gris/30.png"),
        3.1: self.get_texture("textures/labo gris/31.png"),
        3.2: self.get_texture("textures/labo gris/32.png"),
        3.3: self.get_texture("textures/labo gris/33.png"),
        3.4: self.get_texture("textures/labo gris/34.png"),
        3.5: self.get_texture("textures/labo gris/35.png"),
        3.6: self.get_texture("textures/labo gris/36.png"),
        3.7: self.get_texture("textures/labo gris/37.png"),
        3.8: self.get_texture("textures/labo gris/38.png"),
        3.9: self.get_texture("textures/labo gris/39.png"),
    #labo bleu jaune
        4.0: self.get_texture("textures/labo bleu jaune/40.png"),
        4.1: self.get_texture("textures/labo bleu jaune/41.png"),
        4.2: self.get_texture("textures/labo bleu jaune/42.png"),
        4.3: self.get_texture("textures/labo bleu jaune/43.png"),
        4.4: self.get_texture("textures/labo bleu jaune/44.png"),
        4.5: self.get_texture("textures/labo bleu jaune/45.png"),
        4.6: self.get_texture("textures/labo bleu jaune/46.png"),
        4.7: self.get_texture("textures/labo bleu jaune/47.png"),
        4.8: self.get_texture("textures/labo bleu jaune/48.png"),

    #labo bleu
        5.0: self.get_texture("textures/labo bleu/50.png"),
        5.1: self.get_texture("textures/labo bleu/51.png"),
        5.2: self.get_texture("textures/labo bleu/52.png"),
        5.3: self.get_texture("textures/labo bleu/53.png"),
        5.4: self.get_texture("textures/labo bleu/54.png"),
        5.5: self.get_texture("textures/labo bleu/55.png"),
        5.6: self.get_texture("textures/labo bleu/56.png"),
        5.7: self.get_texture("textures/labo bleu/57.png"),
        5.8: self.get_texture("textures/labo bleu/58.png"),
        5.9: self.get_texture("textures/labo bleu/59.png"),
        6.0: self.get_texture("textures/labo bleu/60.png"),

    }