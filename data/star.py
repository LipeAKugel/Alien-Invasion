import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """ Class of a star in Alien Invasion """

    def __init__(self, settings, screen):
        """ Creates a star and set it's starting location """
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.color = settings.star_color

        # Create the star at a random position in the screen
        self.rect = pygame.Rect(0, 0, self.settings.star_width,
            self.settings.star_height)
        
        # Store the star position precisely
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self):
        """ Updates the star's position """
        # Update the y position and set it to the top of the screen
        # if the star is at the bottom
        if self.y <= 700:
            self.y += self.settings.star_bg_speed
            self.rect.y = self.y
        else:
            self.y = 0
            self.rect.y = self.y

        # Update the x position
        self.rect.x = self.x

    def draw_star(self):
        """ Draws the star to the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)
