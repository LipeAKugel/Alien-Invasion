import pygame

from data.settings import Settings
from data.ship import Ship
import data.game_functions as gf
from pygame.sprite import Group
from data.game_stats import GameStats
from data.button import Button
from data.text import Text
from data.scoreboard import Scoreboard
from data.audio import Audio
 
def run_game():
    # Initializes the game and creates a window.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.bg_width, settings.bg_lenght)
        )
    pygame.display.set_caption("Alien Invasion")
    
    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)

    # Create an audio instance
    audio = Audio(settings, stats)

    # Make all buttons.
    start_message = "Press enter to start"
    play_button = Button(settings, screen, start_message, 150)

    # Make all texts.
    quit_message = "Press q to quit"
    quit_text = Text(settings, screen, quit_message, size=24)

    game_over_msg = "Gameover!"
    game_over_text = Text(settings, screen, game_over_msg, size=24)
    game_over_text.rect.center = play_button.rect.center
    game_over_text.rect.bottom = play_button.rect.top

    # Make the background stars
    stars = Group()
    gf.make_background(settings, screen, stars)
     
     # Make a ship, a group of bullets and a group of aliens
    ship = Ship(screen, settings)
    bullets = Group()
    aliens = Group()

    # Create a fleet of aliens
    gf.create_fleet(settings, screen, aliens)

    # Start the main loop for the game.
    while True:
        # Check for events
        gf.check_events(settings, screen, stats, audio, sb, ship, 
            aliens, bullets)

        # Update only when the game is active
        if stats.game_active:
            stars.update()
            ship.update()
            gf.update_aliens(settings, stats, audio, sb, screen, ship, aliens, bullets)
            gf.update_bullets(settings, screen, aliens, bullets, stats, sb)
            gf.update_scoreboard(settings, stats, sb)

        # Update the game's stats
        stats.update()

        # Update the game's audio.
        audio.update()

        # Update the game's screen elements
        gf.update_screen(settings, screen, stats, sb, ship, bullets, aliens, 
            stars, play_button, quit_text, game_over_text)
        
# -----

run_game()
