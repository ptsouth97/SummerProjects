#!/usr/bin/python3.6

import pygame, sys
from pygame.locals import *

pygame.init()  										# activates Pygame, always the first command after import statements
DISPLAYSURF = pygame.display.set_mode((400, 300))	# creates a surface object of size width x height
pygame.display.set_caption('Hello World!')			# sets the text at the top of the window

mousex = 0
mousey = 0

while True:  										# main game loop: 1) handles events, 2) updates game state, 3) draws game state to screen
	for event in pygame.event.get():				# event handling: get() makes a list and for loop checks to see if certain events have occurred
		if event.type == QUIT:
			pygame.quit()							# deactivates Pygame...opposite of pygame.init()
			sys.exit()								# terminates program
		elif event.type == MOUSEMOTION:
			mousex, mousey = event.pos
		elif event.type == MOUSEBUTTONUP:
			print('Hey you clicked me!')
			pygame.time.wait(500)
		elif event.type == KEYDOWN:
			if event.key in (K_UP, K_w):
				print('You pressed up')
				pygame.time.wait(500)
			if event.key in (K_DOWN, K_s):
				print('You pressed down')
				pygame.time.wait(500)

	print('{}, {}'.format(mousex, mousey))
	pygame.display.update()							# draws the surface object held by the DISPLAYSURF variable

