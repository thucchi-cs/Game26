import pygame
import time
import globals as g

class Button(pygame.sprite.Sprite):
    count = 0
    cyorjude = []
    def __init__(self, cx, cy, img, size, disp, dispG):
        super().__init__()
        # Set up
        self.image = pygame.image.load(f"assets/graphics/{img}")
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.centerx = cx
        self.rect.centery = cy
        
        # Object's variables
        if not disp:
            self.bs = True
            self.img = None
            self.displays = []
        else:
            self.img = pygame.image.load(f"assets/graphics/ronin/{disp}")
            self.img = pygame.transform.scale(self.img, (22,22))
            self.displays = []
            self.bs = False
    
    def update(self):
        self.is_clicked()
        self.display()

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]
        if clicked and self.rect.collidepoint(mouse):
            if self.bs:
                Button.delete()
                time.sleep(0.25)
            else:
                if Button.count < 4:
                    self.displays.append(Button.calc_pos())
                    Button.count += 1
                    Button.cyorjude.append(self)
                    Button.check()
                    time.sleep(0.25)

    def display(self):
        for d in self.displays:
            g.SCREEN.blit(self.img, d)

    def calc_pos():
        y = 204
        x = 951 + Button.count * 46
        return (x,y)
        
    def delete():
        if  Button.count >= 1:
            Button.count -= 1
            btn = Button.cyorjude.pop()
            btn.displays.pop()
            print(btn)

    def check():
        correct = [g.btn9, g.btn4, g.btn2, g.btn8]
        if Button.cyorjude == correct and not g.clue4:
            g.clue4 = True
            g.coin4.add(g.micro_screen, g.on_screen)
