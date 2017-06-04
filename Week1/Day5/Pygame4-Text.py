#!/usr/bin/python3.6

import pygame, sys
from pygame.locals import *

pygame.init()  										# activates Pygame, always the first command after import statements
DISPLAYSURF = pygame.display.set_mode((400, 300))	# creates a surface object of size width x height
pygame.display.set_caption('Hello World!')			# sets the text at the top of the window

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True:  										# main game loop: 1) handles events, 2) updates game state, 3) draws game state to screen
	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	for event in pygame.event.get():				# event handling: checks to see if certain events have occurred
		if event.type == QUIT:
			pygame.quit()							# deactivates Pygame...opposite of pygame.init()
			sys.exit()								# terminates program
	pygame.display.update()							# draws the surface object held by the DISPLAYSURF variable
