import GRUandVector
from GRUandVector import gru
from GRUandVector import vector
def simulate_battle():
    Gru=gru("GRU")
    vec=vector("Vector")
    round_num=1
    Gru.select_GRU_weapon()
    vec.display_vector_weapons()
    Gru.select_GRU_sheild()
    vec.display_vector_shields()
    while(Gru.is_alive() and vec.is_alive()):
        if(Gru.energy<20 and vec.energy<15):
            break
        print(f"\nRound {round_num}:")
        print(f"{Gru.name}: Health={Gru.health}, Energy={Gru.energy}")
        print(f"{vec.name}: Health={vec.health}, Energy={vec.energy}")
        Gru.use_weapon(vec)
        vec.use_weapon(Gru)
        round_num+=1
    
    if(Gru.is_alive() and vec.is_alive()==False):
        print("Gru wins the battle!")
    elif(Gru.is_alive==False and vec.is_alive):
        print("Vector wins the battle!")
    else:
        print("Draw")
def validate_input(lower_Bound,upper_bound):
    while(True):
        inp=int(input())
        if(inp>=lower_Bound and inp<=upper_bound):
            break
    return inp


print("Welcome to battle field game")
print("choose your mode")
choice=0

while(True):
    choice=int(input('Mode 1:2 players  Mode2:play with the computer\n'))
    if(choice==1 or choice==2):
        break
if(choice==1):
    simulate_battle()

    










    
