import random
import pygame

pygame.init()


class Entity:
    def __init__(self, x, y, dx, dy, image_path):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.image = pygame.image.load(image_path)

    def blit(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def collision(self, entity):
        lx1 = self.x
        lx2 = entity.x
        rx1 = self.x + self.image.get_size()[0]
        rx2 = entity.x + entity.image.get_size()[0]
        ty1 = self.y
        ty2 = entity.y
        by1 = self.y + self.image.get_size()[1]
        by2 = entity.y + entity.image.get_size()[1]
        lx = max(lx1, lx2)
        rx = min(rx1, rx2)
        ty = max(ty1, ty2)
        by = min(by1, by2)
        if lx <= rx and ty <= by:
            return True
        return False


class Player(Entity):
    def normalize(self, width):
        if self.x < 0 or self.x > width:
            self.x = (self.x + width) % width

    def shoot(self):
        bullet = Bullet(200, 200, 0, -5, "bullet.png")
        px = self.x + self.image.get_size()[0] // 2
        bx = px - bullet.image.get_size()[0] // 2
        by = self.y - bullet.image.get_size()[1]
        bullet.x = bx
        bullet.y = by
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
    is_bullet = False
    kills = 0
    width = 600
    height = 600
    background = pygame.image.load("background.jpg")
    screen = pygame.display.set_mode((width, height))
    player = Player(random.randint(0, width - 70), 530, 5, 0, "player.png")
    enemy = Enemy(random.randint(0, width - 70), 0, 5, 0, "enemy.png")
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
                    self.is_bullet = True

            if event.type == pygame.KEYUP:
                if self.is_bullet:
                    self.bullets.append(self.player.shoot())
                self.is_bullet = False

            self.enemy.move()
            self.enemy.descent(self.width)
            self.player.normalize(self.width)

            for bullet in self.bullets:
                if bullet.collision(self.enemy):
                    self.enemy = Enemy(random.randint(0, self.width - 70), 0, 5, 0, "enemy.png")
                    self.bullets.remove(bullet)
                    self.kills += 1

            for bullet in self.bullets:
                bullet.move()

            if self.enemy.collision(self.player):
                self.game_over = True
                font = pygame.font.SysFont("Arial", 36)
                text = font.render("Game Over \nKills: " + str(self.kills), 1, (255, 255, 255))
                place = text.get_rect(center=(self.width // 2, self.height // 2))
                self.screen.blit(text, place)
                pygame.display.flip()
                pygame.time.delay(2000)
                continue

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, (0, 0))
            self.player.blit(self.screen)
            self.enemy.blit(self.screen)
            font = pygame.font.SysFont("Arial", 18)
            text = font.render("Kills: " + str(self.kills), 1, (255, 255, 255))
            place = text.get_rect(center=(50, 580))
            self.screen.blit(text, place)

            for bullet in self.bullets:
                bullet.blit(self.screen)

            pygame.display.flip()


game = Game()
game.play()