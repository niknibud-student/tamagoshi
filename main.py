from settings import *

window = pygame.display.set_mode((GAME_HEIGHT, GAME_WIDTH))  # Создаем окно 500 на 400
pygame.display.set_caption(GAME_NAME)  # Устанавливаем заголовок

# Загружаем картинку
cornmen_image = pygame.image.load("hero.png").convert_alpha()
cornmen_image = pygame.transform.smoothscale(cornmen_image, (180, 260))
# Обозначаем форму и фиксируем координаты картинки на экране
cornmen_rect = cornmen_image.get_rect(center=(250, 200))

window.fill(BLUE)  # Заливаем фон

# Размещаем картинку и форму в окне
window.blit(cornmen_image, cornmen_rect)

pygame.display.update()  # Обновляем окно

game_over = False  # Переменная-флаг, меняется, когда нажмем крестик

while game_over == False:  # Главный цикл программы
    for event in pygame.event.get():  # для каждого события
        if event.type == pygame.QUIT:  # если событие - нажатие кнопки Выход
            game_over = True
pygame.quit()  # Вне цикла выходим из игры

