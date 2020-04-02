import pygame
import random
from point import Point


class Snake:
    def __init__(self, width, height, status_height):
        self.dx = [-1, 0, 1, 0]
        self.dy = [0, -1, 0, 1]
        self.radius = 5
        self.color = (255, 0, 0)
        self.grow = False
        x_range = width - 2 * self.radius
        y_range = height - 2 * self.radius - status_height
        x = random.randint(0, x_range // (2 * self.radius))
        y = random.randint(0, y_range // (2 * self.radius))
        x = self.radius * (2 * x + 1)
        y = self.radius * (2 * y + 1) + status_height
        self.snake = [Point(x, y)]

    def draw(self, screen):
        for circle in self.snake:
            pygame.draw.circle(screen, self.color, circle.draw(), self.radius)

    def move(self, direction, width, height, status_height):
        if self.grow:
            self.grow = False
            self.snake.append(Point(5, 5))
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].x = self.snake[i - 1].x
            self.snake[i].y = self.snake[i - 1].y
        self.snake[0].x += self.dx[direction] * 2 * self.radius
        self.snake[0].y += self.dy[direction] * 2 * self.radius
        self.snake[0].x = (self.snake[0].x + width) % width
        self.snake[0].y = (self.snake[0].y + height) % height
        if direction == 3:
            self.snake[0].y = max(self.snake[0].y, status_height + self.radius)
        if direction == 1:
            self.snake[0].y = max(self.snake[0].y, (self.snake[0].y - status_height) % height)

    def collision(self):
        for i in range(1, len(self.snake)):
            if self.snake[0].x == self.snake[i].x and self.snake[0].y == self.snake[i].y:
                return True
        return False

    def eat(self, fruit):
        self.grow = (self.snake[0].x == fruit.position.x and self.snake[0].y == fruit.position.y)
        return self.grow



