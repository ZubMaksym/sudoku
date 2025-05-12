from random import sample
from copy import deepcopy
from .solution_counter import SudokuSolverCounter  # Це твій новий клас, який рахує кількість рішень

def remove_nums(grid: list[list]) -> None:
    num_of_cells = len(grid) * len(grid)
    empties_target = num_of_cells * 3 // 7  # Скільки хочеш видалити
    cells = sample(range(num_of_cells), num_of_cells)  # Рандомний порядок проходу клітинок
    removed = 0

    for i in cells:
        row, col = i // len(grid), i % len(grid)
        if grid[row][col] == 0:
            continue

        backup = grid[row][col]
        grid[row][col] = 0

        # Тепер перевіримо чи залишився лише 1 розв'язок
        solver = SudokuSolverCounter(deepcopy(grid))
        solver.solve_and_count()

        if solver.solutions != 1:
            grid[row][col] = backup  # Відкат, бо стало більше 1 розв'язку
        else:
            removed += 1
            if removed >= empties_target:
                break