import random, pygame, sys, time
from pygame.locals import *
import csv

class worldviewer:
	def __init__(self):
	
		pygame.init()
		self.FPSCLOCK = pygame.time.Clock()
		self.name_backround=input("target is?")
		self.backround=pygame.image.load(self.name_backround+".jpg")
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
				
		self.WindowWidth = 592
		self.WindowHeight= 784
		self.CellSize = 16
		CELLWIDTH=self.CellSize
		CELLHEIGHT=self.CellSize
		self.DISPLAYSURF = pygame.display.set_mode((self.WindowWidth, self.WindowHeight))
		#BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
		pygame.display.set_caption('world viewer')
		self.DISPLAYSURF.fill((255,255,255))
		self.DISPLAYSURF.blit(self.backround, (0,0))
		DARKGRAY  = ( 40,  40,	40)
		for x in range(0, self.WindowWidth, self.CellSize): # draw vertical lines
			pygame.draw.line(self.DISPLAYSURF, DARKGRAY, (x, 0), (x, self.WindowHeight))
		for y in range(0, self.WindowHeight, self.CellSize): # draw horizontal lines
			pygame.draw.line(self.DISPLAYSURF, DARKGRAY, (0, y), (self.WindowWidth, y))
		pygame.display.update()
		while True:
			self.player()
		
	def player(self):
		self.targets=[]
		self.teli=[]
		RED = (255,0,0)
		DARKGRAY  = ( 40,  40,	40)
		BLUE=(0,0,255)
		GREEN=(0,255,0)
		self.direction="stop"
		self.posx=16
		self.posy=16
		self.tposx=16
		self.tposy=16
		self.place_type="b"
		while True:
			for event in pygame.event.get(): 
				if (event.type == QUIT): 
					sys.exit(0) 
				if (event.type == MOUSEBUTTONUP):
					mouseX,mouseY = event.pos
					loc=((int(mouseX/16 ),int(mouseY/16)))#make a int that is divisable by 16
					if self.place_type=="b":
						if(loc in self.targets):
							self.targets.remove(loc)
						else:
							self.targets.append(loc)
							print(loc)
					if self.place_type=="t":
						#TP=input("where does this go")
						if(loc in self.teli):
							self.teli.remove(loc)
						else:
							self.teli.append(loc)
							print(loc)
						
						
						
				if event.type == KEYDOWN:
					if event.key == K_t:
						self.place_type="t"
						
					if event.key == K_b:
						self.place_type="b"
						
					if event.key == K_l:
						try:
							self.reader=csv.reader(open(self.name_backround+"meta.csv","r"))
							print("Loading")
							h=0
							w=0
							for line in self.reader:
								if(h%2==0):
									w=0
									for ele in line:
										if ele == 'b':
											self.targets.append((h/2,w))
											print(h/2,"+",w)
										w+=1
										
								h+=1
						except:
							print("no meta data found")
					if event.key == K_r:
							self.meta_data=open(self.name_backround+"meta.csv","w")
							self.writer= csv.writer(self.meta_data)
							print("writing")
							
							for height in range(int(self.WindowHeight/16)):
								row=[]
								for width in range(int(self.WindowWidth/16)):
									if(height,width)in self.targets:
										row.append('b')
										print(height,width)
									else:
										row.append(0)
								self.writer.writerow(row)
								
							self.meta_data.close()
				
				
			keyBord=pygame.key.get_pressed()#this does not get key order and is prioritsed in order of if statments 
				
				
				
			if keyBord[pygame.K_LEFT]:
				self.direction="left"
			elif keyBord[pygame.K_RIGHT] :
				self.direction="right"
			elif keyBord[pygame.K_UP]:
				self.direction="up"
			elif keyBord[pygame.K_DOWN]:
				self.direction="down"
			else:
				self.direction="stop"
			#print(self.direction)
			if self.direction=="left" :
				self.tposx += -16
			elif self.direction=="right" :			
				self.tposx += 16
			elif self.direction=="up" :
				self.tposy += -16
			elif self.direction=="down" :
				self.tposy += 16
				
			tloc=(self.tposx/16,self.tposy/16)
			if(tloc in self.targets):
				print ("collision")
				if self.direction == "left":
					self.tposx+=16
				elif self.direction == "right":
					self.tposx+=-16
				elif self.direction == "up":
					self.tposy+=16
				elif self.direction == "down":
					self.tposy+=-16
			elif(self.tposx<0):
				print("x>0")
				self.tposx=self.tposx+16
			elif(self.tposx>self.WindowWidth):
				print("self.tposx<=self.WindowWidth")
				self.tposx=self.tposx-16
			elif(self.tposy<0):
				print("self.tposy>=0")
				self.tposy=self.tposy+16
			elif(self.tposy>self.WindowWidth):
				print("self.tposy<=self.WindowWidth")
				self.tposy=self.tposy-16
			else:
				self.posx=self.tposx
				self.posy=self.tposy
					

				
			self.DISPLAYSURF.fill((255,255,255))
			self.DISPLAYSURF.blit(self.backround, (0,0))		
			for x in range(0, self.WindowWidth, self.CellSize): # draw vertical lines
				pygame.draw.line(self.DISPLAYSURF, DARKGRAY, (x, 0), (x, self.WindowHeight))
			for y in range(0, self.WindowHeight, self.CellSize): # draw horizontal lines
				pygame.draw.line(self.DISPLAYSURF, DARKGRAY, (0, y), (self.WindowWidth, y))			
			for cord in self.targets:
				x,y = cord 
				x=x*16#send to correct corner 
				y=y*16
				appleRect = pygame.Rect(x, y, self.CellSize, self.CellSize)
				pygame.draw.rect(self.DISPLAYSURF, RED, appleRect)
			for cord in self.teli:
				x,y = cord 
				x=x*16#send to correct corner 
				y=y*16
				appleRect = pygame.Rect(x, y, self.CellSize, self.CellSize)
				pygame.draw.rect(self.DISPLAYSURF, BLUE, appleRect)	
				
			#print("my loc", self.posx, ",",self.posy)	
			self.me = pygame.Rect(self.posx, self.posy, self.CellSize, self.CellSize)
			pygame.draw.rect(self.DISPLAYSURF, GREEN, self.me)
			pygame.display.update()		
			self.FPSCLOCK.tick(5)
Y=worldviewer()
#Y.run()
print("done")