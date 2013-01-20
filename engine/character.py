from client import client
from environment import environment
from environment import video
from environment import sound

class character(client):
    def __init__ (name, self):
        pass

    #self.stats = stats
    #self.item = item
    #self.sprite = sprite

class stats(dict):
    def __init__(self):
        pass

class item(dict):
    def __init__(self):
        pass

class sprite(video, sound):
    def __init__(self):
        pass
