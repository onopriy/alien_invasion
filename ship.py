import pygame


class Ship:
    """Class about starship behavior"""

    def __init__(self, ai_game):
        """Initialize ship settings"""
        self.screen = ai_game.screen
        self.screen_rectangle = ai_game.screen.get_rect()
        self.image = pygame.image.load('images\\ship.bmp')  # load image of ship
        self.rectangle = self.image.get_rect()
        self.rectangle.midbottom = self.screen_rectangle.midbottom  # every new ship spawn at bottom of display

    def blitme(self):
        """Draw ship in currently position"""
        self.screen.blit(self.image, self.rectangle)
