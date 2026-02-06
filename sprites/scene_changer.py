import pygame
import time
import globals as g

class Scene_changer(pygame.sprite.Sprite):
    def __init__(self, cx, cy, img, currentG:pygame.sprite.Group, newG:pygame.sprite.Group, size=None, rot=0):
        super().__init__()
        # Set up
        self.image = pygame.image.load(f"assets/graphics/{img}")
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.image = pygame.transform.rotate(self.image, rot)
        self.rect = self.image.get_rect()
        self.rect.centerx = cx
        self.rect.centery = cy
        
        # Object's variables
        self.current = currentG
        self.new = newG
    
    def update(self):
        self.is_clicked()

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]
        if clicked and self.rect.collidepoint(mouse):
            g.load_screen(self.current, self.new)
            time.sleep(0.15)
