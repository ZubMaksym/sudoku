import pygame
from .random_fill import *
from .coords_gen import create_line_cords
from .settings import font

class Grid:
    def __init__(self):
        self.cell_size = 50
        self.line_coords = create_line_cords(self.cell_size)
        self.grid = create_grid(sub_grid= base)
        self.num_x_offset = 15
        self.game_font = font

    def __draw_lines(self, surface):
        for index, line in enumerate(self.line_coords):
            if index == 3 or index == 6 or index == 13 or index == 16:
                pygame.draw.line(surface, (0, 0, 0), line[0], line[1], width= 4)
            else:
                pygame.draw.line(surface, (0, 0, 0), line[0], line[1])

    def __draw_numbers(self, surface):
        #draw the grid numbers
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                text_surface = self.game_font.render(str(self.get_cell(x, y)), False, (255, 0, 0))
                surface.blit(text_surface, (x * self.cell_size + 225 + self.num_x_offset, y * self.cell_size + 225))

    def draw_all(self, surface):
        self.__draw_lines(surface= surface)
        self.__draw_numbers(surface= surface)

    def get_cell(self, x: int, y: int):
        return self.grid[y][x]
    
    def set_cell(self, x: int, y: int, value: int):
        self.grid[y][x] = value


    def show(self):
        for cell in self.grid:
            print(cell)

if __name__ == "__main__":
    grid = Grid()
    grid.show()


        