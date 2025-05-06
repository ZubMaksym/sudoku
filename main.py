import pygame
from modules.settings import window
from modules.grid import Grid

grid = Grid()
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]: #check for the left mouse
                pos = pygame.mouse.get_pos()
                grid.get_mouse_click(pos[0],pos[1])

    window.fill((255,255,255))
    grid.draw_all(surface= window)
    pygame.display.flip()


