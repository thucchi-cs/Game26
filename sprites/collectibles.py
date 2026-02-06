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
        self.counter = 0
        self.bounce_dir = 1

        self.open = open_type
        self.following = False
    
    def update(self):
        self.is_clicked()
        if self.following:
            self.follow()
        if self.open == "give" and not g.backpack.has(self):
            self.bouce()

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]
        if clicked:
            if self.collected:
                if self.open == "open":
                    if self.rect.collidepoint(mouse) and g.backpack.has(self):
                        self.pop_up()
                    else:
                        self.collect()
                elif self.open == "use":
                    if self.following:
                        self.following = False
                        self.collect()
                        g.using = None
                    if self.rect.collidepoint(mouse):
                        self.pop_up()
                        self.following = True
                        g.using = self
            else:
                if self.rect.collidepoint(mouse):
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

    def follow(self):
        mouse = pygame.mouse.get_pos()
        self.rect.topleft = mouse

    def bouce(self):
        self.rect.y += self.bounce_dir
        if self.counter % 10 == 0:
            self.bounce_dir *= -1
        self.counter += 1