from Pokemon import Pokemon
from Player import Player
from PokedexBuilder import PokedexBuilder
class WildGenerator:
    def __init(self,pkdex):
        self.pokedex=pkdex

    def generator(self,level,dnum):
        self.level=level
        self.dexnum=dnum
        
        newpk=self.pokedex[dnum+1]#makes a 0 based system a one based
        #http://bulbapedia.bulbagarden.net/wiki/Stats
