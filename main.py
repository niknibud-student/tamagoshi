import pygame  # импортируем библиотеку

BLUE = (175, 226, 207)  # Цвет фона в формате RGB

window = pygame.display.set_mode((500, 400))  # Создаем окно 500 на 400
pygame.display.set_caption('Симулятор жизни')  # Устанавливаем заголовок

# Загружаем картинку
cornmen_image = pygame.image.load("hero.png").convert_alpha()
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

