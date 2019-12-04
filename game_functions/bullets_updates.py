import pygame
from game_functions import create_fleet


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    bullets.update()

    # Удаление пуль, вышедших за край экрана.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    # Проверка попаданий в пришельцев.
    # При обнаружении попадания удалить пулю и пришельца.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # Уничтожение существующих пуль и создание нового флота.
        bullets.empty()
        create_fleet.create_fleet(ai_settings, screen, ship, aliens)
