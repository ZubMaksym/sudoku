import pygame
from modules.settings import window
from modules.settings import victory_font, restart_font
from modules.grid import Grid

grid = Grid()
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN and not grid.isWinner:
            if pygame.mouse.get_pressed()[0]: #check for the left mouse
                pos = pygame.mouse.get_pos()
                grid.get_mouse_click(pos[0],pos[1])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.isWinner:
               grid.restart() 

    window.fill((255,255,255))
    
    grid.draw_all(surface= window)

    if grid.isWinner:
        won_surface = victory_font.render("You Won!", False, (0, 255, 0))
        window.blit(won_surface, (540, 70))
        restart_surface = restart_font.render("Press space to restart", False, (0, 255, 0))
        window.blit(restart_surface, (440, 130))

    pygame.display.flip()


