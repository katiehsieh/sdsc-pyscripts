import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A 2D array is simply a list of lsits
grid = []
for row in range(10):
    #Add an empty array that will hold each cell in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0) #append a cell

# Set row 1, cell 5 to '1'. (Remember rows and column numbers start at zero)
grid[1][5] = 1

# Initial pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user click the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# --------------- Main Program Loop ---------------

while not done:
    for event in pygame.event.get(): #user did something
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #user click the mouse... get the position
            pos = pygame.mouse.get_pos()
            #Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to '1'
            grid[row][column] = 1
            print("Click ", pos, "Grid cooridantes: ", row, column)

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

    # Limit to 60 frames a second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn
    pygame.display.flip()


pygame.quit()
