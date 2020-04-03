from random import randrange as rand
import pygame

from point import Point


class Fruit:
    color = (0, 255, 0)
    radius = 10

    def __init__(self, snake, width, height):
        self.position = self.generate(snake, width, height)

    def generate(self, snake, width, height):
        ok = False
        while not ok:
            ok = True
            x = rand(snake.radius, width - snake.radius, 2 * snake.radius)
            y = rand(snake.radius, height - snake.radius, 2 * snake.radius)
            for snakey in snake.snake:
                if x == snakey.x and y == snakey.y:
                    ok = False
                    break
        return Point(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.to_pair(), self.radius)

