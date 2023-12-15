from sprite import *


class Gestion_sprite:
    def __init__(self,jeux):
        self.jeux = jeux
        self.sprite_liste = []
        self.objet_sprite_chemin = "sprites/objet/"
        self.anime_sprite_chemin = 'sprites/anime/'
        ajouter_sprite = self.ajouter_sprite

        #tout les sprites INCROYABLE
        #objet
        ##ajouter_sprite(Sprite_objet(jeux,'sprites/objet/nicofin.png',(55,22)))
        
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(53,21)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(53,22)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(53,23)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(53,24)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(54,22)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(54,21)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(54,23)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(54,25)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(55,20)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(55,21)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(55,23)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(55,24)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(55,25)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(56,20)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(56,21)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(56,22)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(56,23)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(56,24)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(56,25)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(57,20)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(57,21)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(57,22)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(57,24)))




        #anime
        ajouter_sprite(Sprite_anime(jeux,'sprites/anime/nico/0.png',(54,24)))
        ajouter_sprite(Sprite_anime(jeux,'sprites/anime/cle ble/0.png', (27,30)))
        ajouter_sprite(Sprite_anime(jeux,'sprites/anime/cle/0.png', (18,25))) #clé 1






    def update(self):
        [sprite.update() for sprite in self.sprite_liste]

    def ajouter_sprite(self, sprite):
        self.sprite_liste.append(sprite)