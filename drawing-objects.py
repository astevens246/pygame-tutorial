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
    self.surf = pygame.image.load(image) #add image
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


    
pygame.init()

  
# Configure the screen
screen = pygame.display.set_mode([500, 500])
# Create the apple object
apple = Apple()
strawberry = Strawberry()


# Create the game loop
running = True
while running:
  # Look at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      # Clear screen
  screen.fill((0, 0, 0))
  # Draw apple
  apple.move()
  apple.render(screen)
  #Draw strawberry 
  strawberry.move()
  strawberry.render(screen)




  # Update the window
  pygame.display.flip()
  clock.tick(60)

# Quit pygame when the loop exits
pygame.quit()
