import pickle
from Pokemon import Pokemon
from Player import Player
from PokedexBuilder import PokedexBuilder
from Nature import Nature


class Builder:
    def __int__(self):
        self.name=test
    
    def TestBuild(self):
        print("creating player")
        #builds the Pokedex
        Pokedex=PokedexBuilder()
        #builds the natures
        self.Natures=[]
        reader= csv.reader(open('Natures.csv',newline=''))
        count=0
        for row in reader:
            print(row)
            self.Natures[count]=[row]
        reader.close()
        Nature        
        self.x=input("Players name is \n:")
        player= Player(self.x,22,"M",Pokedex.pokeDex)
        for number in range(16):
            player.Capture(Pokedex.pokeDex[number%9])
        player.check_party()
        player.check_box_system()
