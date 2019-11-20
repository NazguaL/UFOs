import sys
import time
import pygame
from settings import Settings
from ship import Ship


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.window_name)
    bg_color = ai_settings.bg_color

    # Создание корабля.
    ship = Ship(screen)

    # Запуск основного цикла игры.
    while True:
        time.sleep(0.05)
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Отображение прорисованного экрана при каждом проходе цикла.
        screen.fill(bg_color)
        ship.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    run_game()


