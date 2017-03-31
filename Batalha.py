# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:13:05 2017

@author: marco
"""

def attack(A,B):
    print("{} attacks!".format(A["nome"]))
    NHP = B["HP"]
    WeaponA = A["Weapon"]
    attackA = A["atk"]+WeaponA["mgt"]-B["def"]
    hitA = A["skl"]*2 + A["lck"]/2 +WeaponA["acc"]- B["spd"]*2 + B["lck"]
    if hitA > 100:
        hitA = 100
    critA = WeaponA["crit"]+A["skl"]/2- B["lck"]
    print("Hit={0} Dmg={1} Crit={2}".format(hitA,attackA,critA))
    import random
    truehit = (random.randint(1,100) + random.randint(1,100))/2
    if truehit <= hitA:
        print("The attack hit! ",end="")
        if random.randint(1,100)<= critA:
            print("A critical hit! {} damage!".format(attackA*3))
            NHP = B["HP"] - attackA*3
        else:
            print("{} damage!".format(attackA))
            NHP = B["HP"] - attackA
        if NHP > 0:
            print("{0} has {1} hp left!".format(B["nome"],NHP))
        else:
            print("{0} died!".format(B["nome"]))
    else:
        print("The attack missed!")
    return NHP

#Broadsword = [11,65,10,5]
#Poleaxe = [12,65,11,0]
#
#Agnes=[0]*9
#Borin=[0]*9
#statnames=["Hp","Atk","Skl","Spd","Lck","Def","Res"]
##Agnes[7] =input("What is the attacker's name? ")
##for i in range (len(statnames)):
##    Agnes[i] = int(input("What is {0}'s {1}? ".format(Agnes[7],statnames[i])))
##Borin[7] =input("What is the defender's name? ")
##for i in range (len(statnames)):
##    Borin[i] = int(input("What is {0}'s {1}? ".format(Borin[7],statnames[i])))
#Borin[8] = Poleaxe
#Agnes[8] = Broadsword
#Agnes = [30,22,83,14,20,17,15,"Agnes",Broadsword]
#Borin = [50,18,10,11,8,13,10,"Borin",Poleaxe]

def Turno(Agnes,Borin):
    import time
    while True:
        Borin["HP"] = attack(Agnes,Borin)
        if Borin["HP"] <= 0:
            break
        time.sleep(2) # delays for 2 seconds
        Agnes["HP"] = attack(Borin,Agnes)
        if Agnes["HP"] <= 0:
            break
        time.sleep(2) # delays for 2 seconds
        if Agnes["spd"]-Agnes["Weapon"]["wgt"] -(Borin["spd"] - Borin["Weapon"]["wgt"]) >= 3:
            Borin["HP"] = attack(Agnes,Borin)
        elif Borin["spd"]-Borin["Weapon"]["wgt"] - (Agnes["spd"] - Agnes["Weapon"]["wgt"]) >= 3:
            Agnes["HP"] = attack(Borin,Agnes)    
        break
    return Agnes["HP"],Borin["HP"]

#Turno(Agnes,Borin)