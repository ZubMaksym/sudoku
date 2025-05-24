from .grid import Grid
from random import choice
from collections import Counter

class HintGrid(Grid):
    def use_hint(self):
        if self.is_winner:
            return

        empty_cells = [
            (y, x) for y in range(9) for x in range(9)
            if self.grid[y][x] == 0 and (y, x) not in self.occupied_cell_coordinates
        ]
        if not empty_cells:
            return

        square_empty_cells = {i: [] for i in range(9)}
        filled_count = Counter()

        for y, x in empty_cells:
            idx = (y // 3) * 3 + (x // 3)  
            square_empty_cells[idx].append((y, x))

        for i in range(9):
            y0, x0 = (i // 3) * 3, (i % 3) * 3
            filled_count[i] = sum(
                self.grid[y][x] != 0
                for y in range(y0, y0 + 3)
                for x in range(x0, x0 + 3)
            )

        target_square = filled_count.most_common(1)[0][0]

        candidates = square_empty_cells[target_square] or empty_cells

        y, x = choice(candidates)

        value = self._Grid__test_grid[y][x]

        self.set_cell(x, y, value)
        self.highlight_value = value
        self.hints.select_cell(y, x)

        self.wrong_attempts.pop((y, x), None)
