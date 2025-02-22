import pygame
from pygame.sprite import Sprite

class Bear(Sprite):
    """Класс, представляющий одного пришельца"""

    def __init__(self, sf_game):
        """Инициализирует пришельца и создает его начальную позицию"""
        super().__init__()
        self.screen = sf_game.screen

        # Загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('images/bear.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в верхнем левом углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)