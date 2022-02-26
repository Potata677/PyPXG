#imports de weas
import sys
from tkinter import *
import tkinter as tk
import numpy as np

#TABLA DE TIPOS
Normal = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5, 1]
Fire = [1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 2, 1]
Water = [1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 1, 1]
Electric = [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1, 1, 1]
Grass = [1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5, 1]
Ice = [1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0.5, 1]
Fighting = [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2, 0.5]
Poison = [1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 0, 2]
Ground = [1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2, 1]
Flying = [1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0.5, 1]
Psychic = [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 0, 0.5, 1]
Bug = [1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5, 0.5]
Rock = [1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5, 1]
Ghost = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 1]
Dragon = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5, 0]
Dark = [1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 0.5]
Steel = [1, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5, 2]
Fairy = [1, 0.5, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 2, 0.5, 1]
#list = [Normal, Fire, Water, Electric, Grass, Ice, Fighting, Poison, Ground, Flying, Psychic, Bug, Rock, Ghost, Dragon,Steel, Fairy]
# list_string = ['Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Steel', 'Fairy']



tabla = np.array([Normal, Fire, Water, Electric, Grass, Ice, Fighting, Poison, Ground, Flying, Psychic, Bug, Rock, Ghost, Dragon,Steel, Fairy])
print(tabla[0][0])

#CLANES ASOCIADOS A TIPOS

"""Clanes = {
    "Seavell": [Water, Ice],
    "Psycraft": [Psychic, Fairy],
    "Orebound": [Ground, Rock],
    "Volcanic": [Fire],
    "Malefic": [Poison, Ghost, Dark],
    "Wingeon": [Flying, Dragon],
    "Naturia": [Grass, Bug],
    "Gardestrike": [Normal, Fighting],
    "Ironhard": [Steel],
    "Raibolt": [Electric]
}"""

Clanes = {
    "Seavell": [2, 5],
    "Psycraft": [10, 17],
    "Orebound": [8, 12],
    "Volcanic": [1],
    "Malefic": [7, 13, 15],
    "Wingeon": [9, 14],
    "Naturia": [4,11],
    "Gardestrike": [0,6],
    "Ironhard": [16],
    "Raibolt": [3]
}

class Clan:
    #Constructor
    def __init__(self, nombre):
        self.name = nombre
        self.stats = {
            "effectiveness": 0,
            "weakness": 0,
            "inmune attack": 0,
            "inmune": 0,
            "resistences": 0,
            "no works well": 0
        }

    #Busca que clan perteneces y lo retorna
    def get_clan(self):
        for name in Clanes:
            if name.lower() == self.name.lower():
                return Clanes[name]

    #Calcula debilidades, fortalezas e inmunidades del clan
    def calc(self):
        clan = Clanes[self.name] #tupla con las pos

        j = i = 0
        for row in tabla:
            for nro in row:
                if len(clan) == 3:
                    if (clan[0] == j) ^ (clan[1] == j) ^ (clan[2] == j):
                        if nro == 2:
                            self.stats["effectiveness"] += 1
                        elif nro == 0.5:
                            self.stats["no works well"] += 1
                        elif nro == 0:
                            self.stats["inmune attack"] += 1
                elif len(clan) == 2:
                    if (clan[0] == j) ^ (clan[1] == j):
                        if nro == 2:
                            self.stats["effectiveness"] += 1
                        elif nro == 0.5:
                            self.stats["no works well"] += 1
                        elif nro == 0:
                            self.stats["inmune attack"] += 1
                elif len(clan) == 1:
                    if clan[0] == j:
                        if nro == 2:
                            self.stats["effectiveness"] += 1
                        elif nro == 0.5:
                            self.stats["no works well"] += 1
                        elif nro == 0:
                            self.stats["inmune attack"] += 1
            j += 1

        for col in np.transpose(tabla):
            for nro in col:
                if len(clan) == 3:
                    if (clan[0] == i) ^ (clan[1] == i) ^ (clan[2] == j):
                        if nro == 2:
                            self.stats["weakness"] += 1
                        elif nro == 0.5:
                            self.stats["resistences"] += 1
                        elif nro == 0:
                            self.stats["inmune"] += 1
                elif len(clan) == 2:
                    if (clan[0] == i) ^ (clan[1] == i):
                        if nro == 2:
                            self.stats["weakness"] += 1
                        elif nro == 0.5:
                            self.stats["resistences"] += 1
                        elif nro == 0:
                            self.stats["inmune"] += 1
                elif len(clan) == 1:
                    if clan[0] == i:
                        if nro == 2:
                            self.stats["weakness"] += 1
                        elif nro == 0.5:
                            self.stats["resistences"] += 1
                        elif nro == 0:
                            self.stats["inmune"] += 1
            i += 1

def main():
    aux = input("Input Clan: ")
    aux = aux.lower()
    aux = aux.capitalize()
    if aux in Clanes:
        clan_selected = Clan(aux)
    else:
        print("Ese nombre de clan no existe weiiii")
        sys.exit()
#clan_selected.search()
    clan_selected.calc() #NO HACE BIEN LA WEA PERO ESTA LA IDEA
    print(clan_selected.stats)
    #display las weas

    #print(clan_selected)

    #window = tk.Tk()
    #window.geometry("1000x800")
    #window.mainloop()


if __name__ == "__main__":
    main()