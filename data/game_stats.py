import json

class GameStats:
    """ A class to track in-game statistcs in Alien Invasion. """

    def __init__(self, settings):
        """ Initialize statistics. """
        self.settings = settings
        self.reset_stats()
        self.load_saved_stats()

        # Start alien invasion in an inactive state
        self.game_active = False

    def reset_stats(self):
        """ Initialize statistics that can change during the game. """
        self.ships_left = self.settings.ship_limit
        self.level = 1
        self.score = 0

    def load_saved_stats(self):
        """ Loads saved stats """
        filename = 'data/save_stats.json'
        try:
            with open(filename) as f_obj:
                # Load the saved high score.
                self.high_score = json.load(f_obj)
        except FileNotFoundError:
            self.high_score = 0

    def update(self):
        """ Update and check game stats """
        # Inactivate the game if the player loses all their ships
        if self.ships_left <= 0:
            self.game_active = False
