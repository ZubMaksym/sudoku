
class MistakeCounter:
    def __init__(self, font):
        self.font = font
        self.mistakes = 0

    def reset(self):
        self.mistakes = 0

    def increment(self):
        self.mistakes += 1

    def draw(self, surface, x=50, y=100):
        text_surface = self.font.render(f"Mistakes: {self.mistakes}", True, (255, 0, 0))
        surface.blit(text_surface, (x, y))
