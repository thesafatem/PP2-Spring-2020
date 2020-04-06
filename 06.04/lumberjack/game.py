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
        self.score = 0

    def show_game_over(self):
        font = pygame.font.SysFont("Arial", 36)
        text = font.render("Game over", 1, (255, 255, 255))
        place = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, place)
        pygame.display.flip()

    def show_score(self):
        font = pygame.font.SysFont("Arial", 18)
        text = font.render('Score: {}'.format(self.score), 1, (255, 255, 255))
        place = text.get_rect(center=(self.width // 2, 10))
        self.screen.blit(text, place)

    def play(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                        self.tree.descent()
                        self.lumberjack.move(self.dir[event.key])
                        self.score += 10

            if self.lumberjack.collision(self.tree):
                self.game_over = True
                self.score -= 10
                self.show_game_over()
                pygame.time.delay(2000)
                continue

            self.screen.fill((0, 0, 0))
            self.show_score()
            self.tree.draw(self.screen, self.width, self.height)
            self.lumberjack.draw(self.screen)
            pygame.display.flip()


game = Game()
game.play()

