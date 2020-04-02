import pygame
from snake import Snake
from fruit import Fruit


class Game:
    def __init__(self):
        self.game_over = False
        self.width = 500
        self.height = 500
        self.status_height = 15
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.FPS = 10
        self.snake = Snake(self.width, self.height, self.status_height)
        self.fruit = Fruit(self.snake, self.width, self.height, self.status_height)
        self.direction = 3
        self.dir = {
            pygame.K_LEFT: 0,
            pygame.K_UP: 1,
            pygame.K_RIGHT: 2,
            pygame.K_DOWN: 3
        }
        self.score = 0
        self.level = 1

    def show_game_over(self):
        pygame.font.init()
        self.game_over = True
        font1 = pygame.font.SysFont("Arial", 36)
        text1 = font1.render("Game Over", 1, (255, 255, 255))
        place1 = text1.get_rect(center=(self.width // 2, self.height // 2 - 20))
        font2 = pygame.font.SysFont("Arial", 18)
        text2 = font2.render('Score: {}'.format(self.score), 1, (255, 255, 255))
        place2 = text2.get_rect(center=(self.width // 2, self.height // 2 + 10))
        self.screen.blit(text1, place1)
        self.screen.blit(text2, place2)
        pygame.display.flip()

    def show_status(self):
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 14)
        text = font.render('Snake Game by @thesafatem', 1, (255, 255, 255))
        place = text.get_rect(center=(self.width // 2, 8))
        text1 = font.render('Level: {}'.format(self.level), 1, (255, 255, 255))
        place1 = text1.get_rect(center=(self.width // 2 + 150, 8))
        text2 = font.render('Score: {}'.format(self.score), 1, (255, 255, 255))
        place2 = text2.get_rect(center=(self.width // 2 + 200, 8))
        self.screen.blit(text, place)
        self.screen.blit(text1, place1)
        self.screen.blit(text2, place2)

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
                        self.direction = self.dir[event.key]

            self.snake.move(self.direction, self.width, self.height, self.status_height)

            if self.snake.collision():
                self.show_game_over()
                pygame.time.delay(3000)
                continue

            if self.snake.eat(self.fruit):
                self.fruit = Fruit(self.snake, self.width, self.height, self.status_height)
                self.score += 10
                if len(self.snake.snake) % 5 == 0:
                    self.level += 1
                    self.FPS += 10

            self.screen.fill((0, 0, 0))
            self.screen.fill((0, 0, 255), (0, 0, self.width, 15))
            self.show_status()
            self.fruit.draw(self.screen)
            self.snake.draw(self.screen)
            pygame.display.flip()

