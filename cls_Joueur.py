import pygame
from cls_Boule import cls_Boule

# Classe cls_Joueur
class cls_Joueur(pygame.sprite.Sprite): 
    
    def __init__(self,Jeu):
        super().__init__()
        self.Jeu = Jeu
        self.vie = 100
        self.max_vie = 100
        self.puissance = 10
        self.vitesse = 5
        self.les_boules = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 25
        self.rect.y = 500
        
    def Lancer_Boule(self):
        self.les_boules.add(cls_Boule(self))
        
    def deplacement_droite(self):
        if not self.Jeu.verifier_colision(self,self.Jeu.les_monstres):
            self.rect.x += self.vitesse
        
    def deplacement_gauche(self):
        self.rect.x -= self.vitesse