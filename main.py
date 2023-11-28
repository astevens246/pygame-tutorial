# main.py
import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from gameobject import GameObject
from ball import Ball
from player import Player

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
player_group.add(player)

# Create different sports balls
soccer_ball = Ball('soccer_ball', 'soccer_ball.png')
basketball = Ball('basketball', 'basketball.png')
tennis_ball = Ball('tennis_ball', 'tennis_ball.png')
bomb_ball = Ball('bomb_ball', 'bomb_ball.png')
apple = Ball('apple', 'apple.png')
strawberry = Ball('strawberry', 'strawberry.png')

# Create more instances of the same sprites
additional_soccer_balls = [Ball('soccer_ball', 'soccer_ball.png') for _ in range(3)]
additional_basketballs = [Ball('basketball', 'basketball.png') for _ in range(3)]
additional_tennis_balls = [Ball('tennis_ball', 'tennis_ball.png') for _ in range(3)]
additional_bomb_balls = [Ball('bomb_ball', 'bomb_ball.png') for _ in range(3)]
additional_apples = [Ball('apple', 'apple.png') for _ in range(3)]
additional_strawberries = [Ball('strawberry', 'strawberry.png') for _ in range(3)]

# Add new instances to sprite groups
all_sprites.add(
    player,
    soccer_ball,
    basketball,
    tennis_ball,
    bomb_ball,
    apple,
    strawberry,
    *additional_soccer_balls,
    *additional_basketballs,
    *additional_tennis_balls,
    *additional_bomb_balls,
    *additional_apples,
    *additional_strawberries
)

balls_group.add(
    soccer_ball,
    basketball,
    tennis_ball,
    bomb_ball,
    apple,
    strawberry,
    *additional_soccer_balls,
    *additional_basketballs,
    *additional_tennis_balls,
    *additional_bomb_balls,
    *additional_apples,
    *additional_strawberries
)

# Load background image and scale it to the screen size
background_image = pygame.image.load('stadium.png')  # Replace with your image file
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize font
font = pygame.font.Font(None, 36)  # None uses the default font, 36 is the font size

# Define game states
READY_STATE = 'ready'
PLAYING_STATE = 'playing'
GAME_OVER_STATE = 'game_over'

# Set initial game state
game_state = READY_STATE

# Create the game loop
running = True
score = 0  # Initialize score outside the loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                if game_state == READY_STATE:
                    game_state = PLAYING_STATE
                    for sprite in balls_group:
                        sprite.reset()
                    score = 0
                    player.reset()
                elif game_state == GAME_OVER_STATE:
                    game_state = READY_STATE

            # Handle arrow key events only when in the playing state
            elif game_state == PLAYING_STATE:
                if event.key == pygame.K_LEFT:
                    player.left()
                elif event.key == pygame.K_RIGHT:
                    player.right()
                elif event.key == pygame.K_UP:
                    player.up()
                elif event.key == pygame.K_DOWN:
                    player.down()

    screen.blit(background_image, (0, 0))

    if game_state == READY_STATE:
        ready_text = font.render("Press Enter to Start", True, (255, 255, 255))
        screen.blit(ready_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))
    elif game_state == PLAYING_STATE:
        all_sprites.update()

        for sprite in all_sprites:
            sprite.render(screen)

        # Check for collisions with balls
        ball_collisions = pygame.sprite.spritecollide(player, balls_group, dokill=True)

        # Handle ball collisions and update score
        for ball in ball_collisions:
            if ball.ball_type == 'bomb_ball':
                game_state = GAME_OVER_STATE
                player.reset()
                for sprite in all_sprites:
                    if isinstance(sprite, Ball):
                        sprite.reset()
                score = 0
            else:
                score += ball.reset()

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
    elif game_state == GAME_OVER_STATE:
        game_over_text = font.render("Game Over. Press Enter to Restart", True, (255, 255, 255))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
