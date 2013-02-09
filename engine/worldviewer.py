import random, pygame, sys, time
from pygame.locals import *


class worldviewer:
	def __init__(self):
		x=input("target is?")
		self.backround=pygame.image.load(x)
		print ("backround loaded")
		self.WindowWidth=self.backround.get_width()
		self.WindowHeight=self.backround.get_height()
		for x in range(16):
			if((self.backround.get_width()+x)%16==0):
				self.width_section=self.backround.get_width()+x
				print ("width:",self.backround.get_width()+x)
		for x in range(16):
			if((self.backround.get_height()+x)%16==0):
				self.height_section=self.backround.get_height()+x	
				print("Height",self.backround.get_height()+x)
				
		self.WindowWidth = 640
		self.WindowHeight= 480
		self.CellSize = 16
		CELLWIDTH=self.CellSize
		CELLHEIGHT=self.CellSize
		DISPLAYSURF = pygame.display.set_mode((self.WindowWidth, self.WindowHeight))
		#BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
		pygame.display.set_caption('world viewer')
		DISPLAYSURF.fill((255,255,255))
		DISPLAYSURF.blit(self.backround, (0,0))
		pygame.display.update()
		x=0
		while(x<10000000):
			x+=1
		#for event in events: 
			#if event.type == QUIT: 
				#sys.exit(0) 
				
Y=worldviewer()
#Y.run()
print("done")