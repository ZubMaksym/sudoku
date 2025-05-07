from .settings import GRID_SIZE
from random import sample

def remove_nums(grid: list[list]) -> None:
    #randomly set numbers to zero in the grid
    num_of_cells = GRID_SIZE * GRID_SIZE
    empies = num_of_cells * 3 // 9 # 7 is ideal - the higher the number, the easier game
    for i in sample(range(num_of_cells), empies):
        grid[i // GRID_SIZE][i % GRID_SIZE] = 0