import pygame

class SelectNumber:
    def __init__(self, font):
        self.btn_width = 40
        self.btn_height = 40
        self.font = font
        self.selected_number = 0
        self.color_selected = (0, 255, 0)
        self.color_default = (0, 0, 0)
        self.btn_positions = [(875, 350), (925, 350),
                              (875, 400), (925, 400),
                              (875, 450), (925, 450),
                              (875, 500), (925, 500),
                              (900, 550),]
    def draw(self, surface):
        for index, pos in enumerate(self.btn_positions):
            pygame.draw.rect(surface, self.color_default, [pos[0], pos[1], self.btn_width, self.btn_height], width=2, border_radius=7)
            if self.button_hover(pos):
                pygame.draw.rect(surface, self.color_selected, [pos[0], pos[1], self.btn_width, self.btn_height], width=2, border_radius=7)
                text_surface = self.font.render(str(index + 1), False, self.color_selected)
            else:
                text_surface = self.font.render(str(index + 1), False, self.color_default)
            
            #check if the number was selected and draw it green
            if self.selected_number > 0:
                if self.selected_number - 1 == index:
                    pygame.draw.rect(surface, self.color_selected, [pos[0], pos[1], self.btn_width, self.btn_height], width=2, border_radius=7)
                    text_surface = self.font.render(str(index + 1), False, self.color_selected)

            surface.blit(text_surface, (pos[0] + 10, pos[1] - 7))


    def on_button(self, mouse_x: int, mouse_y: int, pos: tuple) -> bool:
        return mouse_x > pos[0] and mouse_x < pos[0] + self.btn_width and mouse_y > pos[1] and mouse_y < pos[1] + self.btn_height

    def button_hover(self, pos: tuple) -> bool | None:
        mouse_pos = pygame.mouse.get_pos() 
        if self.on_button(mouse_x= mouse_pos[0], mouse_y= mouse_pos[1], pos= pos):
            return True
        
    def button_clicked(self, mouse_x: int, mouse_y: int) -> None:
        for index, pos in enumerate(self.btn_positions):
            if self.on_button(mouse_x, mouse_y, pos):
                self.selected_number = index + 1



