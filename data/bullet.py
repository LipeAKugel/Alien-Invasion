import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Class for a bullet in Alien Invasion """
    
    def __init__(self, settings, screen, ship):
        """ Create a bullet in the ship's current position """
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor
        
        # Create a bullet at (0, 0) and set to the ship's position.
        self.rect = pygame.Rect(0, 0, settings.bullet_width,
            settings.bullet_lenght)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store the value of the bullet's position
        self.y = float(self.rect.y)
        
    def update(self):
        """ Move the bullet up the screen """
        self.y -= self.speed_factor
        self.rect.y = self.y
        
    def draw_bullet(self):
        """ Draws the bullet to the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)
