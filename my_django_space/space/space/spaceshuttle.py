import pygame
import math

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Определение размеров экрана
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1333

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rocket Launch")

# Загрузка изображений планет и ракеты
planet1_image = pygame.image.load("images/saturn.png").convert_alpha()
planet2_image = pygame.image.load("images/earth.png").convert_alpha()
rocket_image = pygame.image.load("images/spaceship.png").convert_alpha()
rocket_image = pygame.transform.scale(rocket_image, (100, 100))

# Определение начальной и конечной позиции ракеты
rocket_x = 100
rocket_y = SCREEN_HEIGHT - 300
target_x = SCREEN_WIDTH
target_y = 50

# Определение начальной скорости и ускорения ракеты
velocity = 0
acceleration = 0.1

# Определение угла между ракетой и целью
angle = math.atan2(target_y - rocket_y, target_x - rocket_x)

# Основной цикл программы
done = False
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Очистка экрана
    screen.fill(BLACK)

    # Отрисовка планет
    screen.blit(planet1_image, (700, SCREEN_HEIGHT - 1300))
    screen.blit(planet2_image, (SCREEN_WIDTH - 2200, 550))

    # Отрисовка ракеты
    rotated_rocket_image = pygame.transform.rotate(rocket_image, math.degrees(angle))
    screen.blit(rotated_rocket_image, (rocket_x, rocket_y))

    # Обновление позиции ракеты
    velocity += acceleration
    rocket_x += velocity * math.cos(angle)
    rocket_y += velocity * math.sin(angle)

    # Проверка, достигла ли ракета цели
    distance_to_target = math.sqrt((target_x - rocket_x) ** 2 + (target_y - rocket_y) ** 2)
    if distance_to_target < 10:
        done = True

    # Обновление экрана
    pygame.display.flip()

# Завершение Pygame
pygame.quit()
