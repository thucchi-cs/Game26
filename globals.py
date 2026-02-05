import pygame
import sprites.collectibles as collectibles
import sprites.background as bg
import sprites.arrow as arrow
import sprites.object as object
import sprites.robot as robot

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
egg_plate = pygame.sprite.Group()
egg_note = pygame.sprite.Group()

# Dining1
funky_dude = robot.Robot(589, 312, "ronin/Funky Dude.png", dining1, dining4)
frame = object.Object(858, 204, "frame.png", "frame", rot=352, size=(100,70))
dining1.add(bg.Background("Kitchen Overview Red Tile.png", size=(1280,720)), funky_dude, frame, arrow.Arrow(30, HEIGHT//2, dining1, dining4, rot=90), arrow.Arrow(WIDTH-230, HEIGHT//2, dining1, dining2, rot=270))

# Dining2
dining2.add(bg.Background("dining2.png", size=(1280,720)), arrow.Arrow(30, HEIGHT//2, dining2, dining1, rot=90), arrow.Arrow(WIDTH - 230, HEIGHT//2, dining2, dining3, rot=270))

# Dining 3
mannequin = object.Object(770, 500, "ronin/shirt man 2.png", "mannequin", size=(280, 409))
dining3.add(bg.Background("room zoom.png", size=(1280,720)), mannequin, arrow.Arrow(30, HEIGHT//2, dining3, dining2, rot=90), arrow.Arrow(WIDTH - 230, HEIGHT//2, dining3, dining4, rot=270))

# Dining 4
eggbtn = object.Object(631, 591, "eggbtn.png", "eggbtn")
eggs = object.Object(WIDTH + 200, 304, "plate.png", "eggs")
dining4.add(bg.Background("dining1.png", size=(1280,720)), funky_dude, eggbtn, eggs, arrow.Arrow(30, HEIGHT//2, dining4, dining3, rot=90), arrow.Arrow(WIDTH - 230, HEIGHT//2, dining4, dining1, rot=270))

# Eggs screen
plate = object.Object(753,358, "eggs.png", "eggs_plate")
egg_plate.add(bg.Background("4 CLUE.png", size=(1280, 720)), plate)

# Flipped Eggs screen
note = collectibles.Collectible(586, 346, "ronin/Note.png", (328, 300), rot=7)
egg_note.add(bg.Background("Empty Plage.png", size=(1280, 720)), note)
on_screen = pygame.sprite.Group()