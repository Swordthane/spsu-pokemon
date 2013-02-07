import threading, csv
import random, sys, copy, os, pygame
from pygame.locals import *
#class worldbuilder(threading.Thread):
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
			self.width_section=self.backround.get_width()
			self.height_section=self.backround.get_height()
			print("width ",self.width_section," Hight ",self.height_section)
			x=input("do wou wish to create meta data?")
			if(x=="Y"):
				self.meta_data=self.section_name+"meta.csv"
				Meta_writer = csv.writer(open(self.meta_data, 'wb'))
				print("made file")
			
				y=0
				print("made row")
				while(y<self.height_section):
					Meta_writer.writerow(([0] * self.width_section))
					y+=1
				print("done writing")
				x='C'
			if(x=='C'):
				reader= csv.reader(open("boymeta.csv", 'rb'))
				print("read check")
				y=0
				while(y<self.height_section):
					line=next(reader)
					print(line)
					y+=1
				
x=worldbuilder()
x.run()

print("done")