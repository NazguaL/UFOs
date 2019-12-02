import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, представляющий одного пришельца."""

    def __init__(self, ai_settings, screen):
        """Инициализирует пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load('images/ufo.png')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение позиции пришельца в вещественном формате.
        self.x = float(self.rect.x)

    def blitme(self):
        """Выводит пришельца в текущем положении."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        # print("Checked!!!")

    def update(self):
        """Перемещает пришельца."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        print("ai_settings.alien_speed_factor: " + str(self.ai_settings.alien_speed_factor))
        print("ai_settings.alien_fleet_direction: " + str(self.ai_settings.fleet_direction))
        print("Alien's rect.y: " + str(self.rect.y))
        self.rect.x = self.x
