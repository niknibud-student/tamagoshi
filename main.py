from settings import *
from bar import Bar
from button import Button
from cornmen import Cornmen
from cornmen_motion import cornmen_motion


# НАСТРОЙКИ ИГРЫ
window: pygame.Surface = pygame.display.set_mode((GAME_HEIGHT, GAME_WIDTH))  # Создаем окно 500 на 400
pygame.display.set_caption(GAME_NAME)  # Устанавливаем заголовок

# СОЗДАНИЕ И РАЗМЕЩЕНИЕ ПЕРСОНАЖА
cornmen = Cornmen(250, 200)

# СОЗНАИЕ И РАЗМЕЩЕНИЕ КНОПОК
btn_food = Button('./images/food.png', 90, 350)
btn_health = Button('./images/health.png', 250, 350)
btn_sleep = Button('./images/sleep.png', 410, 350)

# ИНИЦИАЛИЗАЦИЯ ПАНЕЛЕЙ И ИХ НАСТРОЙКА
bar_food = Bar('./images/bar.png', 90, 50)
bar_health = Bar('./images/bar.png', 90, 90)
bar_sleep = Bar('./images/bar.png', 90, 130)

window.fill(BLUE)  # Заливаем фон

# ОТРИСОВКА ГЛАВНОГО ГЕРОЯ
window.blit(cornmen.image, cornmen.rect)

# ОТРИСОВКА КНОПОК
window.blit(btn_food.image, btn_food.rect)
window.blit(btn_health.image, btn_health.rect)
window.blit(btn_sleep.image, btn_sleep.rect)

# ОТРИСОВКА ПАНЕЛЕЙ
window.blit(bar_food.image, bar_food.rect)
window.blit(bar_health.image, bar_health.rect)
window.blit(bar_sleep.image, bar_sleep.rect)

pygame.display.update()  # Обновляем окно

game_over: bool = False  # Переменная-флаг, меняется, когда нажмем крестик

while game_over == False:  # Главный цикл программы
    cornmen.happy(window)
    pygame.display.update()
    pygame.time.delay(1000)
    cornmen.shock(window)
    pygame.display.update()
    pygame.time.delay(1000)
    cornmen.normal(window)
    pygame.display.update()
    pygame.time.delay(1000)
    for event in pygame.event.get():  # для каждого события
        if event.type == pygame.QUIT:  # если событие - нажатие кнопки Выход
            game_over = True
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            cornmen_motion(window, cornmen, x, y)
    pygame.display.update()
pygame.quit()  # Вне цикла выходим из игры

