import pygame
import time
import globals as g

class Robot(pygame.sprite.Sprite):
    def __init__(self, cx, cy, newcx, newcy, img, currentG:pygame.sprite.Group, newG:pygame.sprite.Group, size=1, newsize=1):
        super().__init__()
        # Set up
        self.img = img
        self.image = pygame.image.load(f"assets/graphics/{img}")
        self.size = size
        self.pos = (cx, cy)
        self.image = pygame.transform.scale_by(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.centerx = cx
        self.rect.centery = cy
        
        # Object's variables
        self.room = currentG
        self.screen = newG
        self.n_size = newsize
        self.n_pos = (newcx, newcy)
        self.current = 0
    
    def update(self):
        self.is_clicked()
        if g.on_screen.has(self.screen) and self.current == 0:
            self.current = 1
            self.image = pygame.image.load(f"assets/graphics/{self.img}")
            self.image = pygame.transform.scale_by(self.image, self.n_size)
            self.rect = self.image.get_rect()
            self.rect.center = self.n_pos

        elif g.on_screen.has(self.room) and self.current == 1:
            self.current = 0
            self.image = pygame.image.load(f"assets/graphics/{self.img}")
            self.image = pygame.transform.scale_by(self.image, self.size)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]
        if clicked and self.rect.collidepoint(mouse):
            self.close_up()
        
    def close_up(self):
        g.load_screen(self.room, self.screen)
        time.sleep(0.15)