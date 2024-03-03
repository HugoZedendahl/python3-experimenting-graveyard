import random
import time

startTime = time.time()

room = 1
difficulty = 2
combatSkill = 1
health = 10
damage = 1
baseEnemyHealth = 2
enemyHealth = 2
#våra variables för spelsystem
def roll():
    return(random.randint(1,10))

#grunden för vårt "combat system"

def attack():
    heroRoll = roll()+combatSkill
    if (heroRoll)>=difficulty:
        print("you strike the monster!")
        return True
    else:
        print("you missed!")

#attack funktionen
def defend():
    monsterRoll = roll()+difficulty
    heroRoll = roll()+combatSkill
    if monsterRoll>heroRoll:
        print("the monster retaliates!")
        return True
    else:
        print("the monster misses!")
        return False
#monster attask system

print("welcome to the dungeon!! to get the treasure you need to clear 5 rooms with a guardian monster in each getting more difficult in each room! good luck adventurer as we enter the dungeon!!")
time.sleep(1)
print("you enter the room, the guardian monster in front of you, you ready yourself for combat")
time.sleep(1)
print("""you remember your training, write "1" to fight, write "2" to heal, write "3" to flee in shame""")
time.sleep(1)
#intro
while True:
    if room == 6:
        print("victory is yours!!! you struggled, triumphed and you found the treasure of your dreams!!")
        timePlayed = (time.time()-startTime)/60
        print(f"you delved into the dungeon for {timePlayed} minutes, enter anything to end. made by Hugo Zedendahl")
        input()
        quit()
    #check för att se ifall du har vunnit, samt avslutar spelet vid vinst
    
    print("the moster stands in front of you")
    time.sleep(1)
    print(f"you have {health} life left and you deal {damage} every hit.")
    time.sleep(1)
    print("what do you do?")
    tempInput = input()
    #start av spelarens tur
    try:
        tempInput = int(tempInput)
    except:
        print("""you remember your training, write "1" to fight, write "2" to heal, write "3" to flee in shame""")
        continue
    #ifall fel input har inmatas, påminner av vad du kan göra
    if tempInput==1:
        tempAttack = attack()
        if tempAttack == True:
            enemyHealth -= 1

        tempDefend = defend()
        if tempDefend == True:
            health -= 1

    elif tempInput==2:
        print("you call upon the light to heal you wounds!")
        health += 5
    elif tempInput==3:
        print("you flee in shame, never to return...")
        time.sleep(5)
        quit()
    #våra tre alternativ
    while enemyHealth==0:
        print("the monster falls under your blade, you feel power surge in you")
        time.sleep(1)
        print("choose your level up! type 1 to increase your combat skill, type 2 to increase your damage")
        tempInput = input()
        try:
            tempInput = int(tempInput)
            if tempInput == 1:
                combatSkill +=1
                difficulty +=1
                enemyHealth = baseEnemyHealth+difficulty
                room += 1
                print("you delve deeper")
                break
            elif tempInput == 2:
                damage +=1
                difficulty +=1
                enemyHealth = baseEnemyHealth+difficulty
                room += 1
                print("you delve deeper")
                break
        except:
            print("you reconcider")
    #när spelaren har vunnit et rum, återställer värden och ökar svårighetsgraden, samt gör spelaren lite starkare
    if tempInput == 4231:
        room = 6
    #fuskkod för test