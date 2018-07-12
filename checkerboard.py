import pygame,sys,random,time,math

pygame.init()
screen = pygame.display.set_mode((640,640))
pygame.display.set_caption("CHECKER BOARD")

sfill = [255,255,255]
screen.fill(sfill)
black = (0,0,0)
red = (255,0,0)

color = black

for i in range(0,640,80):

    if color == red:
        color = black
    else:
        color = red

    for row in range(0,640,80):
        pygame.draw.rect(screen,color,pygame.Rect(row,i,80,80))
        if color == red:
            color = black
        else:
            color = red
    pygame.display.update()
