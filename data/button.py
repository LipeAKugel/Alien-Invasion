import pygame
import pygame.font

class Button:
    """ A class to represent a button in Alien Invasion """

    def __init__(self, settings, screen, msg, alpha=0):
        """ Initialize the button attributes """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        size = self.width, self.height = (350, 50)
        self.alpha = alpha
        self.button_color = (0, 0, 0, self.alpha)
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.image.fill(self.button_color)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """ Turn the msg into a rendered image """
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw a blank button and then draw the message.
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        