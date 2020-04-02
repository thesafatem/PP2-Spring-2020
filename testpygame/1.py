import pygame
import random

pygame.init()


class Entity:
    def __init__(self, x, y, dx, dy, image_path):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.image = pygame.image.load(image_path)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def blit(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def collision(self, entity):
        lx1 = self.x
        rx1 = self.x + self.image.get_size()[0]
        ty1 = self.y
        by1 = self.y + self.image.get_size()[1]
        lx2 = entity.x
        rx2 = entity.x + entity.image.get_size()[0]
        ty2 = entity.y
        by2 = entity.y + entity.image.get_size()[1]
        lx = max(lx1, lx2)
        rx = min(rx1, rx2)
        ty = max(ty1, ty2)
        by = min(by1, by2)
        return lx <= rx and ty <= by


class Player(Entity):
    def normalize(self, width):
        self.x = (self.x + width) % width

    def shoot(self):
        bullet = Bullet(random.randint(0, 600), random.randint(100, 500), 0, -5, "bullet.png")
        player_center_x = self.x + self.image.get_size()[0] // 2
        bullet_x = player_center_x - bullet.image.get_size()[0] // 2
        bullet_y = self.y - bullet.image.get_size()[1]
        bullet.x = bullet_x
        bullet.y = bullet_y
        return bullet


class Enemy(Entity):
    def descent(self, width):
        if self.x < 0 or self.x + self.image.get_size()[0] > width:
            self.dx = -self.dx
            self.y += 50


class Bullet(Entity):
    pass


class Game:
    game_over = False
    width = 600
    height = 600
    background = pygame.image.load("background.jpg")
    screen = pygame.display.set_mode((width, height))
    player = Player(random.randint(0, 530), 530, 5, 0, "player.png")
    enemy = Enemy(random.randint(0, 530), 0, 5, 0, "enemy.png")
    is_shot = False
    bullets = []

    def play(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.dx = -abs(self.player.dx)
                    self.player.move()
                if event.key == pygame.K_RIGHT:
                    self.player.dx = abs(self.player.dx)
                    self.player.move()
                if event.key == pygame.K_SPACE:
                    self.is_shot = True

            if event.type == pygame.KEYUP:
                if self.is_shot:
                    self.is_shot = False
                    self.bullets.append(self.player.shoot())

            for bullet in self.bullets:
                bullet.move()
                if self.enemy.collision(bullet):
                    self.bullets.remove(bullet)
                    self.enemy = Enemy(random.randint(0, 530), 0, 5, 0, "enemy.png")
                    continue

            if self.enemy.collision(self.player):
                font = pygame.font.SysFont("Arial", 36)
                text = font.render("Game over", 1, (255, 255, 255))
                place = text.get_rect(center=(300, 300))
                self.screen.blit(text, place)
                pygame.display.flip()
                self.game_over = True
                pygame.time.delay(2000)
                continue

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, (0, 0))

            self.enemy.move()
            self.enemy.descent(self.width)
            self.player.normalize(self.width)

            for bullet in self.bullets:
                bullet.blit(self.screen)

            self.player.blit(self.screen)
            self.enemy.blit(self.screen)

            pygame.display.flip()


game = Game()
game.play()
