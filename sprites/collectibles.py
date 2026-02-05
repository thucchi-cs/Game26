import pygame
import globals as g

class Collectible(pygame.sprite.Sprite):
    def __init__(self, cx, cy, img, size=None, rot=0):
        super().__init__()
        # Set up
        self.image = pygame.image.load(f"assets/graphics/{img}")
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rot = rot
        self.image = pygame.transform.rotate(self.image, rot)
        self.rect = self.image.get_rect()
        self.rect.centerx = cx
        self.rect.centery = cy
        
        # Object's variables
        self.name = None
        self.collected = False
    
    def update(self):
        self.is_clicked()

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]
        if not self.collected and clicked and self.rect.collidepoint(mouse):
            self.collect()
    
    def collect(self):
        self.image = pygame.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect()
        self.rect.center = Collectible.calc_pos()
        self.rect.centerx += g.bp_rect.x
        self.rect.centery += g.bp_rect.y
        self.collected = True
        self.remove(g.on_screen)
        self.add(g.backpack)
    
    def calc_pos():
        total = g.backpack.__len__() -1
        x = g.bp_rect.width*(0.2 * (total%5)) + (g.bp_rect.width *0.1)
        y = g.bp_rect.height*(0.5 * (total//5)) + (g.bp_rect.height * 0.25)
        return (x,y)
        