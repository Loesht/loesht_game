import sys

import pygame

from settings import Settings
from fox import Fox
from bullet import Bullet

class SnowFox:
    """Класс для управления ресурсами и поведением игры"""

    def __init__ (self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()

        # Назначение цвета фона
        self.bg_color = (214, 234, 236)

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Snow Fox")
        self.fox = Fox(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self.fox.update()
            self.bullets.update()
            self._update_screen()


    def _check_events(self):
        """Обрабатывает нажатия клавишь и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:
            self.fox.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.fox.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.fox.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.fox.moving_left = False


    def _fire_bullet(self):
        """Создание нового снаряда-снежка и включение его в группу bullets."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)
        self.fox.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра игры и ее запуск.
    sf = SnowFox()
    sf.run_game()