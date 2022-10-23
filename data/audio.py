from pygame import mixer

class Audio:
    """ Audio system for Alien Invasion """

    def __init__(self, settings, stats):
        """ Initializes audio settings and attributes """
        self.stats = stats
        mixer.music.set_volume(settings.audio_volume)

        # Initialize sound effects
        self.fire_bullet = mixer.Sound('data/sound_effects/fire_bullet.wav')
        self.lost_ship = mixer.Sound('data/sound_effects/error.ogg')

    def play_bg_music(self):
        """ Plays the background music on repeat """
        mixer.music.load('data/music/bg.ogg')
        mixer.music.play(-1)

    def bullet_fired(self):
        """ Plays the bullet fired sound """
        mixer.Sound.play(self.fire_bullet)

    def ship_lost(self):
        """ Plays a sound when the player loses a ship """
        mixer.Sound.play(self.lost_ship)

    def update(self):
        """ Updates the game's audio """
        if not self.stats.game_active:
            mixer.music.stop()


