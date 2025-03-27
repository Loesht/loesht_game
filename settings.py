class Settings():
    """Класс для хранения всех настроек игры Snow Fox"""

    def __init__(self):
        """Инициализирует статические настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (214, 234, 236)

        # Настройки модели лисы
        #self.fox_speed = 1.5
        self.fox_limit = 3

        # Параметры снаряда-снежка
        #self.bullet_speed = 1.5
        self.bullet_radius = 20
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3

        # Настройки медведей
        #self.bear_speed = 1.5
        self.flock_drop_speed = 10

        # Темп ускорения игры
        self.initialize_dynamic_settings()
        self.speedup_scale = 1.1
        


    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.fox_speed = 1.5
        self.bullet_speed = 3.0
        self.bear_speed = 1.0

        # flock_direction = 1 - движение вправо; -1 - влево
        self.flock_direction = 1


    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.fox_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.bear_speed *= self.speedup_scale