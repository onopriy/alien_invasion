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
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start of main game's loop"""
        while True:
            self._check_event()  # checking keyboard and mouse
            self.ship.update()  # update of ship position
            self._update_screen()

    def _check_event(self):
        """Checking user's mouse and keyboard"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Check user down key"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Check user up key"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update of screen"""
        self.screen.fill(self.settings.background_color)  # redrawing surface in putting color
        self.ship.blitme()  # image of ship
        pygame.display.flip()  # show last frame


if __name__ == '__main__':
    # creating example of game:
    ai = AlienInvasion()
    ai.run_game()
