import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Class for a alien in Alien Invasion """

    def __init__(self, screen, settings):
        """ Create the alien and set it's starting location """
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load the alien image and it's rect
        self.image = pygame.image.load('data/images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Place the alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Precisely store the alien's position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """ Check if the alien is in the edge of the screen """
        if (self.rect.right >= self.screen_rect.right):
            return True
        elif (self.rect.left <= 0):
            return True

    def update(self):
        """ Update the alien's position """
        self.x += (self.settings.alien_speed_factor *
            self.settings.fleet_direction)
            
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """ Draw the alien at it's current position """
        self.screen.blit(self.image, self.rect)