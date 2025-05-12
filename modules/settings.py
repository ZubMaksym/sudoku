import pygame
import os

window = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Sudoku")

pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 36)
victory_font = pygame.font.SysFont("Comic Sans MS", 52)
restart_font = pygame.font.SysFont("Comic Sans MS", 42)
menu_font = pygame.font.SysFont("Comic Sans MS", 102)

SUB_GRID_SIZE = 3
GRID_SIZE = SUB_GRID_SIZE * SUB_GRID_SIZE

def search_abs_path(file_name: str):
    return os.path.abspath(__file__ + f'/../../{file_name}')