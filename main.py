import pygame
from modules.settings import window, victory_font, restart_font, menu_font, defeat_font, pause_font
from modules.grid import Grid
from modules.menu.buttons import start_button_menu, exit_button_menu, hint_button_menu
from modules.hint_grid import HintGrid

pygame.init()

def show_menu():
    window.fill((255, 255, 255))
    window.blit(menu_font.render("SUDOKU", False, (0, 0, 0)), (390, 70))
    for button in (start_button_menu, exit_button_menu, hint_button_menu):
        button.show_image(window)
    pygame.display.flip()

def show_end_screen(text, font, color):
    grid.timer.pause()
    grid.is_paused = False
    window.blit(font.render(text, False, color), (520, 70))
    window.blit(restart_font.render("Press space to restart", False, color), (440, 130))

def handle_menu_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            return "exit"
    if start_button_menu.is_pressed(events):
        return "start"
    if hint_button_menu.is_pressed(events):
        return "hint"
    if exit_button_menu.is_pressed(events):
        return "exit"
    return None

def handle_game_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            return "exit"
        if grid.is_paused:
            continue
        if isinstance(grid, HintGrid) and grid.hint_btn.is_pressed(events) and not (grid.is_winner or grid.is_defeat):
            grid.use_hint()
        if event.type == pygame.MOUSEBUTTONDOWN and not (grid.is_winner or grid.is_defeat):
            grid.get_mouse_click(*pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and (grid.is_winner or grid.is_defeat):
                grid.restart()
                grid.timer.reset()
            elif pygame.K_1 <= event.key <= pygame.K_9 and not (grid.is_winner or grid.is_defeat):
                grid.handle_keyboard_input(event.key - pygame.K_0)
    if grid.pause_btn.is_pressed(events):
        grid.toggle_pause()
    if not grid.is_paused and grid.auto_solve_btn.is_pressed(events):
        grid.solve_sudoku()
    return None

game, in_menu = True, True
grid = None

while game:
    if in_menu:
        show_menu()
        action = handle_menu_events(pygame.event.get())
        if action == "exit":
            game = False
        elif action == "start":
            in_menu = False
            grid = Grid()
        elif action == "hint":
            in_menu = False
            grid = HintGrid()
        if not in_menu and grid:
            grid.is_hint_game = isinstance(grid, HintGrid)
            grid.restart()
            grid.timer.reset()
        continue

    events = pygame.event.get()
    result = handle_game_events(events)
    if result == "exit":
        break

    window.fill((255, 255, 255))
    grid.draw_all(surface=window)

    if grid.is_winner:
        show_end_screen("YOU WON!", victory_font, (0, 255, 0))
    elif grid.is_defeat:
        show_end_screen("YOU LOST", defeat_font, (255, 0, 0))
    elif grid.is_paused:
        window.blit(pause_font.render("PAUSED", False, (0, 0, 255)), (530, 70))

    pygame.display.flip()
