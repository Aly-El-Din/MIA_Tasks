from Weapons import Weapons
def validate_input(lower_Bound,upper_bound):
        while(True):
            inp=int(input())
            if(inp>=lower_Bound and inp<=upper_bound):
                break
        return inp
class Villain:
    def __init__(self,name,Sheild,Health=100,Energy=500):
        self.name=name
        self.health=Health
        self.energy=Energy
        self.sheild=Sheild
   
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        actual_damage = damage - (damage * self.shield) // 100
        self.health -= actual_damage
    def use_shield(self):
        pass
    def use_weapon(self, opponent):
        pass
    def __str__(self):
        return self.name
