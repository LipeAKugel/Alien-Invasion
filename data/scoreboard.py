import pygame.font
from pygame.sprite import Group

from data.ship import Ship

class Scoreboard():
    """ A class to report scoring information. """

    def __init__(self, settings, screen, stats):
        """ Initialize scorekeeping attributes. """
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        # Font settings for scoring inforamtion.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_images()
        self.prep_ships()

    def prep_images(self):
        """ Renders the score images """
        # Prepare the initial score images.
        self.prep_score()
        self.prep_level()
        self.prep_high_score()

    def prep_score(self):
        """ Turn the score into a rendered image. """
        round_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 10

    def prep_level(self):
        """ Turn the level into a rendered image. """
        level = int(self.stats.level)
        level_str = "{:,}".format(level)
        self.level_image = self.font.render(level_str, True, self.text_color)

        # Display the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.right - 30
        self.level_rect.top = self.score_rect.bottom + 5

    def prep_high_score(self):
        """ Turn the high score into a rendered image. """
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 10

    def prep_ships(self):
        """ Show how many ships are left. """
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen, self.settings, (40, 40))
            ship.rect.x = 150 + (10 + ship.rect.width) * ship_number
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """ Draw score to the screen. """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)