import pygame
from time import sleep
from game_functions import create_fleet


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Обрабатывает столкновение корабля с пришельцем."""
    # Уменьшение ships_left.
    if stats.ships_left > 0:
        stats.ships_left -= 1

        # Очистка списков пришельцев и пуль.
        aliens.empty()
        bullets.empty()

        # Создание нового флота и размещение корабля в центре.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Пауза.
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
