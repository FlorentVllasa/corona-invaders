import pygame
import os
import random
from pygame.locals import *

pygame.init()
screen_width = 1440
screen_height = 900

# Setting up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
white_house_bg = pygame.image.load(os.path.join("resources", "white-house.jpg"))

# Setting up the player
player = pygame.image.load(os.path.join("resources", "america-flag-small.jpg"))

player_x = 700
player_y = 800
player_width = 128
player_height = 71
x_changed = 0
player_speed = 0
clock = pygame.time.Clock()

# Setting up the enemy -> Corona Virus
enemy_list = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
has_moved_down_left = False
has_moved_down_right = False
num_of_enemies = 6

# Load the enemies
for index in range(num_of_enemies):
    enemy_list.append(pygame.image.load(os.path.join("resources", "virus-enemy.png")))
    enemy_x.append(random.randrange(30, 1300))
    enemy_y.append(100)
    enemy_x_change.append(random.randrange(5, 20))
    enemy_y_change.append(10)

# Load the rocket
rocket = pygame.image.load(os.path.join("resources", "rocket.png"))

enemy = pygame.image.load(os.path.join("resources", "virus-enemy.png"))

running = True


def set_player_position(x, y):
    screen.blit(player, (x, y))

while running:
    screen.blit(white_house_bg, (0, 0))
    # screen.blit(rocket, (100, 500))
    # Show Enemies on screen
    for index, enemy in enumerate(enemy_list):
        screen.blit(enemy, (enemy_x[index], enemy_y[index]))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                x_changed = -50
            elif event.key == K_RIGHT:
                x_changed = 50
            # make boundaries
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_changed = 0

    # Player movement and boundaries check
    player_x += x_changed
    if player_x > 1300:
        player_x = 1330
    elif player_x < 0:
        player_x = 0

    # Enemy movement and boundaries check
    # ToDo Implement movement so that viruses go a bit down than opposite direction !!
    for index in range(num_of_enemies):
        if has_moved_down_left:
            enemy_x[index] += enemy_x_change[index]
        elif has_moved_down_right:
            enemy_x[index] -= enemy_x_change[index]

        if enemy_x[index] < 20:
            enemy_x[index] = 50
            enemy_y[index] += enemy_y_change[index]
            has_moved_down_left = True
        elif enemy_x[index] > 1350:
            enemy_x[index] = 1300
            enemy_y[index] += enemy_y_change[index]
            has_moved_down_right = True

        enemy_x[index] -= enemy_x_change[index]



    set_player_position(player_x, player_y)

    pygame.display.update()
    clock.tick(10)

pygame.quit()
quit(0)
