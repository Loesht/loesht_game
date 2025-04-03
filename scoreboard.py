import pygame.font
from pygame.sprite import Group

from fox import Fox

class Scoreboard():
    """Класс для вывода игровой статистики"""

    def __init__(self, sf_game):
        """Инициализирует атрибуты подсчета очков"""
        self.sf_game = sf_game
        self.screen = sf_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sf_game.settings
        self.stats = sf_game.stats

        # Настройки шрифта для вывода счета
        self.text_color = (253, 106, 2)
        self.font = pygame.font.SysFont(None, 48)

        # Подготовка изображений счетов
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_foxes()


    def prep_score(self):
        """Преобразует текущий счет в графическое изображение"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        
        self.score_image = self.font.render(score_str, True,
                    self.text_color, self.settings.bg_color)
        
        # Вывод счета в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        """Преобразует рекордный счет в графическое изображение"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                self.text_color, self.settings.bg_color)
        
        # Выравнивание по центру верхней стороны
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_level(self):
        """Преобразует уровень в графическое изображение"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                            self.text_color, self.settings.bg_color)
        
        # Уровень выводится под текущим счетом
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_foxes(self):
        """Сообщает количество оставшихся лис"""
        self.foxes = Group()
        for fox_number in range(self.stats.foxes_left):
            fox = Fox(self.sf_game)
            fox.rect.x = 10 + fox_number * fox.rect.width
            fox.rect.y = 10
            self.foxes.add(fox)


    def check_high_score(self):
        """Проверяет обновился ли рекорд"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def show_score(self):
        """Выводит счет, рекорды и уровень на экран"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.foxes.draw(self.screen)