# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:13:05 2017

@author: marco
"""
import random
import os
import json
import pygame

with open ("Weapons.json") as wpns:
    Wpn = json.load(wpns)
    
with open ("Techs.json") as tec:
    Tech = json.load(tec)

def attack(A,B):
    print("{0} attacks with {1}!".format(A["nome"],A["Attack"]["nome"]))
    NHP = B["HP"]
    WeaponA = A["Attack"]
    attackA = A["atk"]+WeaponA["mgt"]-B["def"]
    hitA = A["skl"]*2 + A["lck"]/2 +WeaponA["acc"]- B["spd"]*2 + B["lck"]
    if hitA > 100:
        hitA = 100
    if attackA < 0:
        attackA = 0
    critA = WeaponA["crit"]+A["skl"]/2- B["lck"]
    print("Hit={0} Dmg={1} Crit={2}".format(hitA,attackA,critA))
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
        time.sleep(2) # delays for 2 seconds
        break
    return Agnes["HP"],Borin["HP"]

def Fight(Agnes,Borin):
    #enemy attack
    alatk=len(Borin["Techs"]) 
    clac= random.randint(0,alatk)
    if clac == 0:
        Borin["Attack"] = Borin["Weapon"]
    else:
        Borin["Attack"] = Tech[Borin["Techs"][clac-1]]
    #who goes first
    tot = Agnes["lck"]+Borin["lck"]
    calc = (random.randint(1,tot) + random.randint(1,tot))/2 
    if Agnes["lck"]>=calc:
        Turno(Agnes,Borin)
    else:
        Turno(Borin,Agnes)
           
    

#Turno(Agnes,Borin)
import time

def Comando(Agnes,Borin):
    Agnes["Weapon"] = Wpn[Agnes["Weapon"]]
    Borin["Weapon"] = Wpn[Borin["Weapon"]]
    while Agnes["HP"] > 0 and Borin["HP"] > 0:
        os.system("cls")#ClearScreen
        print("{0} has {1} HP.".format(Agnes["nome"],Agnes["HP"]))
        print("{0} has {1} HP.".format(Borin["nome"],Borin["HP"]))
        options = ["1)Fight","2)Item","3)Run"]
        command="aaaa"
        while command not in range(1,4):
            print("What will you do?")
            for n in options:
                time.sleep(0.5)
                print(n)
            command = int(input(""))
        if command == 1:
            move = "lafgaag"
            attack = ["Attack"]
            for b in Agnes["Techs"]:
                attack.append(b)
            while move not in attack:
                os.system("cls")#ClearScreen
                print("What attack will you use?")
                time.sleep(0.5)
                print("-Attack (Mgt={0} Acc={1} Wgt={2} Crit={3} Effect={4})".format(Agnes["Weapon"]["mgt"],Agnes["Weapon"]["acc"],Agnes["Weapon"]["wgt"],Agnes["Weapon"]["crit"],Agnes["Weapon"]["effect"]))
                for a in Agnes["Techs"]:
                    time.sleep(0.5)
                    print("-{0} (Mgt={1} Acc={2} Wgt={3} Crit={4})".format(Agnes["Techs"][a]["name"],Agnes["Techs"][a]["mgt"],Agnes["Techs"][a]["acc"],Agnes["Techs"][a]["wgt"],Agnes["Techs"][a]["crit"],Agnes["Techs"][a]["effect"]))
                print("-Cancel")
                move = input("")
            if move == "Cancel":
                continue
            elif move == "Attack":
                Agnes["Attack"] = Agnes["Weapon"]
            else:
                Agnes["Attack"] = Tech[Agnes["Techs"][move]]
            #calculo quem vai antes
            Fight(Agnes,Borin)
        if command == 2:
            #inventorio
            pass
        if command == 3:
            #fugir
            pass
        
    
def Begin(Agnes,Borin): 
    print("Suddenly, {} attacks you!".format(Borin["nome"]))
    Agnes["HP"]=Agnes["MHP"]
    Agnes = Comando(Agnes,Borin)
    