#!/usr/bin/python
import pygame
import sys
from pygame.locals import * 

pygame.init ()

# vars 
FPS = 60
#celTableValue = 
red  = (225,0,0)
cyean = (0,255,255)
pygame.mouse.set_visible(False)
#####################################################
#startx = 100
#starty = 400
#coords = [{"x":startx,"y"starty}]
#newCell = {"x":coords[0]["x"]+1,"y":coords[0]["y"]}
#coords.insert (0,newCell)
#speed = 10
#moving objects using cel talbe vaule 
#####################################################
setDisplay = pygame.display.set_mode((320,500))
pygame.display.set_caption("Ping pong")

setDisplay.fill (cyean)

pixleJump = 20 
Left = "left"
Right = "right"

image = pygame.image.load("images/pad.png").convert_alpha()
imagex = 100
imagey = 400

setDisplay.unlock()
fpsTime = pygame.time.Clock()
while True:
	setDisplay.blit(image,(imagex,imagey))

   	for event in pygame.event.get():
		#print event
		if event.type ==QUIT:
			sys.exit()
			pygame.quit()

		elif(event.type == KEYDOWN and event.key == K_RIGHT):
           	 #print ("hellow")
			 imagex+= pixleJump
		pygame.display.update()
		setDisplay.fill(cyean)
  		
  		if(event.type == KEYDOWN and event.key == K_LEFT):
           	 #print ("hellow")
			 imagex-= pixleJump
		#pygame.display.update()
		setDisplay.fill(cyean)
       
        



fpsTime.tick(FPS) 
