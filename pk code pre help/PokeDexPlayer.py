from Pokemon import Pokemon

class PokeDexPlayer:
    def __init__(self,pkdex):
        self.GameDex=pkdex#this is the games version
        self.PokeDex=[]#players
        for count in range(len(self.GameDex)):
            self.PokeDex.append("NF")#stands for not found
        print(len(self.GameDex),"number in game")

    def DexCheck(self,pk):
        if(self.PokeDex[pk.dexnumber]!="NF"):
            print("You already have {} in you Pokedex".format(pk.name))
            return True
        else:
            print("You do not have {} in you Pokedex".format(pk.name))
            return False

    def Add_To_Dex(self,pk):
        if(self.DexCheck(pk)==False):
            print(pk.name," added to dex")
            self.PokeDex[int(pk.dexnumber)]=pk
        else:
            print("already done")
