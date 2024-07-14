import pygame
import sys
from constants import *

# Инициализация Pygame
pygame.init()

# Создание игрового окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Создание объекта часов для управления FPS
clock = pygame.time.Clock()


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Здесь будет обновление игрового состояния

        # Очистка экрана
        screen.fill(BLACK)

        # Здесь будет отрисовка игровых объектов

        # Обновление экрана
        pygame.display.flip()

        # Ограничение FPS
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()