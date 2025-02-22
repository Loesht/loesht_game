import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления снарядами-снежками, брошенными лисой"""
    def __init__(self, sf_game):
        super().__init__()
        self.screen = sf_game.screen
        self.settings = sf_game.settings
        self.color = self.settings.bullet_color

        # Инициализация позиции снаряда-снежка
        self.radius = self.settings.bullet_radius
        self.x = float(sf_game.fox.rect.centerx)
        self.y = float(sf_game.fox.rect.top)


    def update(self):
        """Перемещает снаряд-снежок вверх по экрану"""
        # Обновление позиции снаряда в вещественном формате
        self.y -= self.settings.bullet_speed
        # Обновление позиции круга
        if self.y <= 0:
            self.kill()


    def draw_bullet(self):
        """Вывод снаряда на экран"""
        pygame.draw.circle(
            self.screen, self.color, (int(self.x), int(self.y)), self.radius)