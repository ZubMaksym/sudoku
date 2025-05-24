import pygame

window = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Sudoku")

pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 36)
victory_font = pygame.font.SysFont("Comic Sans MS", 52)
defeat_font = victory_font
pause_font = victory_font
restart_font = pygame.font.SysFont("Comic Sans MS", 42)
menu_font = pygame.font.SysFont("Comic Sans MS", 102)

SUB_GRID_SIZE = 3
GRID_SIZE = SUB_GRID_SIZE * SUB_GRID_SIZE

