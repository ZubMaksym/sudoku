from .grid import Grid
from random import choice
from collections import Counter

class HintGrid(Grid):
    def use_hint(self):
        if self.is_winner:
            return

        # Крок 1: Знайти всі незаповнені клітинки
        empty_cells = [
            (y, x) for y in range(9) for x in range(9)
            if self.grid[y][x] == 0 and (y, x) not in self.occupied_cell_coordinates
        ]

        if not empty_cells:
            return

        # Крок 2–3: Визначити квадрат з найбільшою кількістю заповнених клітинок
        squares = {i: [] for i in range(9)}
        filled_counter = Counter()
        for y, x in empty_cells:
            square_index = (y // 3) * 3 + (x // 3)
            squares[square_index].append((y, x))

        for i in range(9):
            y0, x0 = (i // 3) * 3, (i % 3) * 3
            count = sum(
                1 for y in range(y0, y0 + 3) for x in range(x0, x0 + 3)
                if self.grid[y][x] != 0
            )
            filled_counter[i] = count

        most_filled = filled_counter.most_common(1)[0][0]
        candidates = squares[most_filled] or empty_cells

        # Крок 4–5: Отримати правильне значення з рішення
        y, x = choice(candidates)
        value = self._Grid__test_grid[y][x]

        # Крок 6: Записати значення та встановити підсвітку
        self.set_cell(x, y, value)
        self.highlight_value = value
        self.hints.select_cell(y, x)

        self.wrong_attempts.pop((y, x), None)