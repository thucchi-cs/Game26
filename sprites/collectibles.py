import time
import pygame
import globals as g

class Collectible(pygame.sprite.Sprite):
    def __init__(self, cx, cy, img, open_type, size=None, rot=0):
        super().__init__()
        # Set up
        self.img = img
        self.pos = (cx, cy)
        self.size = size
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

        if open_type == "open":
            self.open = open
    
    def update(self):
        self.is_clicked()

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]
        if clicked:
            # print("Click")
            if self.collected:
                print("o")
                if not self.rect.collidepoint(mouse):
                    self.collect()
                    print("collect2")
                else:
                    self.pop_up()
                    print("pop")
            else:
                if self.rect.collidepoint(mouse):
                    self.collect()
                    print("collect1") 
    
    def collect(self):
        self.image = pygame.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect()
        self.rect.center = Collectible.calc_pos()
        self.rect.centerx += g.bp_rect.x
        self.rect.centery += g.bp_rect.y
        self.collected = True
        self.remove(g.on_screen)
        self.add(g.backpack)
        time.sleep(0.15)
    
    def calc_pos():
        total = g.backpack.__len__() -1
        x = g.bp_rect.width*(0.2 * (total%5)) + (g.bp_rect.width *0.1)
        y = g.bp_rect.height*(0.5 * (total//5)) + (g.bp_rect.height * 0.25)
        return (x,y)
        
    def pop_up(self):
        self.image = pygame.image.load(f"assets/graphics/{self.img}")
        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)
        self.image = pygame.transform.rotate(self.image, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.remove(g.backpack)
        self.add(g.on_screen)
        time.sleep(0.15)