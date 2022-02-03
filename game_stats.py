class GameStats:
    """Checking stats in game Alien Invasion"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialized stats changing in the game time"""
        self.ships_left = self.settings.ship_limit
