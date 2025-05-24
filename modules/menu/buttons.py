import pygame
pygame.init()

class Button():
    def __init__(self, x: int, y: int, width: int, height: int, text: str, font_size: int = 36):
        self.X = x
        self.Y = y
        self.width = width
        self.height = height
        self.text = text
        self.FONT = pygame.font.SysFont("Comic Sans MS", font_size, bold=True)
        self.COLOR = (70, 130, 180)
        self.HOVER_COLOR = (100, 149, 237)
        self.TEXT_COLOR = (255, 255, 255)
        self.RECT = pygame.Rect(self.X, self.Y, self.width, self.height)

    def show_image(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.HOVER_COLOR if self.RECT.collidepoint(mouse_pos) else self.COLOR
        pygame.draw.rect(surface, current_color, self.RECT, border_radius=10)
        
        text_surface = self.FONT.render(self.text, True, self.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.RECT.center)
        surface.blit(text_surface, text_rect)

    def is_pressed(self, event_list):
        pos = pygame.mouse.get_pos()
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and self.RECT.collidepoint(pos):
                return True
        return False
                        
start_button_menu = Button(x=490, y=330, width=250, height=90, text="Classic Game")
hint_button_menu = Button(x=440, y=450, width=350, height=90, text="Game With Hints")
exit_button_menu = Button(x=490, y=570, width=250, height=90, text="Exit")

solve_button = Button(x=870, y=250, width=100, height=50, text="Solve", font_size= 20)
pause_button = Button(x=870, y= 310, width=100, height=50, text="Pause", font_size= 20)
hint_button = Button(x=870, y= 370, width=100, height=50, text="Hint", font_size= 20)
