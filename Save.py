# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:17:00 2017

@author: Raphael
"""

import json
import random as rd
import time

def Heal(jog):
    jog["HP"] += 20
    print("Você curou 20 de vida!")
    time.sleep(1.5)
    return jog

def Inventario():
    with open("Inventario.json","r") as inv:
        Inv = json.load(inv)
    if Inv["Potion"]["quant"] != 0:
        print("-Potion x{}".format(Inv["Potion"]["quant"]))
        time.sleep(1.5)
        return True
    else:
        print("You have an empty inventory...")
        time.sleep(1.5)
        return False
    
    

def SaveGameP(PD):
    PlayerData = PD
    with open("Player.json", "w") as Arq:
        json.dump(PlayerData,Arq)
def SaveGameB(BD):
    BeastData = BD
    with open("Beast.json", "w") as Arq:
        json.dump(BeastData,Arq)
def SaveGameI(ID):
    InvData = ID
    with open("Inventory.json", "w") as Arq:
        json.dump(InvData,Arq)
def SaveGameA(AD):
    AdventureData = AD
    with open("Adventure.json", "w") as Arq:
        json.dump(AdventureData,Arq)
        
def StartOver():
    Dic = {
    "Start": 0
    }
    Adv = {"loc" : "Apple Woods", "step" : 0}
    Best = {}
    Inv = {"Potion": {"quant" : 5}}
    with open("Player.json", "w") as Arq:
        json.dump(Dic,Arq)
    with open("Adventure.json", "w") as Arq2:
        json.dump(Adv,Arq2)
    with open("Beast.json", "w") as Arq3:
        json.dump(Best,Arq3)
    with open("Inventario.json", "w") as Arq4:
        json.dump(Inv,Arq4)

        
def SaveAll(PD,BD,ID,AD):
    SaveGameP(PD)
    SaveGameB(BD)
    SaveGameI(ID)
    SaveGameA(AD)

def XpCount(P,E):
    EXPgain = E["lvl"]/P["lvl"] * 100
    print("You got {0} XP!".format(EXPgain))
    time.sleep(2.5)
    P["xp"] += EXPgain
    if P["xp"] >= 100:
        print("You leveled up!!!")
        time.sleep(2.5)
        P = LvlUp(P)
    return P

def LvlUp(P):
    P["xp"] = 0
    P["lvl"] += 1
    Stats = ["MHP","atk","skl","spd","lck","def"]
    Growths = [80,40,45,40,55,35]
    for a in range(len(Stats)):
        count = rd.randint(0, 100)
        if count <= Growths[a]:
            P[Stats[a]] += 1
            time.sleep(1)
            print("{0} went up by 1!".format((Stats[a])))
    time.sleep(1)
    return P

def Escape(P):
    a = rd.randint(0, 20)
    print("You try to escape!")
    if a<P["spd"]:
        Boo = True
    else:
        Boo = False
    return Boo

def Promote():
    Classes = ["Mage","Knight","Thief","Swordsman","Ruffian","Archer"]
    with open("Player.json", "r") as plr:
        Plr = json.load(plr)
    if Plr["class"] in Classes:
        if Plr["lvl"] >= 10:
            t = input("Do you wish to promote to a new class?(Y or N) ")
            if t.upper() == "Y":
                Plr["class"] = Plr["promo"][0]
                print("You became a {0}!!!".format(Plr["promo"][0]))
                time.sleep(2)
                Stats = ["MHP","atk","skl","spd","lck","def"]
                b = 0
                for a in Stats:
                    gain = Plr["bonus"][b]
                    Plr[a] += gain
                    #print("{0} went up by {1}!".format((a,gain)))
                    b +=1
                    if b == 6:
                        break
                print("All your stats went up substantially!!")
                time.sleep(1.5)
                print("You learned {}!!!".format(Plr["promo"][1]))
                Plr["Techs"].append(Plr["promo"][1])
                time.sleep(1.5)
                SaveGameP(Plr)
        else:
            print("Your level is not high enough...")
            print("You must level up {} more times.".format(10-Plr["lvl"]))
    else:
        print("You are already promoted")

