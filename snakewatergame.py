import random
def water():
    man = ["snake","water","gun"]
    chances = 0
    max_chances = 5
    wins = []
    
    while chances < max_chances:
        computer = random.choice(man)
        print("welcome to the (snake,water,gun) game")
        human = input("enter your choice" + " ").lower()
       
        if computer == human:
            print("Draw")
            wins.append("draw")
        elif computer == "snake" and  human == "gun":
            print("congrulations ! you win")
            wins.append("win")
        elif computer == "water"  and  human == "snake": 
            print("congrulations ! you win")
            wins.append("win")
        elif computer == "gun" and human == "water":
            print("congrulations ! you win")
            wins.append("win")
         
        else:
            print("you loose")
        
            wins.append("loose")
        chances +=1

    return wins

   
anme = water()
result = water()




print("Results of each round:", anme)







