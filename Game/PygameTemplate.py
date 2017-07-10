#!/usr/bin/python3.6

import pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 400
WINDOWHEIGHT = 300

# Colors
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
BGCOLOR = WHITE

def main():
	global FPSCLOCK, DISPLAYSURF
	pygame.init()  										# activates Pygame, always the first command after import statements
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	FPSCLOCK = pygame.time.Clock()
	pygame.display.set_caption('caption goes here')		# sets the text at the top of the window
	DISPLAYSURF.fill(BGCOLOR)

	while True:  										# main game loop: 1) handles events, 2) updates game state, 3) draws game state to screen
		DISPLAYSURF.fill(BGCOLOR)
		for event in pygame.event.get():				# event handling: 
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()							# deactivates Pygame...opposite of pygame.init()
				sys.exit()								# terminates program
		pygame.display.update()							# draws the surface object held by the DISPLAYSURF variable
		FPSCLOCK.tick(FPS)

if __name__ == '__main__':
	main()
