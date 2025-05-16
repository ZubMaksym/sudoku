import time

class GameTimer:
    def __init__(self, font):
        self.start_time = time.time()
        self.paused_time = 0
        self.is_paused = False
        self.font = font

    def reset(self):
        self.start_time = time.time()
        self.paused_time = 0
        self.is_paused = False

    def pause(self):
        if not self.is_paused:
            self.paused_time = time.time() - self.start_time
            self.is_paused = True

    def resume(self):
        if self.is_paused:
            self.start_time = time.time() - self.paused_time
            self.is_paused = False

    def get_elapsed_time(self):
        if self.is_paused:
            elapsed = int(self.paused_time)
        else:
            elapsed = int(time.time() - self.start_time)
        minutes = elapsed // 60
        seconds = elapsed % 60
        return f"{minutes:02}:{seconds:02}"

    def draw(self, surface, x=50, y=50):
        time_str = self.get_elapsed_time()
        text_surface = self.font.render(f"Time: {time_str}", True, (0, 0, 0))
        surface.blit(text_surface, (x, y))