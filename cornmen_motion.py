from settings import *
from cornmen import Cornmen

def cornmen_motion(window: pygame.Surface, cornmen: Cornmen, x: int, y: int) -> None:
    if cornmen.rect.collidepoint(x, y):
        cornmen.happy(window)
        pygame.display.update()
    else:
        cornmen.normal(window)
        pygame.display.update()