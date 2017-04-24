# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:17:00 2017

@author: Raphael
"""

import json
import random as rd
import time


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
            
    with open("Player.json", "w") as Arq:
        json.dump(Dic,Arq)
    with open("Adventure.json", "w") as Arq2:
        json.dump(Adv,Arq2)

        
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
    Growths = [80,30,40,35,50,25]
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
    return Boo

    


        

    
    
    