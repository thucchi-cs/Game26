import pygame
import globals as g

class Background(pygame.sprite.Sprite):
    def __init__(self, img, coor=(0,0)):
        super().__init__()
        # Set up
        self.image = pygame.image.load(f"assets/graphics/background/{img}")
        self.rect = self.image.get_rect()
        self.rect.topleft = coor
        
        # Object's variables
    
    def update(self):
        pass
        