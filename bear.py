import pygame
from pygame.sprite import Sprite

class Bear(Sprite):
    """Класс, представляющий одного медведя"""

    def __init__(self, sf_game):
        """Инициализирует медведя и создает его начальную позицию"""
        super().__init__()
        self.screen = sf_game.screen
        self.settings = sf_game.settings

        # Загрузка изображения медведя и назначение атрибута rect
        self.image = pygame.image.load('images/bear.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый медведь появляется в верхнем левом углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции медведя
        self.x = float(self.rect.x)


    def check_edges(self):
        """Возвращает True, если медведь находится у границы экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


    def update(self):
        """Перемещает медведя вправо или влево"""
        self.x += self.settings.bear_speed * self.settings.flock_direction
        self.rect.x = self.x 

