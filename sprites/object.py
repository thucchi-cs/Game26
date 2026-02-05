import pygame
import globals as g
import time

class Object(pygame.sprite.Sprite):
    def __init__(self, cx, cy, img, name, size=None, rot=0):
        super().__init__()
        interactions = {"frame": self.animate_on, "eggbtn": self.order_eggs, "eggs": self.close_eggs, "eggs_plate": self.flip_eggs}
        animations = {"frame": self.animate_frame, "eggs":self.animate_eggs}
        hover = {"frame": True}

        # Set up
        self.image = pygame.image.load(f"assets/graphics/{img}")
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rot = rot
        self.image = pygame.transform.rotate(self.image, rot)
        self.rect = self.image.get_rect()
        self.rect.centerx = cx
        self.rect.centery = cy
        self.name = name
        
        # Object's variables
        self.animating = False
        self.interact = interactions.get(name)
        self.animate = animations.get(name)
        self.hover = hover.get(name)
        self.counter = 0
        self.shake_count = -1
        self.shake_dir = 1
    
    def update(self):
        if self.animating and self.animate:
            self.animate()
        else:
            self.is_clicked()
            self.is_hovered()
            if self.shake_count > 0 and self.hover:
                self.shake()
        

    def is_hovered(self):
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
            if (self.shake_count > -1):
                self.shake_count += 1
        else:
            self.shake_count = 0
            pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))

    def shake(self):
        self.rect.x += self.shake_dir
        if self.shake_count % 5 == 0:
            self.shake_dir *= -1

        if self.shake_count >= 20:
            self.shake_count = -1
    
    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]
        if clicked and self.rect.collidepoint(mouse) and self.interact:
            self.interact()
            time.sleep(0.15)

    def animate_on(self):
        self.animating = True

    def animate_frame(self):
        pos = self.rect.center
        self.rect.center = (pos[0] - 30, pos[1] + 30)
        if self.rect.y > g.WIDTH:
            self.animating = False

    def animate_eggs(self):
        if self.rect.x <= 768:
            self.animating = False
            return
        self.rect.x -= 8

    def start_eggs(self):
        self.animating = True
        self.rect.x = 1183

    def close_eggs(self):
        g.on_screen.remove(g.dining4)
        g.on_screen.add(g.egg_plate)

    def flip_eggs(self):
        g.on_screen.remove(g.egg_plate)
        g.on_screen.add(g.egg_note)

    def order_eggs(self):
        g.eggs.start_eggs()