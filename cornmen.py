from settings import *

class Cornmen:
    def set_cornmen(self, image: str, size_x: int, size_y: int, x: int, y: int) -> None:
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (size_x, size_y))
        self.rect = self.image.get_rect(center=(x, y))