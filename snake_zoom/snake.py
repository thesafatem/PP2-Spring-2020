import pygame
from random import randrange as rand

from point import Point


class Snake:
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    radius = 10
    color = (255, 0, 0)
    is_grow = False

    def __init__(self, width, height):
        self.snake = [Point(rand(self.radius, width - self.radius, 2 * self.radius),
                            rand(self.radius, height - self.radius, 2 * self.radius))]

    def move(self, direction, width, height):
        if self.is_grow:
            self.is_grow = False
            self.snake.append(Point(0, 0))

        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].x = self.snake[i - 1].x
            self.snake[i].y = self.snake[i - 1].y
        self.snake[0].x += self.dx[direction] * 2 * self.radius
        self.snake[0].y += self.dy[direction] * 2 * self.radius
        self.snake[0].x = (self.snake[0].x + width) % width
        self.snake[0].y = (self.snake[0].y + height) % height

    def collision(self):
        for i in range(1, len(self.snake)):
            if self.snake[0].x == self.snake[i].x and self.snake[0].y == self.snake[i].y:
                return True
        return False

    def eat(self, fruit):
        # if self.snake[0] == fruit.position: WRONG
        if self.snake[0].x == fruit.position.x and self.snake[0].y == fruit.position.y:
            self.is_grow = True
            return True
        return False


    def draw(self, screen):
        for snakey in self.snake:
            pygame.draw.circle(screen, self.color, snakey.to_pair(), self.radius)
