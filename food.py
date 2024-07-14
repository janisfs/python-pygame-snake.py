import pygame
import random
from constants import *


class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        return (random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

    def respawn(self):
        self.position = self.random_position()
