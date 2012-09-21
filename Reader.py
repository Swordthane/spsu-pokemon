import csv
from Pokemon import Pokemon 
class read:
    def __init__(self):
        reader= csv.reader(open('Natures.csv',newline=''))
        for row in reader:
            print(row)
        #line=next(reader)
        #print(line)
        #line=next(reader)
        #print(line)
        #line=next(reader)
        print(line)
        #s1=Pokemon(line)
        #s1.ToString()
            
