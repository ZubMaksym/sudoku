import pygame

window = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Sudoku")

pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 36)

SUB_GRID_SIZE = 3
GRID_SIZE = SUB_GRID_SIZE * SUB_GRID_SIZE
