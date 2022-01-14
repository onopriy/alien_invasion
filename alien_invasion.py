import sys
import pygame


class AlienInvasion:
    """Class for control of game resources and behavior of game"""

    def __init__(self):
        """Initialized of game and create game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start of main game's loop"""
        while True:
            # checking keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()  # show last frame


if __name__ == '__main__':
    # creating example of game:
    ai = AlienInvasion()
    ai.run_game()

