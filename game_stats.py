class GameStats:
    """Checking stats in game Alien Invasion"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False  # game start in inactive status
        self.high_score = 0

    def reset_stats(self):
        """Initialized stats changing in the game time"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
