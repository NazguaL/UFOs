import pygame


class Ship():

    def __init__(self, screen):
        self.screen = screen #Инициализирует корабль и задает его начальную позицию.

        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('images/starship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect) #Рисует корабль в текущей позиции.