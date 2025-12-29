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

        # Draw
        g.SCREEN.fill((255,255,0))
        pygame.draw.rect(g.SCREEN, (150,75,0), g.backpack)

        g.on_screen.update()
        g.on_screen.draw(g.SCREEN)
        
        g.collected.update()
        g.collected.draw(g.SCREEN)

        pygame.display.flip()

        # Asyncio
        await asyncio.sleep(0)

