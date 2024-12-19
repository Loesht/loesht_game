import pygame

class Fox():
    """Класс для управления моделью лисы"""

    def __init__(self, sf_game):
        """Инициализирует модель лисы и задает ее начальное положение"""
        self.screen = sf_game.screen
        self.screen_rect = self.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/fox_icon.bmp')
        self.rect = self.image.get_rect()

        # Каждая новая модель лисы появляется у нижней части экрана
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует модель лисы в текущей позиции"""
        self.screen.blit(self.image, self.rect)