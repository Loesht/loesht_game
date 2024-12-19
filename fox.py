import pygame

class Fox():
    """Класс для управления моделью лисы"""

    def __init__(self, sf_game):
        """Инициализирует модель лисы и задает ее начальное положение"""
        self.screen = sf_game.screen
        self.settings = sf_game.settings
        self.screen_rect = self.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/fox_icon.bmp')
        self.rect = self.image.get_rect()

        # Каждая новая модель лисы появляется у нижней части экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра модели лисы
        self.x = float(self.rect.x)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Обновляет позицию лисы с учетом флагов"""
        # Обновляется атрибут x, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.fox_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.fox_speed

        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x


    def blitme(self):
        """Рисует модель лисы в текущей позиции"""
        self.screen.blit(self.image, self.rect)