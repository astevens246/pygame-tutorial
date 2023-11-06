# pylint: disable=no-member

# Import and initialize pygame
import pygame
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Create a new instance of Surface
surf = pygame.Surface((50, 50))
surf.fill((255, 111, 33))
pygame.draw.circle(surf, (255, 0, 0), (25, 25), 20)  # Draw a red circle on surf

# Create the game loop
running = True
while running:
  # Look at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  # Clear screen
  screen.fill((255, 255, 255))
  
  # Draw the surface
  screen.blit(surf, (100, 120))
  
  # Update the window
  pygame.display.flip()

# Quit pygame when the loop exits
pygame.quit()
