import pygame
import globals as g

class name(pygame.sprite.Sprite):
    def __init__(self, cx, cy, img, size):
        super().__init__()
        # Set up
        self.image = pygame.image.load(f"assets/graphics/{img}")
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.centerx = cx
        self.rect.centery = cy
        
        # Object's variables
    
    def update(self):
        self.is_clicked()

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]
        if clicked and self.rect.collidepoint(mouse):
            pass
        