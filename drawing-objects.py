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
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.image = pygame.image.load(image)  # Load image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        pass  # Placeholder method, to be overridden by subclasses

# Define the Apple class, inheriting from GameObject
class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, -64, 'apple.png')  # Start from top with a random x position
        self.dx = 0
        self.dy = (randint(1, 3))  # Move downward
        self.reset()

    def move(self):
        self.y += self.dy
        if self.y > 500:
            self.reset()

    def reset(self):
        self.x = random.choice(lanes)
        self.y = -64

# Define the Strawberry class, inheriting from GameObject
class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, -64, 'strawberry.png')  # Start from left with a random y position
        self.dx = randint(1, 3)  # Move from left to right
        self.dy = 0
        self.reset()

    def move(self):
        self.x += self.dx
        if self.x > 500:
            self.reset()

    def reset(self):
        self.x = random.choice(lanes)  # Randomly choose between lanes
        self.y = randint(0, 500)

# Define the Player class, inheriting from GameObject
class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0, 0, 'player.png')
        self.dx = 0
        self.dy = 0
        self.reset()

    def left(self):
        self.dx -= 100

    def right(self):
        self.dx += 100

    def up(self):
        self.dy -= 100

    def down(self):
        self.dy += 100

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

        # Restrict the player's position to stay within the screen boundaries
        self.x = max(0, min(self.x, 500 - self.image.get_width()))
        self.y = max(0, min(self.y, 500 - self.image.get_height()))

    def reset(self):
        self.x = 250 - 32
        self.y = 250 - 32

# Define the Bomb class, inheriting from GameObject
class Bomb(GameObject):
    def __init__(self):
        super(Bomb, self).__init__(0, 0, 'bomb.png')
        self.image = pygame.transform.scale(self.image, (64, 64))  # Resize the image
        self.reset_direction()

    def reset(self):
        self.x = choice(lanes)
        self.y = choice(lanes)
        
    def reset_direction(self):
        # Choose a random direction: 0 for up, 1 for down, 2 for left, 3 for right
        self.direction = randint(0, 3)
        self.dx = 5  # You can adjust the speed as needed
        self.dy = 5

    def move(self):
        if self.direction == 0:
            self.y -= self.dy
        elif self.direction == 1:
            self.y += self.dy
        elif self.direction == 2:
            self.x -= self.dx
        elif self.direction == 3:
            self.x += self.dx

        # Check if the bomb is off the screen, then reset its direction
        if (self.direction == 0 and self.y < -64) or (self.direction == 1 and self.y > 500) or \
           (self.direction == 2 and self.x < -64) or (self.direction == 3 and self.x > 500):
            self.reset_direction()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Create sprite groups
all_sprites = pygame.sprite.Group()
apples_group = pygame.sprite.Group()
strawberries_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

# Create the apple, strawberry, player, and bomb objects
apple = Apple()
strawberry = Strawberry()
player = Player()
bomb = Bomb()

# Add sprites to groups
all_sprites.add(apple, strawberry, player, bomb)
apples_group.add(apple)
strawberries_group.add(strawberry)
player_group.add(player)


 #Create the game loop
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

    # Update all sprites
    all_sprites.update()

    # Clear screen
    screen.fill((0, 0, 0))

    # Move and draw sprites
    for sprite in all_sprites:
        sprite.move()
        sprite.render(screen)

    # Update the window
    pygame.display.flip()
    clock.tick(60)

# Quit pygame when the loop exits
pygame.quit()