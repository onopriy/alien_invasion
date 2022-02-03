import pygame


class Ship:
    """Class about starship behavior"""

    def __init__(self, ai_game):
        """Initialize ship settings"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rectangle = ai_game.screen.get_rect()
        self.image = pygame.image.load('images\\ship.bmp')  # load image of ship
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rectangle.midbottom  # every new ship spawn at bottom of display
        self.x = float(self.rect.x)  # saving of ship's float x coordinate
        self.moving_right = False  # flag of moving ship on right
        self.moving_left = False  # flag of left moving

    def blitme(self):
        """Draw ship in currently position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update position of ship"""
        # if ship is moving and image's coordinate of right(or left) side is not a last coordinate of screen
        if self.moving_right and self.rect.right < self.screen_rectangle.right:
            self.x += self.settings.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.speed
        self.rect.x = self.x

    def center_ship(self):
        """Spawn ship in midtop"""
        self.rect.midbottom = self.screen_rectangle.midbottom
        self.x = float(self.rect.x)
