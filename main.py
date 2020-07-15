import pygame

from cls_Jeu import cls_Jeu
from cls_Joueur import cls_Joueur
from cls_Boule import cls_Boule

# Initialisation pygame
pygame.init()

# Titre de la fenetre
pygame.display.set_caption("LavLab's Game - Comet Fall")

# Definition de l'ecran
Ecran = pygame.display.set_mode((1080,720))

# Charger JEU
Jeu = cls_Jeu()

# Running
running = True

while running:
 
    # Chargement BACKGROUND
    background = pygame.image.load('assets/bg.jpg')
    
    # Positionnement des images
    Ecran.blit(background,(0,-200))
    Ecran.blit(Jeu.Joueur.image,(Jeu.Joueur.rect))
    
    # Application des images
    Jeu.Joueur.les_boules.draw(Ecran)
    Jeu.les_monstres.draw(Ecran)
    
    #  Déplacement des MONSTRES
    for monstre in Jeu.les_monstres:
        monstre.deplacement()
        monstre.bar_vie(Ecran)
        
    # Déplacement des BOULES
    for boule in Jeu.Joueur.les_boules:
        boule.deplacement()
    
    # MAJ de l'ecran
    pygame.display.flip()
    
    # Déplacement DROITE
    if Jeu.Touches.get(pygame.K_RIGHT) and Jeu.Joueur.rect.x + Jeu.Joueur.rect.width < Ecran.get_width():
        Jeu.Joueur.deplacement_droite()
        
    # Déplacement GAUCHE
    if Jeu.Touches.get(pygame.K_LEFT) and Jeu.Joueur.rect.x > 0:
        Jeu.Joueur.deplacement_gauche()
        
    
    # Evenement de la fenetre
    for event in pygame.event.get():
            
        # Touche pressé
        if event.type == pygame.KEYDOWN:
            Jeu.Touches[event.key] = True            
            
            # Touche espace pressé
            if Jeu.Touches.get(pygame.K_SPACE):
                Jeu.Joueur.Lancer_Boule()
        
        # Touche laché   
        if event.type == pygame.KEYUP:
            Jeu.Touches[event.key] = False
                
        # Fin de session
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()