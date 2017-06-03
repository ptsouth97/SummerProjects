#!/usr/bin/python3.6

import pygame, sys
from pygame.locals import *

pygame.init()  										# activates Pygame, always the first command after import statements

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 400))	# creates a surface object of size width x height
pygame.display.set_caption('Drawing')				# sets the text at the top of the window

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# draw on the surface object
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146,0), (291,106), (236,277), (56,277), (0,106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60,60), (120,60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120,60), (60,120))
pygame.draw.line(DISPLAYSURF, BLUE, (60,120), (120,120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300,50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

# run the game loop
while True:  										# main game loop: 1) handles events, 2) updates game state, 3) draws game state to screen
	for event in pygame.event.get():				# event handling: checks to see if certain events have occurred
		if event.type == QUIT:
			pygame.quit()							# deactivates Pygame...opposite of pygame.init()
			sys.exit()								# terminates program
	pygame.display.update()							# draws the surface object held by the DISPLAYSURF variable
