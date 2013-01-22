import random

class Pokemon():

    Stones=["FireStone","ThunderStone","WaterStone","DawnStone","DuskStone",
            "MoonStone","SunStone","LeafStone"]
    def __init__(self,data):
        
        self.Dex_Num=int(data[0])
        self.Name=data[1]
        self.Name_Original=data[1]#use to verify what nicknamed pk realy is
        self.Level=0
        self.Lengindary=False #where should this come from it might not be the dex
        
        self.Type_1=data[2]#strings can be null
        self.Type_2=data[3]
        self.Type_3=data[4]
        
        #used to caluclate stats ints cant be null
        self.Base_HP=int(data[5])
        self.Base_Attack=int(data[6])
        self.Base_Defence=int(data[7])
        self.Base_Special_Attack=int(data[8])
        self.Base_Special_Defence=int(data[9])
        self.Base_Speed=int(data[10])

        #one of 3 will be picked
        self.Potential_Ability_1=data[11]
        self.Potential_Ability_2=data[12]
        self.Potential_Ability_3=data[13]
        
        self.Base_XP=int(data[14])#used for when faint
        
        #are ints and can be null all nulls are changed to 0's
        
        try:
            self.EV_HP=int(data[15])
        except:
            self.EV_HP=0        
        try:
            self.EV_Attack=int(data[16])
        except:
            self.EV_Attack=0
        try:
            self.EV_Defence=int(data[17])
        except:
            self.EV_Defence=0      
        try:
            self.EV_Special_Attack=int(data[18])
        except:
            self.EV_Special_Attack=0 
        try:
            self.EV_Special_Defence=int(data[19])
        except:
            self.EV_Special_Defence=0
        try:
            self.EV_Speed=int(data[20])
        except:
            self.EV_Speed=0
                
        
        
        
        
        
        
        #int not null
        self.Catch_Rate=int(data[21])
        
        self.Hight=float(data[22])
        self.Weight=float(data[23])

        self.Gender_Ratio=0# float(data[24])#chance pk is male and -1 is non genderd
        self.Evolution=data[25].split()#first is the evolution
        try:
            self.Evolution_Type=int(self.Evolution[0])#used if evol by level up
        except:
            self.Evolution_Type=self.Evolution[0]#any other method
        
            
        


        
        self.Max_XP=int(data[26])#xp to reach lvl 100
        self.Current_XP=0

        #these are generated at time of creation
        
        self.IV_HP = random.randrange(1,32)
        self.IV_Attack = random.randrange(1,32)
        self.IV_Defence = random.randrange(1,32)
        self.IV_Special_Attack = random.randrange(1,32)
        self.IV_Special_Defence = random.randrange(1,32)
        self.IV_Speed = random.randrange(1,32)

        self.Nature=1#needs some work

        self.Ability_Num=0    #this picked the abllity it will use if there is no 2nd or 3rd defults to one
        self.Gender=""
        self.Shiny=False

        #these will me filled in during the leveling code
        self.HP=0
        self.Attack=0
        self.Defence=0
        self.Special_Attack=0
        self.Special_Defence=0
        self.Speed=0

        self.Current_HP=0#how much hp you have left at 0 you are fainted
      
        #these need more class
        self.Held_Item=""
        self.Ability=''


        #these need more data!!!
        self.Attack_List=[]#fill with the attack # it can learn possibly tuples (attack,lvl/th/hm/other)
        self.Known_Attacks=[]#fill with attacks known


        self.Stats_Calc()

        

    def ToString(self):#must not hate this to string
        print("Dex#",self.Dex_Num,"Name",self.Name,"Level",self.Level,"type1",self.Type_1,"2",self.Type_2,"3",self.Type_3,
                "Base HP",self.Base_HP,"Attack",self.Base_Attack,
                "Defence",self.Base_Defence,"SAttack",self.Base_Special_Attack,"SDefence",self.Base_Special_Defence,
                "Speed",self.Base_Speed,"Poten1",self.Potential_Ability_1,"p2",self.Potential_Ability_2,
                "p3",self.Potential_Ability_3,"Base_XP",self.Base_XP,"EV_HP",self.EV_HP,"att",self.EV_Attack,
                "def",self.EV_Defence,"satt",self.EV_Special_Attack,"sdef",self.EV_Special_Defence,"speed",self.EV_Speed,
                "CatchR",self.Catch_Rate,"Hight",self.Hight,
                "weight",self.Weight,"G/R",self.Gender_Ratio,"Evol",self.Evolution,"max xp",self.Max_XP,
                "IV_HP",self.IV_HP,"IV_att",self.IV_Attack ,"def",self.IV_Defence,"satt",self.IV_Special_Attack,
                "sdeff",self.IV_Special_Defence,"sp",self.IV_Speed)
    def Stats_Calc(self):
        self.HP=(((self.IV_HP+(2*self.Base_HP)+(self.EV_HP/4)+100)*self.Level)/100)+10
        self.Attack=((((self.IV_Attack+(2*self.Base_Attack)+(self.EV_Attack/4)+100)*self.Level)/100)+5)*self.Nature
        self.Defence=((((self.IV_Defence+(2*self.Base_Defence)+(self.EV_Defence/4)+100)*self.Level)/100)+5)*self.Nature
        self.Special_Attack=((((self.IV_Special_Attack+(2*self.Base_Special_Attack)+(self.EV_Special_Attack/4)+100)*self.Level)/100)+5)*self.Nature
        self.Special_Defence=((((self.IV_Special_Defence+(2*self.Base_Special_Defence)+(self.EV_Special_Defence/4)+100)*self.Level)/100)+5)*self.Nature
        self.Speed=((((self.IV_Speed+(2*self.Base_Speed)+(self.EV_Speed/4)+100)*self.Level)/100)+5)*self.Nature
        print("HP",self.HP,"Attack",self.Attack,"Defence",self.Defence,"SAttack",self.Special_Attack,
              "SDef",self.Special_Defence,"Speed",self.Speed)
        
    def Level(self , level):
        if(self.Level>level or self.Level==level):
            print("error")
        self.Level=level
        if(self.Evolution_Type == self.Level or self.Evolution_Type <self.Level):
            self.Evolution(self,0)#wont work as method is no longer in pk
            print("evolved")
        elif(self.Evolution_Type=="!!!"):
            #self.Evolution(self,1)
            print("")
        elif(self.Evolution_Type==self.Held_Item):
            self.Evolution(self,0)
            print("ev")
        else:
            print("")
        self.Stats_Calc()
            
    def Evolution_Check_Stone(self,target,stone):
        if (target.Evolution_Type in stone):
            return True
        else:
            return False
