import pygame
import math

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

size = [400, 400]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Radar Sweep")

clock = pygame.time.Clock()

done = False

angle = 0

# --------------- Main Loop ---------------

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    # Dimensions of radar sweep
    # Start with the top left at 20,20 with a width/height of 250
    boxDimension = [20,20,250,250]

    pygame.draw.ellipse(screen, GREEN, boxDimension, 2)

    # Draw a black box around the circle
    pygame.draw.rect(screen, BLACK, boxDimension, 2)

    # Calculate the x,y for the end point of our 'sweep' based on current angle
    x = 125 * math.sin(angle) + 145
    y = 125 * math.cos(angle) + 145

    # Draw the line from the center at 145,145 to the calculated end point
    pygame.draw.line(screen, GREEN, [145,145], [x,y], 2)

    angle += 0.05

    # If we have a full sweep, reset the angle to 0
    PI = 3.141592653
    if angle > 2 * PI:
        angle = angle - 2 * PI

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
