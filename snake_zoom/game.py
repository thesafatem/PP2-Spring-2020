import pygame

from snake import Snake
from fruit import Fruit

class Game:
    width = 500
    height = 500
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    FPS = 10
    dir = {
        pygame.K_LEFT: 0,
        pygame.K_UP: 1,
        pygame.K_RIGHT: 2,
        pygame.K_DOWN: 3
    }

    def __init__(self):
        self.game_over = False
        self.snake = Snake(self.width, self.height)
        self.fruit = Fruit(self.snake, self.width, self.height)
        self.direction = 3
        self.score = 0

    def play(self):
        while not self.game_over:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_over = True
                        break
                    if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP):
                        if abs(self.direction - self.dir[event.key]) != 2 or len(self.snake.snake) == 1:
                            self.direction = self.dir[event.key]

            self.snake.move(self.direction, self.width, self.height)

            if self.snake.collision():
                self.game_over = True
                pygame.font.init()
                font = pygame.font.SysFont("Arial", 36)
                text = font.render("Game over", 1, (255, 255, 255))
                place = text.get_rect(center=(self.width // 2, self.height // 2 - 20))
                font2 = pygame.font.SysFont("Arial", 18)
                text2 = font2.render('Score: {}'.format(self.score), 1, (255, 255, 255))
                place2 = text2.get_rect(center=(self.width // 2, self.height // 2 + 10))
                self.screen.blit(text, place)
                self.screen.blit(text2, place2)
                pygame.display.flip()
                pygame.time.delay(2000)
                continue

            if self.snake.eat(self.fruit):
                self.fruit = Fruit(self.snake, self.width, self.height)
                self.score += 10
                if len(self.snake.snake) % 5 == 0:
                    self.FPS += 10

            self.screen.fill((0, 0, 0))
            self.fruit.draw(self.screen)
            self.snake.draw(self.screen)
            pygame.display.flip()