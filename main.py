import pygame
from modules.settings import window, victory_font, restart_font, menu_font, defeat_font
from modules.grid import Grid
from modules.menu.buttons import start_button_menu, exit_button_menu, hint_button_menu
from modules.hint_grid import HintGrid

pygame.init()

game = True
in_menu = True

while game:
    if in_menu:
        window.fill((255, 255, 255))

        menu_surface = menu_font.render("SUDOKU", False, (0, 0, 0))
        window.blit(menu_surface, (390, 70))

        start_button_menu.show_image(window)
        exit_button_menu.show_image(window)
        hint_button_menu.show_image(window)

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                game = False

        # Обробка натискання кнопок меню
        if start_button_menu.is_pressed(event_list):
            in_menu = False
            grid = Grid()
            grid.is_hint_game = False
            grid.restart()
            grid.timer.reset()

        if hint_button_menu.is_pressed(event_list):
            in_menu = False
            grid = HintGrid()
            grid.is_hint_game = True
            grid.restart()
            grid.timer.reset()

        if exit_button_menu.is_pressed(event_list):
            pygame.quit()
            exit()

        pygame.display.flip()
        continue

    # --- Основний ігровий цикл ---
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            game = False

        if isinstance(grid, HintGrid) and grid.hint_btn.is_pressed(event_list) and not grid.is_winner and not grid.is_defeat:
            grid.use_hint()

        if grid.is_paused:
            continue

        if event.type == pygame.MOUSEBUTTONDOWN and not grid.is_winner and not grid.is_defeat:
            pos = pygame.mouse.get_pos()
            grid.get_mouse_click(pos[0], pos[1])

        if event.type == pygame.KEYDOWN:
            if grid.is_paused:
                continue
            if event.key == pygame.K_SPACE and (grid.is_winner or grid.is_defeat):
                grid.restart()
                grid.timer.reset()
            elif pygame.K_1 <= event.key <= pygame.K_9 and not grid.is_winner and not grid.is_defeat:
                number = event.key - pygame.K_0
                grid.handle_keyboard_input(number)

    if grid.pause_btn.is_pressed(event_list):
        grid.toggle_pause()
    
    if not grid.is_paused:
        if grid.auto_solve_btn.is_pressed(event_list):
            grid.solve_sudoku()

    window.fill((255, 255, 255))
    grid.draw_all(surface=window)

    if grid.is_winner:
        grid.timer.pause()
        won_surface = victory_font.render("You Won!", False, (0, 255, 0))
        window.blit(won_surface, (540, 70))
        restart_surface = restart_font.render("Press space to restart", False, (0, 255, 0))
        window.blit(restart_surface, (440, 130))
    elif grid.is_defeat:
        grid.timer.pause()
        defeat_surface = defeat_font.render("You Lost", False, (255, 0, 0))
        window.blit(defeat_surface, (540, 70))
        restart_surface = restart_font.render("Press space to restart", False, (255, 0, 0))
        window.blit(restart_surface, (440, 130))
    elif grid.is_paused:
        paused_surface = victory_font.render("PAUSED", False, (0, 0, 255))
        window.blit(paused_surface, (530, 70))

    pygame.display.flip()
