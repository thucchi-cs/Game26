# Imports
import asyncio
import pygame
import globals as g

# Main game
async def intro():
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
        g.SCREEN.fill((0,255,255))
        pygame.display.flip()

        # Asyncio
        await asyncio.sleep(0)