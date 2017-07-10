# Week 1, Day 1

## Your goal today is to learn how to edit and run python scripts using VIM and the command line
## Hint: you can open multiple terminal windows so you can read the instructions and do them at the same time

## Figure out your python version
  * From the command line type 'python3'
  * This will tell you which version of python 3 is on your system
  * Write down the version (e.g., python 3.2) so you don't forget it
  * Stop python by pressing 'ctrl-z'

## Update the file with your python version
  * Open the file in this directory by typing 'vim test.py' (don't forget you can use tab to autocomplete)
  * Press 'i' to enter 'insert mode'
  * The very first line needs to tell the script which interpreter should run the script
  * Type the shebang:  '#!'  This just means I'm going to tell you which program to use
  * Then right after the shebang (no spaces), type '/usr/bin/python3.X' where 3.X is the version on your system
  * Press 'Esc' to enter 'command mode'
  * Press 'wq' followed by enter to 'Write then Quit' (it's just saving and exiting)

## Execute the script
  * Give yourself permission to execute the script by typing 'chmod +x test.py'
  * Execute the script by typing './test.py'
  * Did it work?  If not, figure out what you did wrong.
  * Once it's working, navigate back to the SummerProjects folder 'cd ../..'  (go back two folder levels)

## Push your changes to github so I can check them:
  * 'git add .'  adds all changes you made
  * 'git commit -m "I updated the script"  '   ('-m' creates a message that goes with the commit)
  * 'git push origin master'
  * You can login to your [github](https://github.com/) account to verify the changes

