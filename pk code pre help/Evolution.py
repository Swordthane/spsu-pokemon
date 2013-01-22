from Pokemon import Pokemon
import PokedexBuilder 
class Evolution:
    def __init__(self,pokdex):
        Poke_Dex=pokdex

    def Evolution(self,target,code):#code 0 means only one evol path 1 means multi
        temp=Poke_Dex[target.Dex_Num+1]
        if(code==0):
            if(target.Evolution_Type==target.Held_Item):
                target.Held_Item=""

            temp2=Poke_Dex[temp.Evolution[1]]#blank target for evolution
            if(target.Name==temp.Name):#checkes to see if there is a nickname
                target.Name=temp2.Name#no nick name change the name

            target.Base_HP = temp2.Base_HP
            target.Base_Attack = temp2.Base_Attack
            target.Base_Defence = temp2.Base_Defence
            target.Base_Special_Attack = temp2.Base_Special_Attack
            target.Base_Special_Defence = temp2.Base_Special_Defence
            target.Base_Speed = temp2.Base_Speed
            target.Dex_Num = temp2.Dex_Num
            target.Catch_Rate = temp2.Catch_Rate
            
            
            
