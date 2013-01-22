from Pokemon import Pokemon
import csv

class testbuilder:
    def __init__(self):
        x='stuff.csv'
        reader= csv.reader(open(x,newline=''))
        line=next(reader)
        line=next(reader)
        line=next(reader)#first pk
        self.temp=Pokemon(line)
        self.temp.ToString()
        self.temp.Level(16)
