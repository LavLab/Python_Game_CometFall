import pygame

# Classe Monstre
class cls_Monstre(pygame.sprite.Sprite):
    
    def __init__(self, Jeu):
        super().__init__()
        self.Jeu = Jeu
        self.vie = 50
        self.max_vie = 100
        self.puissance = 5
        self.vitesse = 2
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1080
        self.rect.y = 550
        
    def bar_vie(self, Ecran):
        # Bar de vie total
        bar_couleur = (111, 210, 46)
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_vie, 5]
        pygame.draw.rect(Ecran, bar_couleur, bar_position)
        
        # Bar de vie actuel
        bar_couleur = (111, 210, 46)
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.vie, 5]
        pygame.draw.rect(Ecran, bar_couleur, bar_position)
        
        
    def deplacement(self):
        if not self.Jeu.verifier_colision(self, self.Jeu.les_joueurs):
            self.rect.x -= self.vitesse