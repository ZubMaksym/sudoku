import pygame
from modules.settings import window, victory_font, restart_font, menu_font
from modules.grid import Grid
from modules.menu.buttons import start_button, exit_button

pygame.init()

grid = Grid()
game = True
in_menu = True

while game:
    if in_menu:
        window.fill((0, 0, 0))

        menu_surface = menu_font.render("SUDOKU", False, (255, 255, 255))
        window.blit(menu_surface, (390, 70))

        start_button.show_image(window)
        exit_button.show_image(window)

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                game = False

        # Обробка натискання кнопок меню
        if start_button.is_pressed(event_list):
            in_menu = False
        if exit_button.is_pressed(event_list):
            pygame.quit()
            exit()

        pygame.display.flip()
        continue  # Перейти до наступної ітерації

    # --- Основний ігровий цикл ---
    event_list = pygame.event.get()

    # Перевірка на вихід
    for event in event_list:
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.MOUSEBUTTONDOWN and not grid.is_winner:
            pos = pygame.mouse.get_pos()
            grid.get_mouse_click(pos[0], pos[1])

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.is_winner:
                grid.restart()

    # Перевірка натиснення кнопки "Solve"
    if grid.auto_solve_btn.is_pressed(event_list):
        grid.solve_with_button()

    # Малювання гри
    window.fill((255, 255, 255))
    grid.draw_all(surface=window)

    if grid.is_winner:
        won_surface = victory_font.render("You Won!", False, (0, 255, 0))
        window.blit(won_surface, (540, 70))
        restart_surface = restart_font.render("Press space to restart", False, (0, 255, 0))
        window.blit(restart_surface, (440, 130))

    pygame.display.flip()
