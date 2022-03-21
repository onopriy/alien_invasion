import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class of alien ship"""

    def __init__(self, ai_game):
        """Initialized of alien ship resources"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # downloading of image
        self.image = pygame.image.load("images\\alien.bmp")
        self.rect = self.image.get_rect()

        # every new alien spawn at left up
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # saving of x coordinate
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move alien right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is located at edge (left/right)"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            return True
