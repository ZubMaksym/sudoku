from copy import deepcopy
from .solver import SudokuSolver

class SudokuSolverCounter(SudokuSolver):
    def __init__(self, grid):
        super().__init__(deepcopy(grid))
        self.solutions = 0

    def solve_and_count(self, row=0, col=0):
        if row == 8 and col == 9:
            self.solutions += 1
            return
        if col == 9:
            row += 1
            col = 0
        if self.grid[row][col] != 0:
            self.solve_and_count(row, col + 1)
            return

        for num in range(1, 10):
            if self.is_safe(row, col, num):
                self.grid[row][col] = num
                self.solve_and_count(row, col + 1)
                self.grid[row][col] = 0

                if self.solutions > 1:
                    return 
