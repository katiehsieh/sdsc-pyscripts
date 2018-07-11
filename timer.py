import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

# Screen size
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Timer")

# Loop until done
done = False
clock = pygame.time.Clock()
font = pygame.font.Font(None, 100)

frameCount = 0
frameRate = 60
startTime = 90

# --------------- Main Program Loop ---------------

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    # Calculate total seconds
    totalSeconds = frameCount // frameRate
    # Calculate minutes
    minutes = totalSeconds // 60
    # Modulus to get seconds
    seconds = totalSeconds % 60

    # Use python string formatting to format in leading zeros
    outputString = "Time: {0:02}:{1:02}".format(minutes, seconds)

    # Blit to the screen
    text = font.render(outputString, True, BLACK)
    screen.blit(text,[100,125])

    totalSeconds = startTime - (frameCount // frameRate)
    if totalSeconds < 0:
        totalSeconds = 0

    minutes = totalSeconds // 60
    seconds = totalSeconds % 60

    outputString = "Time left: {0:02}:{1:02}".format(minutes, seconds)
    text = font.render(outputString, True, BLACK)
    screen.blit(text,[100,275])

    frameCount += 1
    clock.tick(frameRate)
    pygame.display.flip()
    

pygame.quit()
