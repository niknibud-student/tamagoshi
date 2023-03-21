from settings import *

class Cornmen:
    def __init__(self, x: int, y: int) -> None:
        self.image = pygame.image.load(CORNMEN_NORMAL).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (CORNMEN_SIZE_X, CORNMEN_SIZE_Y))
        self.rect = self.image.get_rect(center=(x, y))

    def happy(self, window: pygame.Surface) -> None:
        self.image = pygame.image.load(CORNMEN_HAPPY).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (CORNMEN_SIZE_X, CORNMEN_SIZE_Y))
        window.blit(self.image, self.rect)

    def normal(self, window: pygame.Surface) -> None:
        self.image = pygame.image.load(CORNMEN_NORMAL)
        self.image = pygame.transform.smoothscale(self.image, (CORNMEN_SIZE_X, CORNMEN_SIZE_Y))
        window.blit(self.image, self.rect)

    def shock(self, window: pygame.Surface) -> None:
        self.image = pygame.image.load(CORNMEN_SHOCK)
        self.image = pygame.transform.smoothscale(self.image, (CORNMEN_SIZE_X, CORNMEN_SIZE_Y))
        window.blit(self.image, self.rect)