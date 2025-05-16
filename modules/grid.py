import pygame
from copy import deepcopy
from .random_fill import create_grid
from .coords_gen import create_line_cords
from .settings import font, SUB_GRID_SIZE
from .remove_numbers import remove_nums
from .solver import SudokuSolver
from .menu.buttons import solve_button
from .game_timer import GameTimer
from .misstake_counter import MistakeCounter
from .hint_system import HintSystem

class Grid:
    def __init__(self):
        self.cell_size = 50
        self.offset_x = (1200 - self.cell_size * 9) // 2
        self.offset_y = (900 - self.cell_size * 9) // 2
        self.num_x_offset = 15

        self.line_coords = create_line_cords(self.cell_size)
        self.grid = create_grid(sub_grid=SUB_GRID_SIZE)
        self.__test_grid = deepcopy(self.grid)
        remove_nums(self.grid)

        self.occupied_cell_coordinates = self._get_occupied_cells()
        self.selected_number = 0
        self.highlight_value = None
        self.is_winner = False

        self.game_font = font
        self.auto_solve_btn = solve_button
        self.timer = GameTimer(self.game_font)
        self.mistake_counter = MistakeCounter(self.game_font)
        self.hints = HintSystem()
        self.wrong_attempts = {}

    def _get_occupied_cells(self) -> list[tuple]:
        occupied = []
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] != 0:
                    occupied.append((y, x))
        return occupied

    def is_cell_preoccupied(self, x: int, y: int) -> bool:
        return (y, x) in self.occupied_cell_coordinates

    def get_cell(self, x: int, y: int):
        return self.grid[y][x]

    def set_cell(self, x: int, y: int, value: int):
        self.grid[y][x] = value

    def get_mouse_click(self, x: int, y: int) -> None:
        self.highlight_value = None
        if self.offset_x <= x < self.offset_x + self.cell_size * 9 and self.offset_y <= y < self.offset_y + self.cell_size * 9:
            col = (x - self.offset_x) // self.cell_size
            row = (y - self.offset_y) // self.cell_size
            if not self.is_cell_preoccupied(col, row):
                self.hints.select_cell(row, col)
        if self.check_grids():
            print("Won, Game Over!")
            self.is_winner = True

    def handle_keyboard_input(self, number: int):
        if self.hints.selected_cell is None:
            return

        row, col = self.hints.selected_cell
        if self.is_cell_preoccupied(col, row):
            return

        correct_value = self.__test_grid[row][col]
        self.set_cell(col, row, number)
        self.highlight_value = number
        self.hints.check_conflicts(self.grid, row, col, number)

        key = (row, col)

        if number != correct_value:
            if key not in self.wrong_attempts or self.wrong_attempts[key] != number:
                self.mistake_counter.increment()
                self.wrong_attempts[key] = number
        else:
            if key in self.wrong_attempts:
                del self.wrong_attempts[key]

        if self.check_grids():
            print("Won, Game Over!")
            self.is_winner = True

    def check_grids(self):
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] != self.__test_grid[y][x]:
                    return False
        return True

    def restart(self):
        self.grid = create_grid(sub_grid=SUB_GRID_SIZE)
        self.__test_grid = deepcopy(self.grid)
        remove_nums(self.grid)
        self.occupied_cell_coordinates = self._get_occupied_cells()
        self.is_winner = False
        self.timer.reset()
        self.mistake_counter.reset()
        self.highlight_value = None
        self.wrong_attempts = {}

    def solve_sudoku(self):
        solver = SudokuSolver(deepcopy(self.__test_grid))
        if solver.solve():
            self.grid = solver.grid
            self.is_winner = True
            self.highlight_value = None
            print("Puzzle solved!")
        else:
            print("No solution exists.")

    def check_is_autosolve_pressed(self):
        event = pygame.event.get()
        self.auto_solve_btn.IS_PRESSED = self.auto_solve_btn.is_pressed(event)
        if self.auto_solve_btn.IS_PRESSED:
            self.solve_sudoku()

    def __draw_lines(self, surface):
        for index, line in enumerate(self.line_coords):
            width = 4 if index in {3, 6, 13, 16} else 1
            pygame.draw.line(surface, (0, 0, 0), line[0], line[1], width=width)

    def __draw_numbers(self, surface):
        for y in range(9):
            for x in range(9):
                value = self.grid[y][x]
                if value != 0:
                    if (y, x) in self.occupied_cell_coordinates:
                        color = (0, 0, 255)
                    elif value != self.__test_grid[y][x]:
                        color = (255, 0, 0)
                    else:
                        color = (0, 255, 0)

                    text_surface = self.game_font.render(str(value), False, color)
                    x_pos = x * self.cell_size + self.offset_x + self.num_x_offset
                    y_pos = y * self.cell_size + self.offset_y
                    surface.blit(text_surface, (x_pos, y_pos))

    def highlight_same_numbers(self, surface):
        if self.highlight_value is None:
            return

        highlight_surf = pygame.Surface((self.cell_size, self.cell_size), pygame.SRCALPHA)
        highlight_surf.fill((255, 255, 0, 100))

        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == self.highlight_value:
                    surface.blit(highlight_surf, (
                        self.offset_x + x * self.cell_size,
                        self.offset_y + y * self.cell_size
                    ))

    def draw_all(self, surface):
        self.__draw_lines(surface)
        self.__draw_numbers(surface)
        self.highlight_same_numbers(surface)
        self.auto_solve_btn.show_image(surface)
        self.timer.draw(surface)
        self.mistake_counter.draw(surface)
        self.hints.draw_lines(surface, self.cell_size, self.hints.selected_cell, self.offset_x, self.offset_y)
