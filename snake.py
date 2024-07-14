import pygame
from constants import *


class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = (GRID_SIZE, 0)

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)

    def change_direction(self, new_direction):
        if new_direction[0] * -1 != self.direction[0] or new_direction[1] * -1 != self.direction[1]:
            self.direction = new_direction

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))