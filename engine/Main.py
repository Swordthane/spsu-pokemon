import threading


class runner(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.counter=0
		
	def run(self):
		while(self.counter<100):
			print(self.counter)
			self.counter+=1
			
background = runner()
background.start()

while(x>0):
	print(x)
	x-=1

background.join()
print("done")