import pygame
import pygame.font

class Text:
    """ Class for texts in Alien Invasion """

    def __init__(self, settings, screen, msg, size = 48):
        """ Initialize the text attributes """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the properties of the text.
        self.size = size
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, self.size)

        # Turn the msg into a rendered image and set it's location.
        self.image = self.font.render(msg, True, self.text_color)
        self.rect = self.image.get_rect()
        self.rect.y = 10
        self.rect.x = 20

    def draw_text(self):
        """ Draws the text to the screen """
        self.screen.blit(self.image, self.rect)