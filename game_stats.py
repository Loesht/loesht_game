class GameStats():
    """Отслеживание статистики игры Snow Fox"""

    def __init__(self, sf_game):
        """Инициализирует статистику"""
        self.settings = sf_game.settings
        self.reset_stats()

        # Игра запускается в активном состоянии
        self.game_active = False


    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.foxes_left = self.settings.fox_limit
