import pygame
import globals as g

class Collectible(pygame.sprite.Sprite):
    def __init__(self, cx, cy, img, size):
        super().__init__()
        # Set up
        self.image = pygame.image.load(f"assets/graphics/{img}")
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.centerx = cx
        self.rect.centery = cy
        
        # Object's variables
        self.name = "KeyTest"
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
        self.rect.centerx += g.backpack.x
        self.rect.centery += g.backpack.y
        self.collected = True
        self.remove(g.on_screen)
        self.add(g.collected)
    
    def calc_pos():
        total = g.collected.__len__()
        x = g.backpack.width*(0.2 * (total%5)) + (g.backpack.width *0.1)
        y = g.backpack.height*(0.5 * (total//5)) + (g.backpack.height * 0.25)
        return (x,y)
        