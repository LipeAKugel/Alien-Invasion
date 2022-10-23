# Game functions for Alien Invasion

import sys
import json
from time import sleep

import pygame

from random import randint
from data.star import Star
from data.bullet import Bullet
from data.alien import Alien
from data.ship import Ship

# General functions:
def reset_game(settings, screen, aliens, bullets, ship):
    """ Resets the game """
    # Empty the list of aliens and bullets.
    aliens.empty()
    bullets.empty()

    # Create a new fleet and center the ship.
    create_fleet(settings, screen, aliens)
    ship.center_ship()

def check_high_score(stats, sb):
    """ Check to see if there's a new high score. """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def save_stats(stats):
    """ Save the stats into a json file """
    filename = 'data/save_stats.json'
    with open(filename, 'w') as f_obj:
        json.dump(stats.high_score, f_obj)

# Background related functions:
def make_background(settings, screen, stars):
    """ Creates a background of stars """
    for star_number in range(settings.number_stars):
        star = Star(settings, screen)
        star.x = randint(0, settings.star_bg_width)
        star.y = randint(0, settings.star_bg_height)
        stars.add(star)

# Ship related functions:
def fire_bullet(settings, audio, bullets, screen, ship):
    """ Creates a bullet at the ship's position """
    if len(bullets) < settings.max_bullets:
        # Create a new bullet and add it to the bullets group.
            new_bullet = Bullet(settings, screen, ship)
            bullets.add(new_bullet)
            audio.bullet_fired()

def ship_hit(settings, stats, audio, screen, sb, ship, aliens, bullets):
    """ Responds to an alien hitting the ship. """
    # Decrements ships left.
    stats.ships_left -= 1
    audio.ship_lost()
    sb.prep_ships()

    if stats.ships_left > 0:
        reset_game(settings, screen, aliens, bullets, ship)
        # Pause.
        sleep(0.5)

# Alien or fleet related functions:
def create_alien(screen, settings, aliens, alien_number, row_number):
    """ Creates a alien and adds it to the aliens group """
    alien = Alien(screen, settings)
    alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
    alien.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)

def check_bullet_alien_collision(settings, screen, aliens, bullets, stats, sb):
    """ Checks for collison between bullets and aliens """
    # Check if a bullet hit a alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(settings, screen, aliens)
        # Increase the game's speed and level
        settings.increase_speed()
        stats.level += 1

    update_scoreboard(settings, stats, sb, collisions)

def check_alien_bottom(settings, screen, stats, audio, sb, alien, aliens, ship, bullets):
    """ Responds to a alien hitting the bottom of the screen """
    if alien.rect.bottom >= settings.bg_lenght:
        # Decrease the amount of ships left
        stats.ships_left -= 1
        audio.ship_lost()
        sb.prep_ships()

        if stats.ships_left > 0:
            reset_game(settings, screen, aliens, bullets, ship)
            # Pause
            sleep(0.5)

        return True

def get_number_aliens(settings, alien_width):
    """ Gets the number of aliens that fit in the screen """
    available_space = settings.bg_width - 2 * alien_width
    number_aliens = int(available_space / (2 * alien_width))
    return number_aliens

def get_number_rows(settings, alien_height, ship_height):
    """ Gets the number of rows that fit in the screen """
    available_space = settings.bg_lenght - 3 * alien_height - ship_height
    number_rows = int(available_space / (2 * alien_height))
    return number_rows

def create_fleet(settings, screen, aliens):
    """ Create's a fleet of aliens """
    # Get the available space on the screen
    alien = Alien(screen, settings)
    ship = Ship(screen, settings)
    number_aliens = get_number_aliens(settings, alien.rect.width)
    number_row = get_number_rows(settings, alien.rect.height, ship.rect.height)

    # Create the fleet
    for row_number in range(number_row):
        for alien_number in range(number_aliens):
            create_alien(screen, settings, aliens, alien_number, row_number)

def check_fleet_edges(settings, aliens):
    """ Responds if any alien has reached the edge of the screen. """
    for alien in aliens:
        if alien.check_edges() == True:
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    """ Changes the fleet's direction and moves it down. """
    settings.fleet_direction *= -1
    for alien in aliens:
        alien.y += settings.fleet_drop_speed

# Event check functions:
def play_button_pressed(settings, screen, stats, audio, sb, aliens, 
    bullets, ship):
    """ Resets and starts the game """
    # Only reset the game if the game is inactive.
    if stats.game_active == False:
        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True
        settings.initialize_dynamic_settings()

        # Restart background music.
        audio.play_bg_music()

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        reset_game(settings, screen, aliens, bullets, ship)

def check_key_events(event, settings, screen, stats, audio, sb, aliens, ship, 
    bullets):
    """ Checks for key events. """
    # Check for KEYDOWN events.
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            save_stats(stats)
            sys.exit()
        if event.key == pygame.K_RETURN:
            if not stats.game_active:
                play_button_pressed(settings, screen, stats, audio, sb, aliens,
                    bullets, ship)

        # Check only if the game is active.
        if stats.game_active:   
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            if event.key == pygame.K_SPACE:
                fire_bullet(settings, audio, bullets, screen, ship)
    
    # Check for KEYUP events.
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        if event.key == pygame.K_LEFT:
            ship.moving_left = False

def check_events(settings, screen, stats, audio, sb, ship, aliens, 
    bullets):
    """Checks for keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_stats(stats)
            sys.exit()
        
        # Check keyboard events
        check_key_events(event, settings, screen, stats, audio, sb, aliens,
            ship, bullets)

# Update functions:
def update_scoreboard(settings, stats, sb, collisions=0):
    """ Updates the points and the scoreboard """
    if collisions:
        # Update the score points.
        for shot_alien in list(collisions.values()):
            stats.score += settings.alien_points

    # Update the scoreboard.
    sb.prep_images()
    check_high_score(stats, sb)

def update_screen(settings, screen, stats, sb, ship, bullets, aliens,
    stars, play_button, quit_text, game_over_text):
    """Updates the images and flips to the new screen."""
    # Redraw the screen.
    screen.fill(settings.bg_color)

    # Update the scoreboard
    sb.show_score()

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Redraw all stars
    for star in stars.sprites():
        star.draw_star()

    # Draw the play button only if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Draw screen texts
    quit_text.draw_text()
    # Only draw the game over text if the player has no ships.
    if stats.ships_left <= 0:
        game_over_text.draw_text()
        sleep(0.5)

    # Hide the mouse if the game is active, show the mouse if the game is inactive.
    if stats.game_active:
        pygame.mouse.set_visible(False)
    else:
        pygame.mouse.set_visible(True)
    
    # Flip to the updated screen.
    pygame.display.flip()

def update_bullets(settings, screen, aliens, bullets, stats, sb):
    """ Updates the game's bullets """
    bullets.update()
    # Remove offscreen bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(settings, screen, aliens, bullets, stats, sb)

def update_aliens(settings, stats, audio, sb, screen, ship, aliens, bullets):
    """ Update all the aliens in the fleet """
    check_fleet_edges(settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, audio, screen, sb, ship, aliens, bullets)

    for alien in aliens:
        if check_alien_bottom(
                settings, screen, stats, audio, sb, alien, aliens, ship, bullets
                ):
            break