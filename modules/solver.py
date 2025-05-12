class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid

    def is_safe(self, row, col, num):
        # Перевірка на безпечність (якщо число не зустрічається в рядку, стовпчику та 3x3 підсітці)
        for x in range(9):
            if self.grid[row][x] == num or self.grid[x][col] == num:
                return False

        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False

        return True

    def solve(self, row=0, col=0):
        # Якщо всі клітинки заповнені, повертаємо True
        if row == 8 and col == 9:
            return True
        if col == 9:
            row += 1
            col = 0
        # Якщо клітинка вже має значення, пропускаємо її
        if self.grid[row][col] != 0:
            return self.solve(row, col + 1)

        # Пробуємо можливі числа від 1 до 9
        for num in range(1, 10):
            if self.is_safe(row, col, num):
                self.grid[row][col] = num
                if self.solve(row, col + 1):
                    return True
                self.grid[row][col] = 0  # Відкат при невдачі
        return False