import sys
import pygame


def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True  # Переместить корабль вправо.
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True  # Переместить корабль влево.


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

