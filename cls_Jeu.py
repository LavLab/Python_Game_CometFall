import pygame
from cls_Joueur import cls_Joueur
from cls_Monstre import cls_Monstre

# Classe Jeu
class cls_Jeu:  
    def __init__(self):
        super().__init__()
        
        # Generer Joueurs
        self.Joueur = cls_Joueur(self)
        self.les_joueurs = pygame.sprite.Group()
        self.les_joueurs.add(self.Joueur)
        
        # Generer Monstres
        self.les_monstres = pygame.sprite.Group()
        self.apparition_monstre()
        
        # Gestion des touches
        self.Touches = {}
        
    def verifier_colision(self, sprite, group):
        return pygame.sprite.pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        
    def apparition_monstre(self):
        Monstre = cls_Monstre(self)
        self.les_monstres.add(Monstre)