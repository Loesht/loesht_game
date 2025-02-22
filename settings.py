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

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_radius = 10
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3