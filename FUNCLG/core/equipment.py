#####################################################################################   
#   Programmer: Jevin Evans                                                         #
#	Date: 7/13/2021                                                                 #
#	Program: Equipment Class                                                        #
#   Description: The Equipment class allows for creation of objects in the game     # 
#       to be used by characters and placed inside of the armor or in other         # 
#       holders/storage containers inside of the game.                              #      
#####################################################################################

import json

try:
    from utils.types import getItemDescription, getItemType
except:
    from FUNCLG.utils.types import getItemDescription, getItemType

class Equipment():

    def __init__(self, name='', description='', armorType=None, itemType=None, weaponType=None, itemLevel=0, abilityPoints=0):        
        """
            Creates an equipment item
        """
        
        self.name = name
        self.description = description
        self.armorType = armorType
        self.itemType = itemType
        self.weaponType = weaponType
        self.itemLevel = itemLevel
        self.abilityPoints = abilityPoints
    
    def __str__(self):
        return f"{self.name} ({self.itemLevel})"

    def details(self):
        titleLen = 2 + len(self.name)
        desc =  f"\n {self.name} \n{''.join(['-' for x in range(titleLen)])}"
        desc += f"\nLevel:{self.itemLevel:3d} | Ability Pts: {self.abilityPoints} "
        desc += "ATK" if getItemType(self.itemType) == "Weapon" else "DEF"
        desc += f"\nType: {getItemDescription(self.itemType, self.armorType, self.weaponType)}"
        desc += f"\nDescription: {self.description}"
        return desc

    def printToFile(self):
        with open(self.name+".json", "w") as oFile:
            json.dump(self.__dict__, oFile)
    
    def export(self):
        return json.dumps(self.__dict__)

    # def getStats(self):

# def main():
#     tempE = Equipment("excelsior", "This is a temp example is used to describe a simple sword.", itemType=4, weaponType=0, itemLevel=52, abilityPoints=500)
#     print(tempE)

#     print(tempE.__dict__)
#     print()
#     print(tempE.export())
