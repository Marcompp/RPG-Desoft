# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:13:05 2017

@author: marco
"""

def attack(A,B):
    print("{} attacks!".format(A[7]))
    NHP = B[0]
    WeaponA = A[8]
    attackA = A[1]+WeaponA[0]-B[5]
    hitA = A[2]*2 + A[4]/2 +WeaponA[1]- B[3]*2 + B[4]
    critA = WeaponA[3]+A[2]/2- B[4]
    print("Hit={0} Dmg={1} Crit={2}".format(hitA,attackA,critA))
    import random
    truehit = (random.randint(1,100) + random.randint(1,100))/2
    if truehit <= hitA:
        print("The attack hit! ",end="")
        if random.randint(1,100)<= critA:
            print("A critical hit! {} damage!".format(attackA*3))
            NHP = B[0] - attackA*3
        else:
            print("{} damage!".format(attackA))
            NHP = B[0] - attackA
        if NHP > 0:
            print("{0} has {1} hp left!".format(B[7],NHP))
        else:
            print("{0} died!".format(B[7]))
    else:
        print("The attack missed!")
    return NHP

Broadsword = [11,65,10,5]
Poleaxe = [12,65,11,0]

Agnes=[0]*9
Borin=[0]*9
statnames=["Hp","Atk","Skl","Spd","Lck","Def","Res"]
#Agnes[7] =input("What is the attacker's name? ")
#for i in range (len(statnames)):
#    Agnes[i] = int(input("What is {0}'s {1}? ".format(Agnes[7],statnames[i])))
#Borin[7] =input("What is the defender's name? ")
#for i in range (len(statnames)):
#    Borin[i] = int(input("What is {0}'s {1}? ".format(Borin[7],statnames[i])))
Borin[8] = Poleaxe
Agnes[8] = Broadsword
Agnes = [30,22,83,14,20,17,15,"Agnes",Broadsword]
Borin = [50,18,10,11,8,13,10,"Borin",Poleaxe]

def Turno(Agnes,Borin):
    import time
    while True:
        Borin[0] = attack(Agnes,Borin)
        if Borin[0] <= 0:
            break
        time.sleep(2) # delays for 2 seconds
        Agnes[0] = attack(Borin,Agnes)
        if Agnes[0] <= 0:
            break
        time.sleep(2) # delays for 2 seconds
        if Agnes[3]-Agnes[8][2] -(Borin[3] - Borin[8][2]) >= 3:
            Borin[0] = attack(Agnes,Borin)
        elif Borin[3]-Borin[8][2] - (Agnes[3] - Agnes[8][2]) >= 3:
            Agnes[0] = attack(Borin,Agnes)    
        break
    return Agnes[0],Borin[0]

Turno(Agnes,Borin)