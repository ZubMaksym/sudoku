import pygame
from modules.settings import window, victory_font, restart_font, menu_font
from modules.grid import Grid
from modules.menu.buttons import start_button, exit_button, hint_button
from modules.game_timer import GameTimer

pygame.init()

grid = Grid()
game = True
in_menu = True

while game:
    if in_menu:
        window.fill((255, 255, 255))

        menu_surface = menu_font.render("SUDOKU", False, (0, 0, 0))
        window.blit(menu_surface, (390, 70))

        start_button.show_image(window)
        exit_button.show_image(window)
        hint_button.show_image(window)

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                game = False

        # Обробка натискання кнопок меню
        if start_button.is_pressed(event_list):
            in_menu = False
            grid.restart()
            grid.timer.reset()

        if hint_button.is_pressed(event_list):
            in_menu = False
            grid.restart()
            grid.show_hints = True
            grid.timer.reset()

        if exit_button.is_pressed(event_list):
            pygame.quit()
            exit()

        pygame.display.flip()
        continue

    # --- Основний ігровий цикл ---
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.MOUSEBUTTONDOWN and not grid.is_winner:
            pos = pygame.mouse.get_pos()
            grid.get_mouse_click(pos[0], pos[1])

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.is_winner:
                grid.restart()
                grid.timer.reset()
            elif pygame.K_1 <= event.key <= pygame.K_9:
                number = event.key - pygame.K_0
                grid.handle_keyboard_input(number)

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

    pygame.display.flip()
