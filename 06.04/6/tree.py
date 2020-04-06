import random
import pygame


class Tree:
    tree = []
    height = 12
    trunk = (160, 82, 45)
    leaf = (58, 95, 11)

    def __init__(self):
        for i in range(3):
            self.tree.append([False, False])
        for i in range(self.height - 3):
            self.generate()

    def generate(self):
        side = random.randint(0, 1)
        self.tree.append([side == 0, side == 1])

    def draw(self, screen, width, height):
        sx = width // 2 - 15
        sy = height // 2 - 180
        pygame.draw.rect(screen, self.trunk, (sx, sy, 30, 360))
        for i in range(self.height - 1, -1, -1):
            if self.tree[i][0]:
                pygame.draw.rect(screen, self.leaf, (sx - 70, sy + (self.height - i - 1) * 30 + 8, 70, 14))
            if self.tree[i][1]:
                pygame.draw.rect(screen, self.leaf, (sx + 30, sy + (self.height - i - 1) * 30 + 8, 70, 14))

    def descent(self):
        for i in range(self.height - 1):
            self.tree[i] = self.tree[i + 1]
        self.tree.pop(self.height - 1)
        self.generate()