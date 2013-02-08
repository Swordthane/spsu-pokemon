import threading, csv
import random, sys, copy, os, pygame
from pygame.locals import *
#class worldbuilder(threading.Thread):
#16X16 grid size
class worldbuilder:
	def __init__(self):
		print ("starting")
		#threading.Thread.__init__(self)
	def run(self):
		x=input("what are you doing?")#
		if(x=="M"):
			x=input("what is the name of this section?")
			self.section_name=x
			x=input("Backround image location?")
			self.backround=pygame.image.load(x)
			for x in range(16):
				if((self.backround.get_width()+x)%16==0):
					self.width_section=self.backround.get_width()+x
					print ("width:",self.backround.get_width()+x)
			for x in range(16):
				if((self.backround.get_height()+x)%16==0):
					self.height_section=self.backround.get_height()+x	
					print("Height",self.backround.get_height()+x)
				
				
			print("width ",self.width_section," Hight ",self.height_section)
			x=input("do wou wish to create meta data?")
			if(x=="Y"):
			
			
				self.meta_data=open(self.section_name+"meta.csv","w")
				self.writer= csv.writer(self.meta_data)
				
				
				#Meta_writer = csv.writer(open(self.meta_data, 'wb'))
				
				
				print("made file")
			
				y=0
				print("made row")
				row=([0] * int(self.width_section/16))
				self.writer.writerow(row)
				self.writer.writerow(row)
				self.writer.writerow(row)
				self.writer.writerow(row)
				self.writer.writerow(row)
				#while(y<(self.height_section/16)):
				#	self.writer.writerow(row)
				#	y+=1
					
				self.meta_data.close()
				print("done writing")
				x='C'
			if(x=='C'):
				reader= csv.reader(open("boymeta.csv", 'r'))
				print("read check")
				for row in reader:
					print(reader)
x=worldbuilder()
x.run()

print("done")