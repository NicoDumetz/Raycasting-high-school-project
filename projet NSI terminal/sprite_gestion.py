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
        ajouter_sprite(Sprite_objet(jeux))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/Neocle.png', (42,38)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/Neocle.png', (42,8)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/grosseputefin.png',(42,37)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/grosseputefin.png',(42,7)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/ethancrampter.png', (7,22)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/Matissecle.png', (24,38)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/Matissecle.png', (24,8)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/ninho.png',(15,25)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/nicofin.png',(55,22)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/dorianfin.png',(46,38)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/dorianfin.png',(46,8)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/groszizifin.png',(46,7)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/groszizifin.png',(46,37)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/sorrenfin.png',(28,38)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/sorrenfin.png',(28,8)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/neelfin.png',(28,37)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/neelfin.png',(28,7)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/marauderfin.png',(28,31)))


        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/baptistefin.png',(17,23)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/caillouxfin.png',(7,23)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/taznim.png',(3,22)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/evlyafin.png',(28,27)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/indienfin.png',(16,26)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/mathieufin.png',(27,33)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/jule.png',(2,18)))



        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/haalandfin.png',(53,20)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(53,21)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(53,22)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(53,23)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(53,24)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/haalandfin.png',(53,25)))

        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/panpanfin.png',(54,20)))
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
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/tomramofin.png',(57,23)))
        ajouter_sprite(Sprite_objet(jeux,'sprites/objet/test.png',(57,24)))




        #anime
        ajouter_sprite(Sprite_anime(jeux,'sprites/anime/nico/0.png',(54,24)))
        ajouter_sprite(Sprite_anime(jeux,'sprites/anime/aymen/0.png',(57,25)))
        ajouter_sprite(Sprite_anime(jeux,'sprites/anime/cle ble/0.png', (27,30)))
        ajouter_sprite(Sprite_anime(jeux,'sprites/anime/cle/0.png', (18,25))) #clé 1






    def update(self):
        [sprite.update() for sprite in self.sprite_liste]

    def ajouter_sprite(self, sprite):
        self.sprite_liste.append(sprite)