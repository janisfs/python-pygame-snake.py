import pygame
import sys
from snake import Snake
from food import Food
from constants import *
import time


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')

    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    score = 0
    start_time = time.time()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_direction((-GRID_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((GRID_SIZE, 0))
                elif event.key == pygame.K_UP:
                    snake.change_direction((0, -GRID_SIZE))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, GRID_SIZE))

        try:
            snake.move()
        except Exception as e:
            print(e)
            running = False

        # Проверка на столкновение змейки с едой
        if snake.body[0] == food.position:
            snake.grow()
            food.respawn()

        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)

        # Отображение счётчика времени и продуктов
        font = pygame.font.Font(None, 36)
        elapsed_time = time.time() - start_time
        time_text = font.render(f"Time: {int(elapsed_time)}s", True, WHITE)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(time_text, (10, 10))
        screen.blit(score_text, (10, 50))

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
