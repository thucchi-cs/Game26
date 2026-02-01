import pygame
import sprites.collectibles as collectibles
import sprites.background as bg
import sprites.arrow as arrow
import sprites.object as object

# Pygame inits
pygame.init()

# Set up screen
WIDTH = 1480
HEIGHT = 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Timing
FPS = 60

# Static on screen objects
bp_rect = pygame.rect.Rect(WIDTH-200,0,200,200)

# Objects
backpack = pygame.sprite.Group(bg.Background("backpack.png", bp_rect.topleft))
dining1 = pygame.sprite.Group()
dining2 = pygame.sprite.Group()
dining3 = pygame.sprite.Group()
dining4 = pygame.sprite.Group()

# Dining1
dining1.add(bg.Background("dining1.png", size=(1280,720)), arrow.Arrow(30, HEIGHT//2, dining1, dining4, rot=90), arrow.Arrow(WIDTH-230, HEIGHT//2, dining1, dining2, rot=270))

# Dining2
frame = object.Object(714,258, "frame.png", "frame", rot=340)
dining2.add(bg.Background("dining2.png", size=(1280,720)), frame, arrow.Arrow(30, HEIGHT//2, dining2, dining1, rot=90), arrow.Arrow(WIDTH - 230, HEIGHT//2, dining2, dining3, rot=270))

# Dining 3
dining3.add(bg.Background("dining3.png", size=(1280,720)), arrow.Arrow(30, HEIGHT//2, dining3, dining2, rot=90), arrow.Arrow(WIDTH - 230, HEIGHT//2, dining3, dining4, rot=270))

# Dining 4
dining4.add(bg.Background("dining4.png", size=(1280,720)), arrow.Arrow(30, HEIGHT//2, dining4, dining3, rot=90), arrow.Arrow(WIDTH - 230, HEIGHT//2, dining4, dining1, rot=270))
on_screen = pygame.sprite.Group()