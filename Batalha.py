# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:13:05 2017

@author: marco
"""
import random
import os
import json
import Save as sav
import Misc as misc

with open ("Weapons.json") as wpns:
    Wpn = json.load(wpns)
    
with open ("Techs.json") as tec:
    Tech = json.load(tec)

def poison(A,B):
    if A["status"] == "poison":
        time.sleep(1)
        dmg = int(A["HP"]/10)
        print("{0} is hurt by poison! {1} damage!".format(A["nome"],dmg))
        A["HP"] -= dmg
    if B["status"] == "poison":
        dmg = int(B["HP"]/10)
        time.sleep(1)
        print("{0} is hurt by poison! {1} damage!".format(B["nome"],dmg))
        B["HP"] -= dmg
    return (A,B)
    
    
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
    eff = 'none'
    if truehit <= hitA:
        print("The attack hit! ",end="")
        if random.randint(1,100)<= critA:
            print("A critical hit! {} damage!".format(attackA*3))
            NHP = B["HP"] - attackA*3
        else:
            print("{} damage!".format(attackA))
            NHP = B["HP"] - attackA
        if WeaponA["effect"] == "poison":
            print("{0} was poisoned!".format(B["nome"]))
            eff = 'poison'
        if NHP > 0:
            print("{0} has {1} hp left!".format(B["nome"],NHP))
        else:
            print("{0} died!".format(B["nome"]))
    else:
        print("The attack missed!")
    return NHP,eff

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
        Borin["HP"],eff= attack(Agnes,Borin)
        if Borin["HP"] <= 0:
            break
        if eff == "poison":
            Borin["status"]="poison"
        time.sleep(2) # delays for 2 seconds
        Agnes["HP"],eff = attack(Borin,Agnes)
        if Agnes["HP"] <= 0:
            break
        if eff == "poison":
            Agnes["status"]="poison"
        time.sleep(2) # delays for 2 seconds
        if Agnes["spd"]-Agnes["Wpn"]["wgt"] -(Borin["spd"] - Borin["Wpn"]["wgt"]) >= 3:
            Borin["HP"],eff = attack(Agnes,Borin)
            if eff == "poison":
                Borin["status"]="poison"
        elif Borin["spd"]-Borin["Wpn"]["wgt"] - (Agnes["spd"] - Agnes["Wpn"]["wgt"]) >= 3:
            Agnes["HP"],eff = attack(Borin,Agnes) 
            if eff == "poison":
                Agnes["status"]="poison"
        time.sleep(2) # delays for 2 seconds
        break
    return Agnes["HP"],Borin["HP"],Agnes["status"],Borin["status"]

def Fight(Agnes,Borin):
    #enemy attack
    alatk=len(Borin["Techs"]) 
    clac= random.randint(0,alatk)
    if clac == 0:
        Borin["Attack"] = Borin["Wpn"]
    else:
        Borin["Attack"] = Tech[Borin["Techs"][clac-1]]
    #who goes first
    tot = Agnes["lck"]+Borin["lck"]
    calc = (random.randint(1,tot) + random.randint(1,tot))/2 
    if Agnes["lck"]>=calc:
        Turno(Agnes,Borin)
    else:
        Turno(Borin,Agnes)
    return Agnes,Borin
    

#Turno(Agnes,Borin)
import time

def Comando(Agnes,Borin):
    Agnes["Wpn"] = Wpn[Agnes["Weapon"]]
    Borin["Wpn"] = Wpn[Borin["Weapon"]]
    Agnes["status"] = "none"
    Borin["status"] = "none"
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
                print("-Attack (Mgt={0} Acc={1} Wgt={2} Crit={3} Effect={4})".format(Agnes["Wpn"]["mgt"],Agnes["Wpn"]["acc"],Agnes["Wpn"]["wgt"],Agnes["Wpn"]["crit"],Agnes["Wpn"]["effect"]))
                for a in range(0,len(Agnes["Techs"])):
                    time.sleep(0.5)
                    print("-{0} (Mgt={1} Acc={2} Wgt={3} Crit={4} Effect={5})".format(Tech[Agnes["Techs"][a]]["nome"],Tech[Agnes["Techs"][a]]["mgt"],Tech[Agnes["Techs"][a]]["acc"],Tech[Agnes["Techs"][a]]["wgt"],Tech[Agnes["Techs"][a]]["crit"],Tech[Agnes["Techs"][a]]["effect"]))
                print("-Cancel")
                move = input("")
            if move == "Cancel":
                continue
            elif move == "Attack":
                Agnes["Attack"] = Agnes["Wpn"]
            else:
                Agnes["Attack"] = Tech[move]
            #calculo quem vai antes
            Agnes,Borin = poison(Agnes,Borin)
            Agnes,Borin = Fight(Agnes,Borin)
        if command == 2:
            #inventorio
            pass
        if command == 3:
            #fugir
            escape = sav.Escape(Agnes)
            if escape == True:
                print("You escaped safely")
                time.sleep(1)
                return Agnes,True
            else:
                print("You failed to escape")
                time.sleep(1)
                attack(Borin,Agnes)
            pass
    return Agnes,False
        
    
def Begin(Agnes,Borin):
    with open ("Beast.json") as bst:
        Bst = json.load(bst)
    if Borin["nome"] not in Bst:
        Bst[Borin["nome"]] = Borin
        sav.SaveGameB(Bst)
    print("Suddenly, {} attacks you!".format(Borin["nome"]))
    time.sleep(2)
    Agnes["HP"] =Agnes["MHP"]
    Agnes,escape = Comando(Agnes,Borin)
    if escape == True:
        return Agnes
    if Agnes["HP"]>0:
        Agnes = sav.XpCount(Agnes,Borin)
        Agnes = misc.WeaponDrop(Agnes,Borin)
        sav.SaveGameP(Agnes)
    else:
        print("YOU LOSE")
        time.sleep(0.5)
        os._exit(0)