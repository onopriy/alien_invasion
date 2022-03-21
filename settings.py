class Settings:
    """Class for settings in Alien Invasion"""

    def __init__(self):
        """Initialized game settings"""
        self.screen_width = 800
        self.screen_height = 600
        self.background_color = (230, 230, 230)
        self.speed = 0.75
        self.ship_limit = 3
        # bullet parameters
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1
        self.score_scale = 1.5  # growth rate of score per alien

        self.initialized_dynamic_settings()

    def initialized_dynamic_settings(self):
        self.speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.alien_points = 50

        # fleet_direction = 1 mean left move, -1 it's right move
        self.fleet_direction = 1

    def increase_speed(self):
        """Increment settings of speed"""
        self.speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
