import pygame
import globals as g

class Object(pygame.sprite.Sprite):
    def __init__(self, cx, cy, img, name, size=None, rot=0):
        super().__init__()
        interactions = {"frame": self.animate_on}
        animations = {"frame": self.animate_frame}

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
        self.animating = False
        self.interact = interactions[name]
        self.animate = animations[name]
        self.counter = 0
        self.shake_count = -1
        self.shake_dir = 1
    
    def update(self):
        if self.animating:
            self.animate()
        else:
            self.is_clicked()
            self.is_hovered()
            if self.shake_count > 0:
                self.shake()
        

    def is_hovered(self):
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            if (self.shake_count > -1):
                self.shake_count += 1
        else:
            self.shake_count = 0

    def shake(self):
        self.rect.x += self.shake_dir
        if self.shake_count % 5 == 0:
            self.shake_dir *= -1

        if self.shake_count >= 20:
            self.shake_count = -1
    
    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]
        if clicked and self.rect.collidepoint(mouse):
            self.interact()

    def animate_on(self):
        self.animating = True
        print("hello")

    def animate_frame(self):
        # if self.counter % 10 == 0:
            pos = self.rect.center
            # self.rot -= 10
            # self.image = pygame.transform.rotate(self.image, self.rot)
            # self.rect = self.image.get_rect()
            self.rect.center = (pos[0] - 30, pos[1] + 30)
        # self.counter += 1
