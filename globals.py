import pygame
import sprites.collectibles as collectibles
import sprites.background as bg
import sprites.arrow as arrow

# Pygame inits
pygame.init()

# Set up screen
WIDTH = 1000
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Timing
FPS = 60

# Static on screen objects
bp_rect = pygame.rect.Rect(800,0,200,200)

# Objects
backpack = pygame.sprite.Group(bg.Background("backpack.png", bp_rect.topleft))
room1 = pygame.sprite.Group()
room2 = pygame.sprite.Group()
room3 = pygame.sprite.Group()
room4 = pygame.sprite.Group()

room1.add(bg.Background("dining1.png"), collectibles.Collectible(50, 50, "fly.png", (50, 50)), collectibles.Collectible(450, 550, "guy.png", (50,150)), collectibles.Collectible(530, 50, "girl.png", (50, 150)), collectibles.Collectible(750, 250, "guy.png", (50,150)), collectibles.Collectible(150, 150, "fly.png", (50, 50)), collectibles.Collectible(450, 250, "girl.png", (50,150)), collectibles.Collectible(230, 540, "fly.png", (50, 50)), collectibles.Collectible(550, 550, "guy.png", (50,150)), arrow.Arrow(30, 300, room1, room4, rot=90), arrow.Arrow(780, 300, room1, room2, rot=270))
room2.add(bg.Background("dining2.png"), arrow.Arrow(30, 300, room2, room1, rot=90), arrow.Arrow(780, 300, room2, room3, rot=270))
room3.add(bg.Background("dining3.png"), arrow.Arrow(30, 300, room3, room2, rot=90), arrow.Arrow(780, 300, room3, room4, rot=270))
room4.add(bg.Background("dining4.png"), arrow.Arrow(30, 300, room4, room3, rot=90), arrow.Arrow(780, 300, room4, room1, rot=270))
on_screen = pygame.sprite.Group()