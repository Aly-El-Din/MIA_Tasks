class Weapons:
    #constructor
    def __init__(self,name,Energy,Damage,Resources,Describtion):
        #protected attributes as we will inherit from this class
        self._name=name
        self._energy=Energy
        self._damage=Damage
        self._resources=Resources
        self._describtion=Describtion
    def get_name(self):
        return self._name 
    def validate_weapon(self,energy):
        if(self._resources==0):
            print("Resources for this weapon are empty, choose another weapon\n")
            return False
        elif (energy<self._energy and energy>50):
            print("Energy is not sufficient to use this weapon, choose another one\n")
            return False
        elif (energy<50):
            print("Energy is not sufficient to use any weapon\n")
        return True
    def describeWeapon(self):
        return f"Name: {self._name}\nEnergy: {self._energy}\nDamage: {self._damage}\nNumber of weapons {self._resources}\nDescribtion: {self._describtion}"
    