import pygame

pygame.init()


class Game:
    screen = pygame.display.set_mode((500, 500))
    game_over = False
    number = 0

    def draw(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont("Arial", 72)
        text = font.render(str(self.number), 1, (255, 255, 255))
        place = text.get_rect(center=(250, 250))
        self.screen.blit(text, place)
        pygame.display.flip()

    def play(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.number -= 1
                    elif event.key == pygame.K_RIGHT:
                        self.number += 1

            self.draw()


game = Game()
game.play()