import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from fox import Fox
from bullet import Bullet
from bear import Bear

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

        self.bears = pygame.sprite.Group()
        self._create_flock()


    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self.fox.update()
            self.bullets.update()
            self._check_flock_edges()
            self.bears.update()
            self._update_bullets()
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


    def _update_bullets(self):
         # Удаление снарядов при выходе за пределы экрана 
        for bullet in self.bullets.copy():
            if bullet.y <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_bear_collision()


    def _check_bullet_bear_collision(self):
        """Обработка коллизии нарядов с медведями"""
        # При попадании удалить снаряд и медведя
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.bears, True, True) 
        
         # Проверка коллизий медведя и лисы
        if pygame.sprite.spritecollide(self.fox, self.bears, 
                                       dokill=True):
            print("Fox hit!!!")
        
        # Уничтожение снарядов и создание новой стаи
        if not self.bears:
            self.bullets.empty()
            self._create_flock() 


    def _create_flock(self):
        """Создание стаи медведей"""
        # Создание медведя и вычисление кол-ва медведей в ряду
        # Интервал между соседними медвеями равен ширине медведя
        bear = Bear(self)
        bear_width, bear_height = bear.rect.size
        available_space_x = self.settings.screen_width - (2 * bear_width)
        number_bear_x = available_space_x // (2 * bear_width)

        """Определяет кол-во рядов, помещающихся на экране"""
        fox_height = self.fox.rect.height
        available_space_y = (self.settings.screen_height - 
                             (3 * bear_height) - fox_height)
        number_rows = available_space_y // (2 * fox_height)

        # Создание стаи
        for row_number in range(number_rows):
            for bear_number in range(number_bear_x):
                self._create_bear(bear_number, row_number)


    def _create_bear(self, bear_number, row_number):
        # Создание медведя и его размещение в ряду
        bear = Bear(self)
        bear_width, bear_height = bear.rect.size
        bear.x = bear_width + 2 * bear_width * bear_number
        bear.rect.x = bear.x
        bear.rect.y = bear.rect.height + 2 * bear.rect.height * row_number
        self.bears.add(bear)


    def _check_flock_edges(self):
        """Реагирует на достижение медведем  края экрана"""
        for bear in self.bears.sprites():
            if bear.check_edges():
                self._change_flock_direction()
                break


    def _change_flock_direction(self):
        """Опускает всю стаю и меняет направление движения флота"""
        for bear in self.bears.sprites():
            bear.rect.y += self.settings.flock_drop_speed
        self.settings.flock_direction *= -1


    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)
        self.fox.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.bears.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра игры и ее запуск.
    sf = SnowFox()
    sf.run_game()