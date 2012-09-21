from Pokemon import Pokemon
from uuid import uuid4
from PokeDexPlayer import PokeDexPlayer
class Player (dict): #TODO
    def __init__(self, name, age, sex,pkdex):
        self.name = name
        self.age  = age
        self.sex  = sex
        self.pokedex=PokeDexPlayer(pkdex)

        self.current = 0#box currently reseving
        self.party = [0]
        self.boxes = [[],[],[],[],[],[],[],[],[],[],[],[]]#there needs to be a better way of doing this old way did not work
        self.UID = uuid4() #works better as a way to get truly unique IDs

        self.max_party=3
        self.pokemon_owned=0#number total
        self.pokemon_in_party=0#number in party
        
    def Capture(self,pk):
        #print("Congratulations you have captured {}".format(pk.name))
	#x=input("would you like to give it a nickname?  Y/N \n")
        pk.UID=(self.UID.int)
        self.pokedex.Add_To_Dex(pk)
        if(self.pokemon_in_party == 0):
            #player has no pokemon add to first postion
            self.party[0]=pk
            self.pokemon_in_party+=1
            #print("Party size",self.pokemon_in_party) 
            #print("first {} to party".format(self.party[0].name))
        elif(self.pokemon_in_party+1 > self.max_party):
            #send pokemon to box
            #print("send to box system")
            Player.add_pokemon_box(self,pk)
        else:
            #there is space in party 
            self.party.append(pk)
            self.pokemon_in_party +=1
            #print("added {} to party".format(pk.name))
            #print("Party size",self.pokemon_in_party) 
    #prints the players party
    def check_party(self):
        print("Check Party")
        for count in self.party:
            print(count.name)

    #adds pokemon to first avalible box        
    def add_pokemon_box(self, pk):
        done=False
        while(done!=True):
            #for current in self.boxes: CODE not needed
            if(len(self.boxes[self.current])<5):
                self.boxes[self.current].append(pk)
                #print("add to box",self.current, pk.name)
                done=True
                    #above checks to see if there is space in box and puts pokemon in when true
                    
            else:
                #print("box:{} is full moving to next".format(self.current))
                self.current+=1
                #box was full. moves to new box and restarts loop

    #fixed your list of lists loop, needed more for's in it...XD, also I assume this is debug stuff
    def check_box_system(self):
        print("Check Box")
        for sub_list in self.boxes:
            for element in sub_list:
                #print ("test")
                print (element.name)
