from Weapons import Weapons
from mainSheilds import Sheilds
from villain import Villain
#Gru's available weapons
freeze_Gun= Weapons("Freeze Gun",50,11,float('inf'),"Minions occasionally wield freeze ray guns that shoot a freezing beam to immobilize opponents temporarily")
electricPod=Weapons("Electric Prod",88,18,5,"Minions might use electric prods to deliver mild shocks to enemies, stunning them momentarily.")
megaMagnet=Weapons("Mega Magnet",92,10,3,"Minions utilize a mega magnet to attract or repel metal objects, potentially disrupting enemy vehicles or equipment..")
KalmanMissile=Weapons("Kalman Missile",120,20,1,"This unavoidable Missile created for enourmous distraction.")
#list of weapons for gru to select from 
gru_weapons=[freeze_Gun,electricPod,megaMagnet,KalmanMissile]

#GRU's available sheilds
EnergyProjectedBarrierGun=Sheilds ("Energy-Projected BarrierGun",20,40,float('inf'),"The spaceship's shields create aninvisible, energy-projected barrieraround the vehicle. This barrierabsorbs and dissipates energy-based attacks such as lasers,beams, and plasma shots.")
SelectivePermeability=Sheilds("Selective Permeability",50,90,2,"The shields can be programmed toallow certain objects, signals, or energies to pass through while blocking others. This can be useful for communication or specific tactical maneuvers.")
GRUSheild=Sheilds("GRU sheild",0,0,0," ")
#list of sheilds for gru to select from
gru_sheilds=[EnergyProjectedBarrierGun,SelectivePermeability]

#available weapons for vector
laser_blasters= Weapons("Laser Blasters",40,8,float('inf'),"Vector's primary weapon would be powerful laser blasters attached to his flying pod. These blasters emit focused energy beams that can slice through obstacles and damage enemy vehicles.")
plasma_grenades=Weapons("Plasma Grenades",56,13,8,"Vector could use plasma grenades that explode on impact, releasing fiery energy bursts that deal significant damage to enemy vehicles caught in the blast radius.")
sonic_resonance_canon=Weapons("Sonic Resonance Cannon",100,22,3,"Fires powerful sonic waves that can shatter enemy shields and disrupt their systems, temporarily incapacitating them.")
vectorWeapon=Weapons("vector weapon",0,0,0,' ')#initializing a weapon
#List of weapons for vector to select from 
vector_weapons=[laser_blasters,plasma_grenades,sonic_resonance_canon]

#available sheilds for vector
energyNetTrap=Sheilds ("Energy Net Trap",15,32,float('inf'),"Vector's pod might have the ability to deploy an energy net that ensnares enemy vehicles, temporarily immobilizing them and leaving them vulnerable to Vector's other attacks.")
QuantumDeflector=Sheilds("Quantum Deflector",40,80,3,"Manipulates quantum states to create a deflection field, causing enemy projectiles to miss the spaceship by a slight margin in the quantum realm.")
vectorSheild=Sheilds("vector sheild",0,0,0," ")
#list of sheilds for vector to select from
vector_sheilds=[energyNetTrap,QuantumDeflector]

def validate_input(lower_Bound,upper_bound):
    while(True):
        inp=int(input())
        if(inp>=lower_Bound and inp<=upper_bound):
            break
    return inp

