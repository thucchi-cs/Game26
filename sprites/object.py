import pygame
import globals as g
import time

class Object(pygame.sprite.Sprite):
    def __init__(self, cx, cy, img, name, size=None, rot=0):
        super().__init__()
        interactions = {"frame": self.animate_on, "eggbtn": self.order_eggs, "eggs": self.close_eggs, "tile": self.break_tile, "man": self.undress, "toilet": self.uncover, "door": self.open_door}
        animations = {"frame": self.animate_frame, "eggs":self.animate_eggs}
        hover = {"frame": True, "door": True, "tile": True}

        # Set up
        self.pos = (cx,cy)
        self.image = pygame.image.load(f"assets/graphics/{img}")
        self.size = size
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
            if (self.shake_count > -1):
                self.shake_count += 1
        else:
            if self.hover:
                self.rect.center = self.pos
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
        if clicked and self.rect.collidepoint(mouse) and self.interact:
            self.interact()
            time.sleep(0.15)

    def animate_on(self):
        self.animating = True
        g.frame_break.play()

    def animate_frame(self):
        pos = self.rect.center
        self.rect.center = (pos[0] - 30, pos[1] + 30)
        if self.rect.y > g.WIDTH:
            g.clue0 = True
            self.animating = False
            g.dining1.remove(g.frame2)
            self.remove(g.dining2)
            self.remove(g.on_screen)
            g.clue0 = True
            g.dining4.add(g.eggbtn)

    def animate_eggs(self):
        if self.rect.x <= 852:
            self.animating = False
            return
        self.rect.x -= 8

    def start_eggs(self):
        self.animating = True
        self.rect.x = 1183

    def close_eggs(self):
        g.load_screen(g.dining4, g.egg_plate)
        g.note_collected = True
        g.dining2.add(g.scene_changer.Scene_changer(904, 650, "arrow.png", g.dining2, g.bathroom, size=(50,30)))

    def order_eggs(self):
        print("what")
        g.eggs.start_eggs()
        self.remove(g.dining4)
        g.beepboop.play()

    def break_tile(self):
        if (self.counter == 0) and (g.using == g.hammer):
            self.counter += 1
            pos = self.rect.center
            self.image = pygame.image.load(f"assets/graphics/tilebroken.png")
            self.rect = self.image.get_rect()
            self.rect.center = pos
            g.smash.play()
        elif self.counter == 1:
            self.remove(g.dining1)
            self.remove(g.on_screen)
            g.coin2.add(g.dining1, g.on_screen)
            self.counter += 1
            g.clue2 = True

    def open_door(self):
        if g.using == g.key:
            g.win.play()
            time.sleep(0.5)
            g.load_screen(g.dining1, g.end)

    def undress(self):
        if g.note_collected and not g.clue3:
            self.image = pygame.image.load(f"assets/graphics/ronin/man.png")
            if self.size:
                self.image = pygame.transform.scale(self.image, self.size)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            g.clue3 = True
            g.coin3.add(g.dining1, g.on_screen)

    def uncover(self):
        if not g.clue1:
            self.image = pygame.image.load(f"assets/graphics/ronin/ToiletUncovered.png")
            if self.size:
                self.image = pygame.transform.scale(self.image, self.size)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            g.clue1 = True
            g.coin1.add(g.bathroom, g.on_screen)