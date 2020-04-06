import random
import pygame


class Lumberjack:
    color = (255, 0, 0)

    def __init__(self):
        self.position = random.randint(0, 1)
        self.y = 410
        self.x = 150 + int(self.position == 1) * 25 - int(self.position == 0) * 35

    def move(self, direction):
        self.position += direction
        if self.position in (-1, 2):
            self.position = (self.position + 1) % 2
        self.x = 150 + int(self.position == 1) * 25 - int(self.position == 0) * 35

    def collision(self, tree):
        return tree.tree[0][self.position]

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 10, 20))