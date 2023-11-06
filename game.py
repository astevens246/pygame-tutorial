import pygame
# pylint: disable=no-member

pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Create the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))
    num_rows = 3
    num_cols = 3
    circle_radius = 75
    
    for row in range(num_rows):
        for col in range(num_cols):
            x = col * (circle_radius * 2 + 10) + circle_radius
            y = row * (circle_radius * 2 + 10) + circle_radius
            position = (x, y)
            color = (64, 64, 64) #dark grey
            pygame.draw.circle(screen, color, position, circle_radius)
    #Update the display
    pygame.display.flip()
    
    # # Draw the red circle
    # color = (255, 0, 0)
    # position = (50, 50)
    # pygame.draw.circle(screen, color, position, 75)

    # # Draw the orange circle
    # color1 = (252, 132, 3)
    # position1 = (450, 50)
    # pygame.draw.circle(screen, color1, position1, 75)
    
    # # Draw the yellow circle
    # color1 = (248, 252, 3)
    # position1 = (250, 250)
    # pygame.draw.circle(screen, color1, position1, 75)
    
    # # Draw the green circle
    # color1 = (3, 252, 53)
    # position1 = (100, 400)
    # pygame.draw.circle(screen, color1, position1, 75)
    
    # # Draw the blue circle
    # color1 = (3, 3, 252)
    # position1 = (400, 400)
    # pygame.draw.circle(screen, color1, position1, 75)

    # # Update the display
    # pygame.display.flip()

pygame.quit()

