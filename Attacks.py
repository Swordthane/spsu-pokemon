class Attacks:
    def __init__(self, line):
        self.Number=line[0]
        self.Name=line[1]
        self.Description=line[2]
        self.Type1=line[3]
        self.Move_Type=line[4]#special or physical
        if(self.Move_Type=="Special"):
            self.Special_Attack=line[5]
        else:    
            self.Attack=line[5]

        self.Accuracy=line[6]
        self.PP=line[7]
        self.Move_Order=line[8]#1 goes first, -# go last


        self.Effect_Chance=line[9]#2 numbers that are splitable aks seperated by a space
        self.Targets=line[10]
        #1=both user, 2 Either Opponetnt, 3 both opponents, 4 both apponents and partner,5 all
        #null field target one opponet


        
