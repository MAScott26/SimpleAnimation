# SimpleAnimation
define main
import pygame
initialize pygame

boxUp = True
boxRight = True

set screen sizre
set display caption
set background surface as screensize
load background image
convert background image
set background image size to screen size

create 2nd surface for moving box,
 box becomes loaded image
 image gets converted to become transparent
 image size becomes 100x100.

 defailt box position gets
 x = 0
 y = 200

 clock = pygame clock

 keepgoing = True
 keySwitch = False

   while keepGoing

   keys = pygame keys pressed

   FPS = 30

   if pgygame x is pressed, quit game

   if boxRight is true
     box moves right
    else, box moves left

  if boxUp is true
  box moves up
  else, box move down

if Space is pressed
  Switch directions of boxRight


  blit background.
  blit box
  display flip
pygame.quit.

if__name__ is __main__
main()
main()
