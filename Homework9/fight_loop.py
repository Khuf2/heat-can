# Homework 9 - 7/1/20
# Lists, String Building, String Slicing, For Loop Review

'''
# fight(): 
# e1, e2 = enemy1, enemy2
# 
'''
def fight(e1, e2):
    # Your code starts here. 
    winner = None
    while(e1["HP"] > 0 and e2["HP"] > 0):
        if(e1["spd"] > e2["spd"]):
            # e1 goes first

            if((e1["cd"]) == 0):
                # use special, then reset my cd back to max
                e1["skill"](e1, e2)
                # enemy1 max CD is 3
                e1["cd"] = 3
                print ("e1 uses skill")
            else:
                # I attack
                calcDmg(e2, e1["att"])
                e1["cd"] -= 1
                print ("e1 attacks")
            
            dead = e2["HP"] <= 0
            if (not dead):
                if((e2["cd"]) == 0):
                    # use special, then reset my cd back to max
                    e2["skill"](e1, e2)
                    # enemy2 max CD is 2
                    e2["cd"] = 2
                    print ("e2 uses skill")
                else:
                    # I attack
                    calcDmg(e1, e2["att"])
                    e2["cd"] -= 1
                    print ("e2 attacks")

        else:
            # e2 goes first

            if((e2["cd"]) == 0):
                # use special, then reset my cd back to max
                e2["skill"](e1, e2)
                # enemy2 max CD is 3
                e2["cd"] = 2
                print ("e2 uses skill")
            else:
                # I attack
                calcDmg(e1, e2["att"])
                e2["cd"] -= 1
                print ("e2 attacks")

            dead = e1["HP"] <= 0
            if (not dead):
                if((e1["cd"]) == 0):
                    # use special, then reset my cd back to max
                    e1["skill"](e1, e2)
                    # enemy1 max CD is 3
                    e1["cd"] = 3
                    print ("e1 uses skill")
                else:
                    # I attack
                    calcDmg(e2, e1["att"])
                    e1["cd"] -= 1
                    print ("e1 attacks")
            
        # HP/CD Update
        print("\nEnemy1: " + str(e1["HP"]) + "   CD: " + str(e1["cd"]))
        print("Enemy2: " + str(e2["HP"]) + "   CD: " + str(e2["cd"]) + "\n")
            
    if(e1["HP"] == 0):
        winner = e2
    elif(e2["HP"] == 0):
        winner = e1

    return winner

def oneSpecial(e1, e2):
    # if enemy special is ready, do 3x dmg
    # otherwise, do 2x dmg
    if(e2["cd"] == 0):
        calcDmg(e2, (4*(e1["att"])) )
    else:
        calcDmg(e2, (2*(e1["att"])) )
    e1["att"] += 1

def twoSpecial(e1, e2):
    # if below half, heal
    # if above half, fireball
    # if can kill e2, use fireball
    fireballDmg = 3*(e2["ap"])
    healAmt = 2*(e2["ap"])
    if(e1["HP"] <= fireballDmg or e2["HP"] > 50):
        # use fireball if they are in kill range
        calcDmg(e1, fireballDmg )
        print ("fireball")
    else:
        e2["HP"] += healAmt
        print("heal")

def calcDmg(e, dmg):
    if((e["HP"] - dmg) < 0):
        e["HP"] = 0
    else:
        e["HP"] -= dmg

# switching enemy1 "att" between 3 and 4 will toggle victor

enemy1 = { "HP": 80, "att": 4, "ap": 3, "spd": 3, "cd": 4, "skill": oneSpecial }
enemy2 = { "HP": 100, "att": 3, "ap": 5, "spd": 2, "cd": 3, "skill": twoSpecial }

print( fight(enemy1, enemy2) )