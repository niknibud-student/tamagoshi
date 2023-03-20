from settings import *

class Button:
    def set_button(self, image: str, x: int, y: int) -> None:
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))