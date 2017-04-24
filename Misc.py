# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 14:01:58 2017

@author: marco
"""

import json
import os
import time
import random

with open ("Weapons.json") as wpns:
    Wpn = json.load(wpns)
    
with open ("Chars.json") as char:
    Char = json.load(char)
    
def Equip(jog,weapon):
    print("You've found a {5}! (Mgt={0} Acc={1} Wgt={2} Crit={3} Effect={4})".format(weapon["mgt"],weapon["acc"],weapon["wgt"],weapon["crit"],weapon["effect"],weapon["name"]))
    if weapon["name"] == Wpn[jog["Weapon"]]["name"]:
        print("But you're already equiped with one...")
        return jog["Weapon"]
    else:
        print("Do you wish to drop your current weapon? (Mgt={0} Acc={1} Wgt={2} Crit={3} Effect={4})".format(jog["Weapon"]["mgt"],jog["Weapon"]["acc"],jog["Weapon"]["wgt"],jog["Weapon"]["crit"],jog["Weapon"]["effect"]))
        asw = input("(S or N)")
        if asw.upper() == "S":
            print("You've dropped your current weapon and equiped the {}".format(weapon["name"]))
            return weapon["name"]
        else:
            print("You kept your current weapon...")
            return jog["Weapon"]

def WeaponDrop(A,B):
    rad = random.randint(0,10)
    if rad <= 2:
        A["Weapon"] = Equip(A,Wpn[B["Weapon"]])
    return A

def NewGame():
    print("Welcome, adventurer, a great quest lies before you!")
    time.sleep(1)
    nom=input("But first... Please register your name: ")
    print("{} is it? A fine name!".format(nom))
    time.sleep(1)
    print("Now...")
    time.sleep(1)
    print("What class do you wish to be?")
    start = ["Mage","Knight","Swordsman","Ruffian","Archer","Thief"]
    sel = "a"
    while sel not in range(1,len(start)+1):
        for i in range(len(start)):
            time.sleep(1)
            print("{0}) {1}".format(i+1,start[i]))
        sel = int(input(""))
    player = Char[start[sel-1]]
    player["nome"] = nom
    print("A {}? Fine!".format(player["class"]))
    time.sleep(1)
    print("Now, your adventure begins!")
    time.sleep(2)
    print("I'll miss you...")
    os.system("cls")
    return player