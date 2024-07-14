import pygame
import random
from constants import *


class Food:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        x = random.randint(0, (SCREEN_WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        return (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))