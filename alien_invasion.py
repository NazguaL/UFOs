import sys
import time
import pygame


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("UFOs")
    # Запуск основного цикла игры.

    while True:
        time.sleep(0.05)
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Отображение прорисованного экрана.
        pygame.display.flip()

if __name__ == "__main__":
    run_game()
