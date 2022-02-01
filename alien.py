import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class of alien ship"""

    def __init__(self, ai_game):
        """Initialized of alien ship resources"""
        super().__init__()
        self.screen = ai_game.screen

        # downloading of image
        self.image = pygame.image.load("images\\alien.bmp")
        self.rect = self.image.get_rect()

        # every new alien spawn at left up
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # saving of x coordinate
        self.x = float(self.rect.x)
