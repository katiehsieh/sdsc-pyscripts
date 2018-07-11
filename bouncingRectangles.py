import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WIDTH = 200
HEIGHT = 900

pygame.init()

# Set the width and height of the playing screen
size = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(size)

# Caption of window
pygame.display.set_caption("Bouncing Rectangle")


# Loop until the user clicks the 'close' button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting positon of the rectangle
rect_x = 50
rect_y = 50

# Speed and direction of rectangle
rect_change_x = 10
rect_change_y = 10

# --------------- Main Program Loop ---------------
while not done:
    # Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Logic
    # Move the rectangle starting piont
    rect_x += rect_change_x
    rect_y += rect_change_y

    # Bounce the ball if needed
    if rect_y > HEIGHT - 50 or rect_y < 0:
        rect_change_y = rect_change_y * -1

    if rect_x > WIDTH - 50 or rect_x < 0:
        rect_change_x = rect_change_x * -1

    # --- Drawing
    # Set the screen background
    #screen.fill(BLACK)

    # Draw the rectangle
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, CYAN, [rect_x + 10, rect_y + 10, 30, 30])

    # --- Wrap-up
    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn
    pygame.display.flip()

# Close everything down
pygame.quit
