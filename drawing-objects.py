# pylint: disable=no-member
from random import randint, choice
import random
import pygame

# Define the lanes list
lanes = [93, 218, 343]

# Import and initialize pygame
pygame.init()

# Get the clock
clock = pygame.time.Clock()

# Define the GameObject class as a base class for other sprites
class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image, width=None, height=None):
        super(GameObject, self).__init__()
        self.image = pygame.image.load(image)  # Load image
        if width and height:
            self.image = pygame.transform.scale(self.image, (width, height))  # Resize image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.image, self.rect.topleft)

class Ball(GameObject):
    def __init__(self, ball_type):
        super(Ball, self).__init__(0, -64, f'{ball_type}.png', 50, 50)  
        self.dx = 0
        self.dy = randint(1, 2)  
        self.reset()
        print(f'{ball_type} Image Path: {self.image}')

    def move(self):
        self.rect.y += self.dy
        if self.rect.y > 500:
            self.reset()
            
    def reset(self):
        self.rect.x = random.choice(lanes)
        self.rect.y = -64
        self.dy = randint(1, 2)

    def render(self, screen):
        print(f'{self.__class__.__name__} Rendering at: ({self.x}, {self.y})')
        super(Ball, self).render(screen)

# Define the Player class, inheriting from GameObject
class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0, 0, 'player.png', 50, 50)
        self.dx = 0
        self.dy = 0
        self.reset()

    def left(self):
        self.dx -= 20  # Increase the increment

    def right(self):
        self.dx += 20

    def up(self):
        self.dy -= 20

    def down(self):
        self.dy += 20

    def move(self):
        self.rect.x -= (self.rect.x - self.dx) * 0.25
        self.rect.y -= (self.rect.y - self.dy) * 0.25

        # Restrict the player's position to stay within the screen boundaries
        self.x = max(0, min(self.x, 500 - self.image.get_width()))
        self.y = max(0, min(self.y, 500 - self.image.get_height()))

    def reset(self):
        self.x = 250 - 32
        self.y = 250 - 32
        self.dx = 0
        self.dy = 0

    def render(self, screen):
        screen.blit(self.image, self.rect.topleft)

# Configure the screen
screen = pygame.display.set_mode([500, 500])

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

# Add sprites to groups
all_sprites.add(player, soccer_ball, basketball, tennis_ball)
balls_group.add(soccer_ball, basketball, tennis_ball)
player_group.add(player)


# Load background image (or set background color)
background_image = pygame.image.load('stadium.png')  # Replace with your image file or use a color
background_image = pygame.transform.scale(background_image, (500, 500))
background_rect = background_image.get_rect()

# ... (your existing code)

# Create the game loop
running = True
while running:
    # Look at events
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

    # Clear screen with background image (or color)
    screen.blit(background_image, background_rect)

    # Update all sprites
    all_sprites.update()
    balls_group.update()
    player_group.update()

    # Check for collisions with balls
    ball_collisions = pygame.sprite.spritecollide(player, balls_group, dokill=True)

    # Handle ball collisions
    for ball in ball_collisions:
        player.reset()  # Reset player position
        ball.reset()  # Reset the collided ball

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
