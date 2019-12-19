import sys
import pygame
from game_functions.create_fleet import create_fleet
from game_functions.bullet_fire import fire_bullet



def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True  # Переместить корабль вправо.
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True  # Переместить корабль влево.
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_play_button(ai_settings, screen, stats, sb, play_button, mouse_x, mouse_y, ship, bullets, aliens):
    """Запускает новую игру при нажатии кнопки Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Сброс игровых настроек.
        ai_settings.initialize_dynamic_settings()
        """Указатель мыши скрывается"""
        pygame.mouse.set_visible(False)

        """Сброс игровой статистики."""
        stats.reset_stats()
        stats.game_active = True

        # Сброс изображений счетов и уровня.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Очистка списков пришельцев и пуль.
        aliens.empty()
        bullets.empty()

        # Создание нового флота и размещение корабля в центре.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, bullets, aliens):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, mouse_x, mouse_y, ship, bullets, aliens)


