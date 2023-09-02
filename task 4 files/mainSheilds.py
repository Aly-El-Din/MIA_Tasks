class Sheilds:
    def __init__(self,name,Energy,Save,Resources,Description):
        self._name=name
        self._energy=Energy
        self._save=Save 
        self._resources=Resources
        self._describtion=Description
    def validate_sheild(self,energy):
        if(energy<self._energy):
            print("Your energy is not sufficient to use this shield, chooser another")
            return False
        return True

    def describeShield(self):
        return f"Name: {self._name}\nEnergy: {self._energy}\nSave: {self._save}\nNumber of shields {self._resources}\nDescribtion: {self._describtion}" 