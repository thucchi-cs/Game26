# Imports
import asyncio
import pygame
import globals as g

# Main game
async def game():
    # Set up stuff
    clock = pygame.time.Clock()
    run = True
    quit = False

    # Graphics
    g.on_screen.add(g.start)
    hovers = [i for i in g.on_screen.sprites() + g.backpack.sprites() if (type(i) in g.hover_types)]
    g.hoverable.add(hovers)

    # Music and sounds
    g.game_music.load()

    # Game loop
    while run:
        clock.tick(g.FPS)

        # Check for events
        for event in pygame.event.get():
            # Check to close game
            if event.type == pygame.QUIT:
                run = False
                quit = True

            # Check keyboard inputs
            if event.type == pygame.KEYDOWN:
                # Check to quit
                if event.key == pygame.K_q:
                    run = False
                    quit = True

                # Debug position print
                if event.key == pygame.K_SPACE:
                    print(pygame.mouse.get_pos())

        # Draw
        g.SCREEN.fill((255,255,255))

        g.on_screen.draw(g.SCREEN)
        g.on_screen.update()
        
        g.backpack.update()
        g.backpack.draw(g.SCREEN)

        # Hovering
        g.is_hovering()

        pygame.display.flip()

        # Asyncio
        await asyncio.sleep(0)

