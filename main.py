import pygame
from modules.settings import window
from modules.grid import Grid

grid = Grid()
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.fill((255,255,255))
    grid.draw_all(surface= window)
    pygame.display.flip()


