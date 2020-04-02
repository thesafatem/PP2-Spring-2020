import pygame
import random
from point import Point


class Fruit:
    def __init__(self, snake, width, height, status_height):
        self.color = (0, 255, 0)
        self.radius = snake.radius
        self.position = self.generate(snake, width, height, status_height)

    def generate(self, snake, width, height, status_height):
        collision = True
        x_range = width - 2 * self.radius
        y_range = height - 2 * self.radius - status_height
        while collision:
            collision = False
            x = random.randint(0, x_range // (2 * self.radius))
            y = random.randint(0, y_range // (2 * self.radius))
            x = self.radius * (2 * x + 1)
            y = self.radius * (2 * y + 1) + status_height
            for circle in snake.snake:
                if x == circle.x and y == circle.y:
                    collision = True
                    break;
        return Point(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.draw(), self.radius)


