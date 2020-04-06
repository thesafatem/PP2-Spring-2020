import pygame
from tree import Tree
from lumberjack import Lumberjack


class Game:
    width = 300
    height = 500
    dir = {
        pygame.K_LEFT: -1,
        pygame.K_RIGHT: 1
    }

    def __init__(self):
        pygame.font.init()
        self.game_over = False
        self.tree = Tree()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.lumberjack = Lumberjack()

    def play(self):
        while not self.game_over:
		???


game = Game()
game.play()

