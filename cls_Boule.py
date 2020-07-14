import pygame

# Classe Boule
class cls_Boule(pygame.sprite.Sprite):
    
    def __init__(self,Joueur):
        super().__init__()
        self.vitesse = 5
        self.Joueur = Joueur
        self.image = pygame.image.load('assets\projectile.png')
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = Joueur.rect.x + 80
        self.rect.y = Joueur.rect.y + 65
        self.origin_image = self.image
        self.angle = 0
        
    def rotation(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        
    def suppression(self):
        self.Joueur.les_boules.remove(self)
    
    def deplacement(self):
        self.rect.x += self.vitesse
        self.rotation()
        
        if self.Joueur.Jeu.verifier_colision(self, self.Joueur.Jeu.les_monstres):
            self.suppression()
        
        
        if self.rect.x > 1080:
            self.suppression()