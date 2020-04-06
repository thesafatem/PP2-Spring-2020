import pygame
import random

dx = [-1, 1, 1, -1]
dy = [-1, -1, 1, 1]
direction = 0

width = 600
height = 300
radius = 10

screen = pygame.display.set_mode((width, height))

x = random.randrange(radius, width - radius, 2 * radius)
y = random.randrange(radius, height - radius, 2 * radius)

clock = pygame.time.Clock()

game_over = False

while not game_over:
    clock.tick(1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            break

    x2 = x + dx[direction]
    y2 = y + dy[direction]
    if x2 == 0:
        if direction == 0:
            direction = 1
        else:
            direction = 2
    elif x2 == width:
        if direction == 1:
            direction = 0
        else:
            direction = 3
    elif y2 == 0:
        if direction == 0:
            direction = 3
        else:
            direction = 2
    elif y2 == height:
        if direction == 3:
            direction = 0
        else:
            direction = 1
    else:
        x = x2
        y = y2

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.display.flip()
