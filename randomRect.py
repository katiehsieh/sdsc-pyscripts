import pygame
import random

pygame.init

# Random window size
WIDTH = random.randint(500,700)
HEIGHT = random.randint(400,600)
print("Window width:", WIDTH)
print("Window height:", HEIGHT)

size = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Random Rectangles")

# Random number of rectangles
numRect = random.randint(3,7)
print("Number of rectangles: " + str(numRect))

# Repeat for number of rectangles
counter = 1
while counter <= numRect:
    print()
    print("Rectangle #" + str(counter))
    #Random rectangle color
    randColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    print("Color:", randColor)

    #Random rectangle size
    randWidth = random.randint(10,50)
    randHeight = random.randint(10,50)
    print("Width:", randWidth)
    print("Height:", randHeight)

    #Random rectangle position
    randX = random.randint(0,WIDTH-randWidth)
    randY = random.randint(0,HEIGHT-randHeight)
    print("X:", randX)
    print("Y:", randY)
    
    pygame.draw.rect(screen, randColor, [randX, randY, randWidth, randHeight])
    
    counter += 1

pygame.display.flip()
print()
print("DONE! :)")
