# Week 1, Day 2

* Today's goal is to get [Pygame](https://www.pygame.org) working on the Raspberry Pi
* This could be the most frustrating part, so be patient

* First let's check if Pygame is already installed
  * Open a terminal with 'ctrl-t'
  * Remember the python distribution from yesterday? Type 'python3.X' where X is the version number
  * You are now in the python command line
  * Type 'import pygame'
  * If there's no error, it's already installed and you can skip the next section
  * Type 'ctrl-z' to stop python command line

* Install pygame
  * 'python3.X -m pip install pygame --user'  again, X is your python version
  * If it doesn't install, let me know or try to troubleshoot on your own

* Test the installation
  * './Pygame1-Test.py'
  * You should see a black window pop up that says 'Hello World'
  * Change the code with Vim so that it says 'Hello Dad' instead 
  * Change the size of the box to '800x600'

* Push your changes to Github
  * git add .
  * git commit -m 'made some changes'
  * git push origin master
