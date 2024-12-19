import sys

import pygame

from settings import Settings
from fox import Fox

class SnowFox:
    """Класс для управления ресурсами и поведением игры"""

    def __init__ (self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()
        

        # Назначение цвета фона
        self.bg_color = (214, 234, 236)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snow Fox")
        self.fox = Fox(self)
        

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        """Обрабатывает нажатия клавишь и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)
        self.fox.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра игры и ее запуск.
    sf = SnowFox()
    sf.run_game()