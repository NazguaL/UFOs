import pygame


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    screen.fill(ai_settings.bg_color)

    # Все пули выводятся позади изображений корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Кнопка Play отображается в том случае, если игра неактивна.
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()
