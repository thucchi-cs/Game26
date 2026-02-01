import pygame
import globals as g

class Background(pygame.sprite.Sprite):
    def __init__(self, img, coor=(0,0), size=None):
        super().__init__()
        # Set up
        self.image = pygame.image.load(f"assets/graphics/background/{img}")
        if size:
            self. image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.topleft = coor
        
        # Object's variables
    
    def update(self):
        pass
        