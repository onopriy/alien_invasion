import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for controll shooting of ship"""

    def __init__(self, ai_example):
        """Creating of projectile in currently position of ship"""
        super().__init__()
        self.screen = ai_example.screen
        self.settings = ai_example.settings
        self.color = self.settings.bullet_color

        # creating of projectile in position (0, 0) and appointment in the right position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_example.ship.rect.midtop

        # position in float
        self.y = float(self.rect.y)

    def update(self):
        """Moving projectile up"""
        self.y -= self.settings.bullet_speed  # new position of bullet in float format
        self.rect.y = self.y  # update position of rectangle(projectile)

    def draw_bullet(self):
        """Draw bullet on surface"""
        pygame.draw.rect(self.screen, self.color, self.rect)
