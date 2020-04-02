import pygame
import random

pygame.init()

background = pygame.image.load("background.jpg")

screen = pygame.display.set_mode((600, 800))

done = False
is_blue = True

# Player
x = 400
y = 500

enemy_x = random.randint(0, 600)
enemy_y = random.randint(50, 150)
x_enemy_change = 5
y_enemy_change = 50
playerImage = pygame.image.load("player.png")
enemyImage = pygame.image.load("enemy.png")


def player(x, y):
    screen.blit(playerImage, (x, y))


def enemy(x, y):
    screen.blit(enemyImage, (x, y))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    x_change = 0

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change -= 5
        if event.key == pygame.K_RIGHT:
            x_change += 5
    if event.type == pygame.KEYUP:
        x_change = 0

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    x += x_change
    enemy_x += x_enemy_change
    if enemy_x < 0 or enemy_x > 536:
        x_enemy_change = -x_enemy_change
        enemy_y += y_enemy_change
    player(x, y)
    enemy(enemy_x, enemy_y)
    pygame.display.flip()
