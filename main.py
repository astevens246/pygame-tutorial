import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from gameobject import GameObject
from ball import Ball
from player import Player

# Import other game objects as needed

# Initialize Pygame
pygame.init()

# Get the clock
clock = pygame.time.Clock()

# Configure the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Create sprite groups
all_sprites = pygame.sprite.Group()
balls_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

# Create the player object
player = Player()

# Create different sports balls
soccer_ball = Ball('soccer_ball')
basketball = Ball('basketball')
tennis_ball = Ball('tennis_ball')
bomb_ball = Ball('bomb_ball')  # Add a bomb ball

# Add sprites to groups
all_sprites.add(player, soccer_ball, basketball, tennis_ball, bomb_ball)
balls_group.add(soccer_ball, basketball, tennis_ball, bomb_ball)
player_group.add(player)

# Load background image and scale it to the screen size
background_image = pygame.image.load('stadium.png')  # Replace with your image file
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
background_rect = background_image.get_rect()

# Create the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()

    # Clear screen with scaled background image
    screen.blit(background_image, background_rect)

    # Update all sprites
    all_sprites.update()
    balls_group.update()
    player_group.update()

    # Check for collisions with balls
    ball_collisions = pygame.sprite.spritecollide(player, balls_group, dokill=True)

    # Handle ball collisions
    for ball in ball_collisions:
        if ball.ball_type == 'bomb_ball':  # Check if the collided ball is a bomb
            player.reset()  # Reset player position
            for sprite in all_sprites:
                sprite.reset()  # Reset all sprites
            score = 0  # Reset the score
            running = False  # End the game

    # Move and draw sprites
    for sprite in all_sprites:
        sprite.move()

    # Draw sprites after clearing the screen
    for sprite in all_sprites:
        sprite.render(screen)

    # Update the window
    pygame.display.flip()
    clock.tick(60)

# Quit pygame when the loop exits
pygame.quit()
