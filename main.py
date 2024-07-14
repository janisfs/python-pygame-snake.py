import pygame
import sys
from constants import *
from snake import Snake
from food import Food

# ... (предыдущий код остается без изменений)


def main():
    snake = Snake()
    food = Food()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -GRID_SIZE))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, GRID_SIZE))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-GRID_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((GRID_SIZE, 0))

        # Обновление состояния игры
        snake.move()

        # Проверка столкновения с едой
        if snake.body[0] == food.position:
            snake.grow()
            food = Food()

        # Очистка экрана
        screen.fill(BLACK)

        # Отрисовка игровых объектов
        snake.draw(screen)
        food.draw(screen)

        # Обновление экрана
        pygame.display.flip()

        # Ограничение FPS
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()