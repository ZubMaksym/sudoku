from .grid import Grid
from random import choice
from collections import Counter

class HintGrid(Grid):
    def use_hint(self):
        # Якщо гравець уже виграв — підказка не потрібна
        if self.is_winner:
            return

        # Збираємо всі порожні клітинки, які ще можна змінювати (не зафіксовані)
        empty_cells = [
            (y, x) for y in range(9) for x in range(9)
            if self.grid[y][x] == 0 and (y, x) not in self.occupied_cell_coordinates
        ]
        if not empty_cells:
            return  # Підказку дати неможливо

        # Для кожного квадрату 3x3 зберігаємо координати порожніх клітинок
        square_empty_cells = {i: [] for i in range(9)}
        filled_count = Counter()  # Рахуємо, скільки клітинок заповнено в кожному квадраті

        for y, x in empty_cells:
            idx = (y // 3) * 3 + (x // 3)  # Визначаємо індекс квадрата (від 0 до 8)
            square_empty_cells[idx].append((y, x))

        # Рахуємо кількість заповнених клітинок у кожному квадраті 3x3
        for i in range(9):
            y0, x0 = (i // 3) * 3, (i % 3) * 3  # Верхній лівий кут квадрата
            filled_count[i] = sum(
                self.grid[y][x] != 0
                for y in range(y0, y0 + 3)
                for x in range(x0, x0 + 3)
            )

        # Знаходимо квадрат із найбільшою кількістю заповнених клітинок
        target_square = filled_count.most_common(1)[0][0]

        # Якщо в цьому квадраті немає порожніх клітинок — вибираємо будь-яку іншу
        candidates = square_empty_cells[target_square] or empty_cells

        # Випадковим чином вибираємо клітинку-кандидата для підказки
        y, x = choice(candidates)

        # Отримуємо правильне значення цієї клітинки з розв’язку головоломки
        value = self._Grid__test_grid[y][x]

        # Встановлюємо значення та підсвічуємо його
        self.set_cell(x, y, value)
        self.highlight_value = value
        self.hints.select_cell(y, x)

        # Якщо була помилкова спроба для цієї клітинки — видаляємо її
        self.wrong_attempts.pop((y, x), None)
