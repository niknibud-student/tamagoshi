import pygame  # импортируем библиотеку

window = pygame.display.set_mode((500, 400))  # Создаем окно 500 на 400
pygame.display.set_caption('Симулятор жизни')  # Устанавливаем заголовок
game_over = False  # Переменная-флаг, меняется, когда нажмем крестик

while game_over == False:  # Главный цикл программы
    for event in pygame.event.get():  # для каждого события
        if event.type == pygame.QUIT:  # если событие - нажатие кнопки Выход
            game_over = True
pygame.quit()  # Вне цикла выходим из игры

