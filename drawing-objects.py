# pylint: disable=no-member
from random import randint
import random
# Import and initialize pygame
import pygame
# Get the clock
clock = pygame.time.Clock()

class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.image = pygame.image.load(image) #add image
    self.rect = self.image.get_rect(topleft=(x, y))
    self.x = x
    self.y = y
  
  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

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
        self.x = random.choice([93, 218, 343])
        self.y = -64

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
        self.x = random.choice([93, 343])  # Randomly choose between 93 and 343 for x
        self.y = randint(0, 500)
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
    self.x = max(0, min(self.x, 500 - self.surf.get_width()))
    self.y = max(0, min(self.y, 500 - self.surf.get_height()))

  def reset(self):
    self.x = 250 - 32
    self.y = 250 - 32
  

    
pygame.init()

  
# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Create sprite groups 
all_sprites = pygame.sprite.Group()
apples_group = pygame.sprite.Group()
strawberries_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

# Create the apple object
apple = Apple()
strawberry = Strawberry()
player = Player() #Create an instance of the Player class

# Add sprites to groups
all_sprites.add(apple, strawberry, player)
apples_group.add(apple)
strawberries_group.add(strawberry)
player_group.add(player)


# Create the game loop
running = True
while running:
  # Look at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
# Check for event type KEYBOARD
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
  
  # Draw sprites
  all_sprites.draw(screen)



  # Update the window
  pygame.display.flip()
  clock.tick(60)

# Quit pygame when the loop exits
pygame.quit()
