import math
import pygame
from .random_fill import *
from .coords_gen import create_line_cords
from .settings import font
from .remove_numbers import remove_nums


class Grid:
    def __init__(self):
        self.cell_size = 50
        self.line_coords = create_line_cords(self.cell_size)
        self.grid = create_grid(sub_grid= base)
        self.num_x_offset = 15
        self.game_font = font
        remove_nums(self.grid)
        self.occupied_cell_coordinates = self.pre_occupied_cells_cords()
        print(self.occupied_cell_coordinates)

    def get_mouse_click(self, x: int, y: int) -> None:
        if x > 225 and x < 675 and y > 225 and y < 675:
            col = (x - 225) // 50
            row = (y - 225) // 50
            # print(f"Row: {row}, col: {col}")
            if not self.is_cell_preoccupied(col, row):
                self.set_cell(col, row, -1)
        
    def is_cell_preoccupied(self, x: int, y: int) -> bool:
        #check for occupied cells
        for cell in self.occupied_cell_coordinates:
            if (x == cell[1] and y == cell[0]):
                return True
        return False


    def pre_occupied_cells_cords(self) -> list[tuple]:
        #gather all the x,y cords for all initialised cells
        occupied_cell_coordinates = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell(x, y) != 0:
                    occupied_cell_coordinates.append((y, x)) #first hte row and then the column
        return occupied_cell_coordinates

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
                if self.get_cell(x, y) != 0:
                    text_surface = self.game_font.render(str(self.get_cell(x, y)), False, (255, 0, 0))
                    surface.blit(text_surface, (x * self.cell_size + 225 + self.num_x_offset, y * self.cell_size + 225))

    def draw_all(self, surface):
        self.__draw_lines(surface= surface)
        self.__draw_numbers(surface= surface)

    def get_cell(self, x: int, y: int):
        return self.grid[y][x]
    
    def set_cell(self, x: int, y: int, value: int):
        self.grid[y][x] = value


    # def show(self):
    #     for cell in self.grid:
    #         print(cell)

if __name__ == "__main__":
    grid = Grid()
    grid.show()


        