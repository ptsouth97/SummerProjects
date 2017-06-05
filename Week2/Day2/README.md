# Week 2, Day 2

## How to Add Background Music to your App

  * import pygame, sys
  * pygame.init()
  * pygame.mixer.music.load('galactic-chase.wav')
  * pygame.mixer.music.play(-1, 0.0)
  * pygame.mixer.music.stop()
  * pygame.quit()

## Run the script
  * ./Pygame6-BackgroundMusic.py

## Change the music file
  * Find another .wav file on the internet
  * Replace the file in the directory and load it in the program

## Push changes to Github
  * cd ../..
  * git add .
  * git commit -m 'added new music file'
  * git push origin master
