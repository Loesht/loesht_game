class Settings():
    """Класс для хранения всех настоек игру Snow Fox"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (214, 234, 236)

        # Настройки модели лисы
        self.fox_speed = 1.5
        self.fox_limit = 3

        # Параметры снаряда
        self.bullet_speed = 1.5
        self.bullet_radius = 20
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3

        # Настройки медведей
        self.bear_speed = 5
        self.flock_drop_speed = 10
        # flock_direction = 1 движение вправо, -1 движение влево
        self.flock_direction = 1
