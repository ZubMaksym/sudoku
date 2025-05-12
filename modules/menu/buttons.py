import pygame
from modules.settings import search_abs_path

start_image= "modules/menu/start_btn.png"

exit_image= "modules/menu/exit_btn.png"

solve_image = "modules/menu/solved.png"

class Button():
    def __init__(self, x: int, y: int, width: int, height: int, name_image: str):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.NAME_IMAGE = name_image
        self.IS_PRESSED = False

        self.load_image()

    def load_image(self):
        image_path = search_abs_path(file_name=self.NAME_IMAGE)
        image_load = pygame.image.load(image_path)
        self.IMAGE = pygame.transform.scale(image_load, (self.WIDTH, self.HEIGHT))
        self.RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)

    def show_image(self, surface):
        surface.blit(self.IMAGE, (self.X, self.Y))

    def is_pressed(self, event_list):
        pos = pygame.mouse.get_pos()
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and self.RECT.collidepoint(pos):
                return True
        return False
                                

start_button = Button(x= 500, y= 350, width= 200, height= 80, name_image= start_image)
exit_button = Button(x= 500, y= 500, width= 200, height= 80, name_image= exit_image)
solve_button = Button(x= 880, y= 250, width= 80, height= 80, name_image= solve_image)