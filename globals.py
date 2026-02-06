import pygame
import sprites.collectibles as collectibles
import sprites.background as bg
import sprites.scene_changer as scene_changer
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
funky_dude = robot.Robot(589, 312, 617,337, "ronin/Funky Dude.png", dining1, dining4, newsize=3)
dining1.add(bg.Background("cool dude .png", size=(1280,720)), funky_dude, scene_changer.Scene_changer(WIDTH//2, HEIGHT-30, "arrow.png", dining1, dining3, rot=180, size=(50,30)), scene_changer.Scene_changer(WIDTH-230, HEIGHT//2, "arrow.png", dining1, dining2, rot=270, size=(50,30)))

# Dining2
frame = object.Object(334,262, "frame.png", "frame", rot=352, size=(350,250))
dining2.add(bg.Background("yes ronin it is.png", size=(1280,720)), frame, scene_changer.Scene_changer(30, HEIGHT//2, "arrow.png", dining2, dining1, rot=90, size=(50,30)), scene_changer.Scene_changer(WIDTH - 230, HEIGHT//2, "arrow.png", dining2, dining3, rot=270, size=(50,30)))

# Dining 3
mannequin = object.Object(770, 500, "ronin/shirt man 2.png", "mannequin", size=(280, 409))
dining3.add(bg.Background("room zoom.png", size=(1280,720)), mannequin, scene_changer.Scene_changer(30, HEIGHT//2, "arrow.png", dining3, dining2, rot=90, size=(50,30)), scene_changer.Scene_changer(WIDTH//2, HEIGHT - 30, "arrow.png", dining3, dining1, rot=180, size=(50,30)))

# Dining 4
eggbtn = object.Object(631, 591, "ronin/order eggs.png", "eggbtn", size=(121, 62))
eggs = object.Object(WIDTH + 200, 486, "ronin/hres plat.png", "eggs", size=(200, 30))
# eggs = scene_changer.Scene_changer(WIDTH + 200, 304, "plate.png", dining4, egg_plate)
dining4.add(bg.Background("Funky Dude is Literally Me.png", size=(1280,720)), funky_dude, eggbtn, eggs, scene_changer.Scene_changer(WIDTH//2, HEIGHT - 30, "arrow.png", dining4, dining1, rot=180, size=(50,30)))

# Eggs screen
plate = scene_changer.Scene_changer(753,358, "eggs.png", egg_plate, egg_note)
egg_plate.add(bg.Background("4 CLUE.png", size=(1280, 720)), plate, scene_changer.Scene_changer(WIDTH//2, HEIGHT - 30, "arrow.png", egg_plate, dining1, rot=180, size=(50,30)))

# Flipped Eggs screen
note = collectibles.Collectible(586, 386, "ronin/NoteREAL.png", "open", size=(350, 450), rot=0)
egg_note.add(bg.Background("Empty Plage.png", size=(1280, 720)), note, scene_changer.Scene_changer(WIDTH//2, HEIGHT - 30, "arrow.png", egg_note, dining1, rot=180, size=(50,30)))
on_screen = pygame.sprite.Group()
hoverable = pygame.sprite.Group()
hover_types = [object.Object, collectibles.Collectible, scene_changer.Scene_changer, robot.Robot]

def load_screen(unload: pygame.sprite.Group, load: pygame.sprite.Group):
    on_screen.remove(unload)
    on_screen.add(load)
    hovers = [i for i in load.sprites() + backpack.sprites() if (type(i) in hover_types)]
    hoverable.empty()
    hoverable.add(hovers)

def is_hovering():
    mouse = pygame.mouse.get_pos()
    for obj in hoverable.sprites():
        if obj.rect.collidepoint(mouse):
            pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
            return
    pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))