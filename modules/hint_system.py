# modules/hints/hint_system.py
import pygame

class HintSystem:
    def __init__(self):
        self.selected_cell = None  # (row, col)
        self.conflicts = []

    def select_cell(self, row, col):
        self.selected_cell = (row, col)
        self.conflicts = []

    def check_conflicts(self, grid, row, col, value):
        self.conflicts.clear()
        has_conflict = False

        # Перевірка по рядку
        for c in range(9):
            if c != col and grid[row][c] == value:
                self.conflicts.append((row, c))
                has_conflict = True

        # Перевірка по стовпцю
        for r in range(9):
            if r != row and grid[r][col] == value:
                self.conflicts.append((r, col))
                has_conflict = True

        # Перевірка по квадрату 3x3
        box_x = col // 3 * 3
        box_y = row // 3 * 3
        for i in range(3):
            for j in range(3):
                r, c = box_y + i, box_x + j
                if (r != row or c != col) and grid[r][c] == value:
                    self.conflicts.append((r, c))
                    has_conflict = True

        return has_conflict

    def draw_lines(self, surface, cell_size, selected, offset_x, offset_y, color=(0, 0, 255, 30)):
        if selected is None:
            return

        row, col = selected
        highlight_surf = pygame.Surface((cell_size, cell_size), pygame.SRCALPHA)
        highlight_surf.fill(color)

        for i in range(9):
            surface.blit(highlight_surf, (offset_x + i * cell_size, offset_y + row * cell_size))  # Горизонталь
            surface.blit(highlight_surf, (offset_x + col * cell_size, offset_y + i * cell_size))  # Вертикаль
