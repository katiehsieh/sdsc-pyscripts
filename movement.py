import pygame, math, random

pygame.init()

WHITE = (255,255,255)
YELLOW = (255,255,0)
red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)
COLOR = (red,green,blue)
delta = 1

clock = pygame.time.Clock()
size = [700,500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Movement Ideas")

screen.fill(WHITE)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    for x in range(50,400,5):
        red += delta
        if red > 255:
            delta *= -1
            red = 255
        elif red < 0:
            delta *= -1
            red = 0
        
        COLOR = (red,green,blue)
        
        pygame.draw.rect(screen,COLOR,[x,100,80,80],0)
        pygame.display.flip()
        screen.fill(WHITE)
        clock.tick(60)
        
    for x in range(400,50,-5):
        red += delta
        if red > 255:
            delta *= -1
            red = 255
        elif red < 0:
            delta *= -1
            red = 0
        
        COLOR = (red,green,blue)
        
        pygame.draw.rect(screen,COLOR,[x,100,80,80],0)
        pygame.display.flip()
        screen.fill(WHITE)
        clock.tick(60)
        red += 1

pygame.quit()