class gru(Villain):
    GRUWeapon=Weapons("GRU weapon",0,0,0,' ')#initializing a weapon

    def __init__(self,name, Health=500, Energy=100):
        super().__init__(name, Health, Energy)
  
    #function to display weapons for gru to select the suitable weapon   
    def select_GRU_weapon(self):
        print("Choose GRU's weapon from the following weapons:\n")
        weapon_counter=1    
        for gru_weapon in gru_weapons:
            print(f"{weapon_counter}\n")
            weapon_counter+=1
            print(gru_weapon.describeWeapon())
    def use_weapon(self,opponent):
        if(isinstance(opponent,vector)):
            flag=False
            print("Gru, it's your turn, choose a weapon to hit the opponent")
            while(self.energy>=50):
                chooseGruWeapon=validate_input(1,4)
                self.GRUWeapon=gru_weapons[chooseGruWeapon-1]
                if(self.GRUWeapon.validate_weapon(self.energy)):
                    flag=True
                    self.GRUWeapon._resources-=1
                    self.energy-=self.GRUWeapon._energy
                    opponent.use_shield()
                    opponent.take_damage(self.GRUWeapon)                    
                    break
            if(flag==False):
                opponent.use_shield()
    def use_shield(self):
        print("Gru,choose your shield to defend yourself")
        flag=False
        while(self.energy>=20):
            chooseVectorShield=validate_input(1,2)
            GRUSheild=gru_sheilds[chooseVectorShield-1]
            if(GRUSheild.validate_sheild(self.energy)):
                self.energy-=GRUSheild._energy
                self.sheild=GRUSheild
                flag=True
                break
        if(flag==False):
            self.sheild._save=0

    def take_damage(self,opponent_weapon):
        actual_damage=0
        if(isinstance(opponent_weapon,Weapons)):
            actual_damage=opponent_weapon._damage-(opponent_weapon._damage*self.sheild._save)/100.0
        if(self.GRUWeapon.get_name()=="Mega Magnet"):
            actual_damage-=opponent_weapon._damage*20/100.0
            if(actual_damage<0):
                actual_damage=0
        self.health-=actual_damage
    #function to display sheilds for gru to select the suitable one for him
    def select_GRU_sheild(self):
        sheild_counter=1
        for gru_sheild in gru_sheilds:
            print(f"{sheild_counter}\n")
            sheild_counter+=1
            print(gru_sheild.describeShield())




class vector(Villain):
    def __init__(self,name, Health=500, Energy=100):
        super().__init__(name, Health, Energy)    
    def display_vector_weapons(self):
        print("Choose vector's weapon from the following weapons:\n")
        weapon_counter=1
        #diplaying weapons
        for vector_weapon in vector_weapons:
            print(f"{weapon_counter}\n")
            weapon_counter+=1
            print(vector_weapon.describeWeapon())
    def display_vector_shields(self):
        print("Choose Vector's sheild from the following sheilds:\n")
        sheild_counter=1
        #displaying shields
        for vector_sheild in vector_sheilds:
            print(f"{sheild_counter}\n")
            sheild_counter+=1
            print(vector_sheild.describeShield())
    def use_weapon(self,opponent):
        flag=False
        if(isinstance(opponent,gru)):
            print("Vector, It's turn, choose a weapon from you available weapons")
            while(self.energy>=40):
                chooseVectorWeapon=validate_input(1,4)
                vectorWeapon=vector_weapons[chooseVectorWeapon-1]
                if(vectorWeapon.validate_weapon(self.energy)):
                    vectorWeapon._resources-=1
                    self.energy-=vectorWeapon._energy
                    flag=True
                    opponent.use_shield()
                    opponent.take_damage(vectorWeapon)
                    break
            if(flag==False):
                opponent.use_shield()
    def use_shield(self):
        print("Vector, choose your shield to defend yourself")
        flag=False
        while(self.energy>=15):
            chooseVectorShield=validate_input(1,2)
            vectorSheild=vector_sheilds[chooseVectorShield-1]
            if(vectorSheild.validate_sheild(self.energy)):
                self.energy-=vectorSheild._energy
                self.sheild=vectorSheild
                flag=True
                break
        if(flag==False):
            self.sheild._save=0
    def take_damage(self,opponent_weapon):
        if(isinstance(opponent_weapon,Weapons)):
            actual_damage=opponent_weapon._damage-(opponent_weapon._damage*self.sheild._save)/100.0
            if (opponent_weapon.get_name()=="Kalman Missile"):
                actual_damage=opponent_weapon._damage
        self.health-=actual_damage




















