from settings import *
from bar import Bar
from button import Button
from cornmen import Cornmen


# НАСТРОЙКИ ИГРЫ
window = pygame.display.set_mode((GAME_HEIGHT, GAME_WIDTH))  # Создаем окно 500 на 400
pygame.display.set_caption(GAME_NAME)  # Устанавливаем заголовок

# СОЗДАНИЕ И РАЗМЕЩЕНИЕ ПЕРСОНАЖА
cornmen = Cornmen()
cornmen.set_cornmen("./images/hero.png", 180, 260, 250, 200)

# СОЗНАИЕ И РАЗМЕЩЕНИЕ КНОПОК
btn_food = Button()
btn_food.set_button('./images/food.png', 90, 350)
btn_health = Button()
btn_health.set_button('./images/health.png', 250, 350)
btn_sleep = Button()
btn_sleep.set_button('./images/sleep.png', 410, 350)

# ИНИЦИАЛИЗАЦИЯ ПАНЕЛЕЙ И ИХ НАСТРОЙКА
bar_food = Bar()
bar_food.set_bar('./images/bar.png', 90, 50)
bar_health = Bar()
bar_health.set_bar('./images/bar.png', 90, 90)
bar_sleep = Bar()
bar_sleep.set_bar('./images/bar.png', 90, 130)

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

game_over = False  # Переменная-флаг, меняется, когда нажмем крестик

while game_over == False:  # Главный цикл программы
    for event in pygame.event.get():  # для каждого события
        if event.type == pygame.QUIT:  # если событие - нажатие кнопки Выход
            game_over = True
pygame.quit()  # Вне цикла выходим из игры

