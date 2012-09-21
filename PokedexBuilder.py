import pickle
from Pokemon import Pokemon
import csv
class PokedexBuilder:
    def __init__(self):
        print("Are we making or loading?")
        x=input("Make/LOAD?")
        x=x.upper()
        if(x=="MAKE"):
            x=input("What should it be named?")
            #FILE = open(("{}.txt".format(x)), "wb")
            print("Starting Generation")
            self.build()
            #print("Build completed do you wish to save or edit?")
            #pickle.dump(self.pokeDex,FILE)
            #FILE.close()

            
        elif(x=="LOAD"):
            print("Preparing to koad file")
            x=input("Target file name?")
            FILE = open(("{}.txt".format(x)), "rb")
            self.Poke_Dex=pickle.load(FILE)
            print("Build loaded doing build check")
            self.check()
            FILE.close()



            
        else:
            print("Invalid... \n Now closeing")

        

    def build(self):
        self.Poke_Dex=[]
        find=False
        x='stuff.csv'
        while(find!=True):
            try:
                reader= csv.reader(open(x,newline=''))
                find=True
            except:
                x=input("input File not found reenter file name and path")
            
        #for row in reader:
            #print(row, len(row))
        line=next(reader)
        line=next(reader)
        line=next(reader)#first pk
        for row in range(9):
            temp=Pokemon(line)
            self.Poke_Dex.append(temp)
            line=next(reader)
        #for row in reader:
            #temp=Pokemon(line)
            #self.Poke_Dex.append(temp)
            



        #print(line)
        #s1=Pokemon(line,22)
        #s1.ToString()

    def add_pk(self,pk):
        self.Poke_Dex.append(pk)
        print("Added pokemon to pokedex")

    def Edit(self):
        x=input("Who do you wish to edit?(#)")
        try:
            x=int(x)
        except ValueError:
            print("Failure to target")
        done=False
        target=SelfPpoke_Dex[x-1]
        self.Poke_Dex[x-1].tostring()
        while(done!=True):
            print("Imput what do you want to do")
            print("1:Change Name or DexNumber")#needs colioson handling
            print("2:Change Type")
            print("3:Change Stats")
            print("4:Change IV")
            print("5:Change Nature")
            print("6:Change Attacks")
            print("7:Change Leveling")
        






        
    
    def check(self):
        for element in self.Poke_Dex:
            #print("running")
            element.ToString()
