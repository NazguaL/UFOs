import time
import pygame
from settings import Settings
from ship import Ship
from game_functions import *


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.window_name)
    # bg_color = ai_settings.bg_color

    ship = Ship(screen)  # Создание корабля.

    # Запуск основного цикла игры.
    while True:
        time.sleep(0.05)  # уменьшение загрузки ЦП
        # Отслеживание событий клавиатуры и мыши.
        check_events()
        # Отображение прорисованного экрана при каждом проходе цикла.
        update_screen(ai_settings, screen, ship)

if __name__ == "__main__":
    run_game()


