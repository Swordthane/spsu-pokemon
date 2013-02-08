import random, pygame, sys, time
from pygame.locals import *


class world viewer:
	def __init__(self):
		WINDOWWIDTH = 640
		WINDOWHEIGHT = 480
		CELLSIZE = 16
		CELLWIDTH=CELLSIZE
		CELLHEIGHT=CELLSIZE
		DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
		BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
		pygame.display.set_caption('world viewer')
		
		ImageDict= {'map':pygame.image.load}