# Imports
import asyncio
import pygame
import globals as g
import levels.intro as intro
import levels.gameplay as gameplay
import levels.end as end

pygame.display.set_caption("TSA Game 2026")

async def main():
    # await intro.intro()
    await gameplay.game()
    # await end.end()

asyncio.run(main())