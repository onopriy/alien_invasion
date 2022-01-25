class Settings:
    """Class for settings in Alien Invasion"""

    def __init__(self):
        """Initialized game settings"""
        self.screen_width = 800
        self.screen_height = 600
        self.background_color = (230, 230, 230)
        self.speed = 0.75
        # bullet parameters
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
