#!/usr/bin/python3.6

import pygame, sys
from pygame.locals import *

pygame.init()
pygame.mixer.music.load('galactic-chase.wav')
pygame.mixer.music.play(-1, 0.0)

FPS = 30														
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)		
pygame.display.set_caption('Flip')							

WHITE = (255, 255, 255)
 
catImg = pygame.image.load('cat.png')
flippedCat = pygame.transform.flip(catImg, True, True)
catx = 280
caty = 150
catdirection = 'left'


while True:														
    DISPLAYSURF.fill(WHITE)

    if catdirection == 'left':
        DISPLAYSURF.blit(catImg, (catx, caty))
        catx -= 5
        if catx <=5:
            catdirection = 'right'
			
    if catdirection == 'right':
        DISPLAYSURF.blit(flippedCat, (catx, caty))
        catx += 5
        if catx >=280:
            catdirection = 'left'

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mixer.music.stop()
            pygame.quit()										
            sys.exit()											

    pygame.display.update()										
    fpsClock.tick(FPS)

