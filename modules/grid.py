import pygame
from copy import deepcopy
from .random_fill import *
from .coords_gen import create_line_cords
from .settings import font, SUB_GRID_SIZE
from .remove_numbers import remove_nums
from .selection import SelectNumber
from .solver import SudokuSolver
from .menu.buttons import solve_button
from .game_timer import GameTimer
from .misstake_counter import MistakeCounter

class Grid:
    def __init__(self):
        self.cell_size = 50
        self.line_coords = create_line_cords(self.cell_size)
        self.grid = create_grid(sub_grid=SUB_GRID_SIZE)
        self.__test_grid = deepcopy(self.grid)  # Створюємо копію перед видаленням чисел
        remove_nums(self.grid)
        self.num_x_offset = 15
        self.game_font = font
        self.occupied_cell_coordinates = self.pre_occupied_cells_cords()
        self.selection = SelectNumber(self.game_font)
        self.is_winner = False
        self.auto_solve_btn = solve_button
        self.misstakes = 0

        self.timer = GameTimer(self.game_font)
        self.mistake_counter = MistakeCounter(self.game_font)

    def get_mouse_click(self, x: int, y: int) -> None:
        if x > 225 and x < 675 and y > 225 and y < 675:
            col = (x - 225) // 50
            row = (y - 225) // 50
            # print(f"Row: {row}, col: {col}")
            if not self.is_cell_preoccupied(col, row):
                if self.__test_grid[row][col] != 0 and self.selection.selected_number != self.__test_grid[row][col]:
                    self.mistake_counter.increment()
                self.set_cell(col, row, self.selection.selected_number)
        self.selection.button_clicked(x, y)
        if self.check_grids():
            print("Won, Game Over!")
            self.is_winner = True
                
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
                    if(y, x) in self.occupied_cell_coordinates:
                        text_surface = self.game_font.render(str(self.get_cell(x, y)), False, (0, 0, 255))
                    else:
                        text_surface = self.game_font.render(str(self.get_cell(x, y)), False, (0, 255, 0))
                    if self.get_cell(x, y) != self.__test_grid[y][x]:
                        text_surface = self.game_font.render(str(self.get_cell(x, y)), False, (255, 0, 0))
                        
                    surface.blit(text_surface, (x * self.cell_size + 225 + self.num_x_offset, y * self.cell_size + 225))

    def draw_all(self, surface):
        self.__draw_lines(surface= surface)
        self.__draw_numbers(surface= surface)
        self.selection.draw(surface= surface)
        self.auto_solve_btn.show_image(surface= surface)
        self.timer.draw(surface)
        self.mistake_counter.draw(surface)

    def get_cell(self, x: int, y: int):
        return self.grid[y][x]
    
    def set_cell(self, x: int, y: int, value: int):
        self.grid[y][x] = value

    def check_grids(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] != self.__test_grid[y][x]:
                    return False
        return True
    
    def restart(self) -> None:
        # Відновлюємо початкові значення та знову генеруємо нове поле
        self.grid = create_grid(sub_grid= SUB_GRID_SIZE)
        self.__test_grid = deepcopy(self.grid)
        remove_nums(self.grid)
        self.occupied_cell_coordinates = self.pre_occupied_cells_cords()
        self.is_winner = False

        self.timer.reset()
        self.mistake_counter.reset()

    def solve_sudoku(self):
        solver = SudokuSolver(deepcopy(self.__test_grid))
        success = solver.solve()
        if success:
            print("Puzzle solved!")
            self.grid = solver.grid  # Оновлюємо поле
            self.is_winner = True
        else:
            print("No solution exists.")
    
    def check_is_autosolve_pressed(self):
        event = pygame.event.get()
        self.auto_solve_btn.IS_PRESSED = self.auto_solve_btn.is_pressed(event)
        if (self.auto_solve_btn.IS_PRESSED):
            self.solve_sudoku()


# if __name__ == "__main__":
#     grid = Grid()
#     grid.show()


        