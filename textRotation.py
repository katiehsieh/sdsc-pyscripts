import pygame

pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

PI = 3.141592653

size = [800, 800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rotate Text")

done = False
clock = pygame.time.Clock()
textRotateDegrees = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear screen
    screen.fill(WHITE)

    # Draw some borders
    pygame.draw.line(screen, BLACK, [100,50], [700,50], 5)
    pygame.draw.line(screen, BLACK, [100,50], [100,700], 5)
    
    pygame.draw.line(screen, BLUE, [200, 400], [700, 400], 5)
    pygame.draw.line(screen, BLUE, [200, 400], [200, 700], 5)
    font = pygame.font.SysFont('Lato', 50, True, False)

    text = font.render("Sideways text", True, RED)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, [105,55])
    
    text = font.render("Upside Down text", True, GREEN)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, [200,55])

    text = font.render("Flipped text", True, BLUE)
    text = pygame.transform.flip(text, False, True)
    screen.blit(text, [200,200])

    text = font.render("Flipped text", True, BLUE)
    text = pygame.transform.flip(text, True, False)
    screen.blit(text, [200,300])

    text = font.render("Rotating Degrees", True, BLACK)
    text = pygame.transform.rotate(text, textRotateDegrees)
    textRotateDegrees += 1
    screen.blit(text, [205,405])
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
