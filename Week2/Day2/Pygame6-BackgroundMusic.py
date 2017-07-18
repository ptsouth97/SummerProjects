#!/usr/bin/python3.6

import pygame, sys
from pygame.locals import *

pygame.init()  													# activates Pygame, always the first command after import statements

pygame.mixer.music.load('slay.wav')
pygame.mixer.music.play(-1, 0.0)

FPS = 30														# frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((1980,1080), 0, 32)		# creates a surface object of size width x height
pygame.display.set_caption('Animation')							# sets the text at the top of the window

WHITE = (255, 255, 255)
catImg = pygame.image.load('knight.png')
catx = 10
caty = 10
direction = 'right'

while True:  													# main game loop: 1) handles events, 2) updates game state, 3) draws game state to screen
	DISPLAYSURF.fill(WHITE)

	if direction == 'right':
		catx += 5
		if catx == 280:
			direction = 'down'
	elif direction == 'down':
		caty += 5
		if caty == 220:
			direction = 'left'
	elif direction == 'left':
		catx -= 5
		if catx == 10:
			direction = 'up'
	elif direction == 'up':
		caty -= 5
		if caty == 10:
			direction = 'right'

	DISPLAYSURF.blit(catImg, (catx, caty))						# blit: draw the contents of one surface onto another...e.g. copy the cat image to surface object

	for event in pygame.event.get():							# event handling: checks to see if certain events have occurred
		if event.type == QUIT:
			pygame.mixer.music.stop()
			pygame.quit()										# deactivates Pygame...opposite of pygame.init()
			sys.exit()											# terminates program
	pygame.display.update()										# draws the surface object held by the DISPLAYSURF variable
	fpsClock.tick(FPS)
