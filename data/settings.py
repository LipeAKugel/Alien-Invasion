# Settings for Alien Invasion
class Settings():
    """ Class to store all the settings in Alien Invasion """
    
    def __init__(self):
        """ Initializes the game's static settings """
        # Screen settings:
        self.bg_width = 1200
        self.bg_lenght = 700
        self.bg_color = (30, 30, 30)
        
        # Audio settings:
        self.audio_volume = 0.1

        # Ship settings:
        self.ship_limit = 3

        # Alien settings:
        self.fleet_drop_speed = 10
        
        # Bullet settings:
        self.bullet_width = 5
        self.bullet_lenght = 15
        self.bullet_color = 255, 200, 10
        self.max_bullets = 3

        # Star background settings:
        self.star_bg_width = 1200
        self.star_bg_height = 700
        self.star_bg_speed = 0.5
        self.star_width = 2
        self.star_height = 2
        self.star_color = 250, 250, 250
        self.number_stars = 150

        # Speed increase settings:
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game. """
        # Ship settings:
        self.ship_speed_factor = 1.5

        # Alien settings:
        self.alien_speed_factor = 1
        self.alien_points = 50

        # Bullet settings:
        self.bullet_speed_factor = 1

        # fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """ Increases speed settings. """
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)