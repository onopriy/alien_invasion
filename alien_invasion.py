import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class for control of game resources and behavior of game"""

    def __init__(self):
        """Initialized of game and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start of main game's loop"""
        while True:
            # checking keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.background_color)  # redrawing surface in putting color
            self.ship.blitme()
            pygame.display.flip()  # show last frame


if __name__ == '__main__':
    # creating example of game:
    ai = AlienInvasion()
    ai.run_game()
