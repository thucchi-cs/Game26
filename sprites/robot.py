import pygame
import time
import globals as g

class Robot(pygame.sprite.Sprite):
    def __init__(self, cx, cy, img, currentG:pygame.sprite.Group, newG:pygame.sprite.Group, size=None):
        super().__init__()
        # Set up
        self.image = pygame.image.load(f"assets/graphics/{img}")
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.centerx = cx
        self.rect.centery = cy
        
        # Object's variables
        self.room = currentG
        self.screen = newG
    
    def update(self):
        self.is_clicked()

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]
        if clicked and self.rect.collidepoint(mouse):
            self.close_up()
        
    def close_up(self):
        g.on_screen.remove(self.room)
        g.on_screen.add(self.screen)
        time.sleep(0.15)