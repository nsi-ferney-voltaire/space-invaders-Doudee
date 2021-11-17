import pygame  # necessaire pour charger les images et les sons
import random


class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.image = pygame.image.load("vaisseau.png")
        self.position = 400
        self.direction = 0
    
    def setDirection(self, direction : str):
        if direction == "gauche":
            self.direction = "gauche"
        if direction == "droite":
            self.direction = "droite"
        
        
    def getPosition(self):
        return self.position        
    
    def deplacer(self):
        if self.direction == "gauche":
            self.position -= 7
        if self.direction == "droite":
            self.position += 7
        self.position = min(max(self.position,0),737)
        
    
    def tirer(self):
        self.direction = 0
        
        



class Balle():
    def __init__(self, joueur):
        self.tireur = joueur
        self.depart = joueur.position
        self.hauteur = 500
        self.image = pygame.image.load("balle.png")
        self.etat = "chargee"
        
    def bouger(self):
        if self.etat == "tiree":
            self.hauteur -= 15
            if self.hauteur < 0:
                self.depart = self.tireur.position
                self.hauteur = 500
                self.etat = "chargee"
        if self.etat == "chargee":
            self.depart = self.tireur.position
            
    def toucher(self,ennemis):
        if self.hauteur == ennemis.hauteur and self.depart == ennemis.depart:
            return True
        return None
            
class ennemis():
    
    nbEnnemis = random.randint(2,10)
    
    def __init__(self):        
            self.depart = random.randint(0,800)
            self.type = random.randint(1,2)
            self.hauteur = 0
            self.image = pygame.image.load(f"invader{self.type}.png")
            self.vitesse = self.type * 1.25
        self.hitbox = self.hauteur
            
    def avancer(self):
        self.hauteur += self.vitesse
        
    
        
            
    
            
            
            

        
         
        