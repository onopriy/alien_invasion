import sys
from time import sleep
import pygame

from game_stats import GameStats
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard


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
        # creating of example for make a user stats
        self.stats = GameStats(self)
        self.scoareboard = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self, 'Play')



    def run_game(self):
        """Start of main game's loop"""
        while True:
            self._check_event()  # checking keyboard and mouse
            if self.stats.game_active:
                self.ship.update()  # update of ship position
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_event(self):
        """Checking user's mouse and keyboard"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                record_file = open('record.txt', 'w+')
                record_file.write(str(self.stats.high_score))
                record_file.close()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start new game when player tap Play button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialized_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.scoareboard.prep_score()
            self.scoareboard.prep_level()
            self.scoareboard.prep_ships()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Check user down key"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_ESCAPE:
            record_file = open('record.txt', 'w+')
            record_file.write(str(self.stats.high_score))
            sys.exit()

    def _check_keyup_events(self, event):
        """Check user up key"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _ship_hit(self):
        """Behavior of game when ship is hit"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.scoareboard.prep_ships()

            # clean lists of aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # creating new fleet and ship spawn
            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)  # pause
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _fire_bullet(self):
        """Creating of new projectfile and adding it to group bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        else:
            pass

    def _update_bullets(self):
        """Update positions of projectile and delete old"""
        self.bullets.update()  # update position of every projectile
        for bullet in self.bullets.copy():  # delete of invisible projectile
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullets_collisions()

    def _check_bullets_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.scoareboard.prep_score()
            self.scoareboard.check_high_score()
        if not self.aliens:
            self.bullets.empty()
            self.settings.increase_speed()
            self._create_fleet()
            self.stats.level += 1
            self.scoareboard.prep_level()

    def _check_alien_bottom(self):
        """Check that alien contact to bottom of surface"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()    # same when ship is hit
                break

    def _update_aliens(self):
        """Update position of moving alien"""
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_alien_bottom()

    def _create_alien(self, alien_number, row_number):
        """Helpful function to create alien for line of ships"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        """Create fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)  # interval between alien ship's 2 widths
        # define number of rows on surface
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        # first line of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        """Check alien connect to edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Fleet moving down or to different edge"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update of screen"""
        self.screen.fill(self.settings.background_color)  # redrawing surface in putting color
        self.ship.blitme()  # image of ship
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.scoareboard.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()  # show last frame


if __name__ == '__main__':
    # creating example of game:
    ai = AlienInvasion()
    ai.run_game()
