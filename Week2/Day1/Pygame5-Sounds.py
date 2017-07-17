/usr/bin/python3.6

import pygame, sys
from pygame.locals import *
import time

pygame.init()
soundObj = pygame.mixer.Sound('beeps.wav')
soundObj.play()
time.sleep(1) 	# wait and let the sound play for 1 second
soundObj.stop()
pygame.quit()
