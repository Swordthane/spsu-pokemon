from client import client

class video:
    def __init__ (self, file, coords):
        pass

    def draw (self):
        pass

    def erase (self):
        pass

class sound:
    def __init__ (self, file):
        pass

    def play (self):
        pass

    def pause (self):
        pass

class tile (video, sound):
    def __init__(self):
        pass

class event:
    def __init(self):
        pass

class environment (client):
    def __init__ (self):
        pass

    #self.video = video
    #self.sound = sound
    #self.tiles = tile
    #self.events = event
