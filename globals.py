import pygame
import sprites.collectibles as collectibles

# Pygame inits
pygame.init()

# Set up screen
WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Timing
FPS = 60

# Static on screen objects
backpack = pygame.rect.Rect(600,0,200,200)

# Objects
collected = pygame.sprite.Group()
room1 = pygame.sprite.Group(collectibles.Collectible(50, 50, "fly.png", (50, 50)), collectibles.Collectible(450, 550, "guy.png", (50,150)), collectibles.Collectible(530, 50, "girl.png", (50, 150)), collectibles.Collectible(750, 250, "guy.png", (50,150)), collectibles.Collectible(150, 150, "fly.png", (50, 50)), collectibles.Collectible(450, 250, "girl.png", (50,150)), collectibles.Collectible(230, 540, "fly.png", (50, 50)), collectibles.Collectible(550, 550, "guy.png", (50,150)))
on_screen = room1
