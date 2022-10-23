import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """ Class for a ship in Alien Invasion """
    
    def __init__(self, screen, settings, scale_factor=(40, 40)):
        """ Create the ship and set it's starting location """
        super().__init__()
        self.screen = screen
        self.settings = settings
        
        # Load the ship and get it's rect.
        self.image = pygame.image.load('data/images/ship.bmp')
        self.image = pygame.transform.scale(self.image, scale_factor)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each ship in the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Stores the value for the ships center.
        self.center = float(self.rect.centerx)
        
        # Initilize its movement flags
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """ Set the ship's position to the bottom center of the screen """
        self.center = self.screen_rect.centerx

    def update(self):
        """ Moves the ship according to the movement flags """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.settings.ship_speed_factor
        
        # Update the ship rect
        self.rect.centerx = self.center
        
    def blitme(self):
        """ Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)
