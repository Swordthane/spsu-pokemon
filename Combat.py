from Pokemon import Pokemon
from HumanPlayer import HumanPlayer
#this class is for pve
class Combat:
    def __init__(self, player, NPC, weather):
        self.Player=player
        self.NPC=NPC
        self.WeatherCondition=weather

    def NormalCombat(self):
        temp=0
        print(self.Player.name," is ready to fight")
        if(len(self.player.party>0):
            print("GO! ",self.player.party[0])
