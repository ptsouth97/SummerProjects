#!/usr/bin/python3.6

import pygame, sys
from pygame.locals import *

pygame.init()  													# activates Pygame, always the first command after import statements

pygame.mixer.music.load('galactic-chase.wav')
pygame.mixer.music.play(-1, 0.0)

joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
	# No joysticks!
	print('Error, I did not find any joysticks.')
else:
	my_joystick = pygame.joystick.Joystick(0)
	my_joystick.init()



FPS = 30														# frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)		# creates a surface object of size width x height
pygame.display.set_caption('Animation')							# sets the text at the top of the window

WHITE = (255, 255, 255)
RED =   (255,   0,   0)
 
fireball = pygame.image.load('fireball.png')
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
ballx = 380
bally = 150
balldirection = 'left'
jump = False


while True:														# main game loop: 1) handles events, 2) updates game state, 3) draws game state to screen
	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(catImg, (catx, caty))						# blit: draws contents of surface to another... copy cat image to surface object
	
	if balldirection == 'left':
		pygame.draw.circle(DISPLAYSURF, RED, (ballx, bally), 20)
		ballx -= 5
		if ballx <=20:
			balldirection = 'right'

	if balldirection == 'right':
		pygame.draw.circle(DISPLAYSURF, RED, (ballx, bally), 20)
		ballx += 5
		if ballx >=380:
			balldirection = 'left'

	for event in pygame.event.get():							# event handling: checks to see if certain events have occurred
		if event.type == QUIT or my_joystick.get_button(8) > 0:
			pygame.mixer.music.stop()
			pygame.quit()										# deactivates Pygame...opposite of pygame.init()
			sys.exit()											# terminates program
		elif event.type == KEYDOWN:
			if event.key in (K_RIGHT, K_d):
				if catx <= 280:
					catx +=10
			if event.key in (K_LEFT, K_a):
				if catx >= 10:
					catx -=10
			if event.key in (K_UP, K_w):
				if caty >= 10: 
					caty -=10
			if event.key in (K_DOWN, K_s):
				if caty <= 220:
					caty +=10
			if event.key in (K_SPACE, K_x):
				DISPLAYSURF.blit(fireball, (catx-60, caty))
		
		elif event.type == pygame.JOYBUTTONDOWN:
			# FIREBALL
			X = my_joystick.get_button(0)
			if X > 0:
				DISPLAYSURF.blit(fireball, (catx-60, caty))			

			# JUMP
			A = my_joystick.get_button(1)
			if A > 0:
				caty -= 10
				jump=True
				pygame.display.update()
				fpsClock.tick(FPS)
				
				pygame.time.wait(250)
				catx += 10
				pygame.display.update()
				fpsClock.tick(FPS)
				'''break'''
				

			# UNDECIDED BUTTONS
			B = my_joystick.get_button(2)
			Y = my_joystick.get_button(3)

			# EXIT
			select = my_joystick.get_button(8)

			# PAUSE
			start = my_joystick.get_button(9)
			'''if start > 0:
				pause = True
				paused()'''
		
		elif event.type == pygame.JOYAXISMOTION:
			
			leftRight = my_joystick.get_axis(0)
			if leftRight > 0:
				catx += 10
			if leftRight < 0:
				catx -= 10

			upDown= my_joystick.get_axis(1)
			if upDown > 0:
				caty += 10
			if upDown < 0:
				caty -= 10

	
	pygame.display.update()										# draws the surface object held by the DISPLAYSURF variable
	fpsClock.tick(FPS)

