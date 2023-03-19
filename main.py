from settings import *

window = pygame.display.set_mode((GAME_HEIGHT, GAME_WIDTH))  # Создаем окно 500 на 400
pygame.display.set_caption(GAME_NAME)  # Устанавливаем заголовок

# Загружаем картинку
cornmen_image = pygame.image.load("./images/hero.png").convert_alpha()
cornmen_image = pygame.transform.smoothscale(cornmen_image, (180, 260))
# Обозначаем форму и фиксируем координаты картинки на экране
cornmen_rect = cornmen_image.get_rect(center=(250, 200))
btn_food = pygame.image.load('./images/food.png')
btn_food_rect = btn_food.get_rect(center=(90, 350))
btn_health = pygame.image.load('./images/health.png')
btn_health_rect = btn_health.get_rect(center=(250, 350))
btn_sleep = pygame.image.load('./images/sleep.png')
btn_sleep_rect = btn_sleep.get_rect(center=(410, 350))
bar_food = pygame.image.load('./images/bar.png')
bar_food_rect = bar_food.get_rect(center=(90, 50))
bar_health = pygame.image.load('./images/bar.png')
bar_health_rect = bar_health.get_rect(center=(90, 90))
bar_sleep = pygame.image.load('./images/bar.png')
bar_sleep_rect = bar_sleep.get_rect(center=(90, 130))

window.fill(BLUE)  # Заливаем фон

# Размещаем картинку и форму в окне
window.blit(cornmen_image, cornmen_rect)
window.blit(btn_food, btn_food_rect)
window.blit(btn_health, btn_health_rect)
window.blit(btn_sleep, btn_sleep_rect)
window.blit(bar_food, bar_food_rect)
window.blit(bar_health, bar_health_rect)
window.blit(bar_sleep, bar_sleep_rect)

pygame.display.update()  # Обновляем окно

game_over = False  # Переменная-флаг, меняется, когда нажмем крестик

while game_over == False:  # Главный цикл программы
    for event in pygame.event.get():  # для каждого события
        if event.type == pygame.QUIT:  # если событие - нажатие кнопки Выход
            game_over = True
pygame.quit()  # Вне цикла выходим из игры

