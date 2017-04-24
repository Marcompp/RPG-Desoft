# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:40:37 2017

@author: Raphael
"""
import random as rd
import time
import Batalha as btl
import json

def Passar(loc):
    if loc == "Apple Woods":
        print("Through an opening amongst the trees, you have arrived at the legendary Caves of Light.")
        time.sleep(2)
        return "Caves of Light"
    elif loc == "Caves of Light":
        print("After endless venturing through the mazelike caves, /nyou finally arrive at the exit to the Sundown Plateau")
        time.sleep(2)
        return "Sundown Plateau"
    elif loc == "Sundown Plateau":
        print("On the horizon you spot your next destination, Mt. Legory, and make your way there")
        time.sleep(2)
        return "Mt. Legory"
    elif loc == "Mt. Legory":
        print("You find an entrance on the cliffside and follow it until you discover the Core Cavern")
        time.sleep(2)
        return "Core Cavern"
    elif loc == "Core Cavern":
        print("At the exit of the Cavern you find yourself at the Lost Swamp,/n a place few have ever escaped from")
        time.sleep(2)
        return "Lost Swamp"
    elif loc == "Lost Swamp":
        print("Treading through the accursed swamp, you find your final destination,/n the Arcmat Ruins, said to be the birthplace of all magic")
        time.sleep(2)
        return "Arcmat Ruins"
    elif loc == "Arcmat Ruins":
        print("After finishing your epic quest,/n you decide to chill and kill monsters and let off some steam at the ARENA!!!")
        time.sleep(2)
        return "The Arena"
        
    
with open ("Weapons.json") as wpns:
    Wpn = json.load(wpns)

def Encount(jog,loc):
    with open ("Chars.json") as chars:
        Char = json.load(chars)
    rend = rd.randint(0, len(loc["inimigos"])-1)
    print("You found a {0}!".format(loc['inimigos'][rend]))
    time.sleep(2)
    btl.Begin(jog,Char[loc['inimigos'][rend]])
    

def Passear(jog,loc,step):
    if step < 3:
        print("You are currently in {0}.".format(loc["nome"]))
        time.sleep(2)
        print("You walk around for a while")
        time.sleep(2)
        rand = rd.randint(0, 10)
        if rand <= loc["encounter"]:
            Encount(jog,loc)
            step+=1
        elif rand == loc['loot']:
            a = input("You found a treasure chest, do you wish to open it?(Y ou N?) ")
            if a == 'Y':
                randi = rd.randint(0, len[loc]['treasure']-1)
                print("You found {0}!".format(loc['treasure'][randi]))
                time.sleep(1)
                step += 1
                return step
        else:
            print("You walked for hours with nothing to show for it.")
            time.sleep(2)
        if step == 0:
            return step
        if step == 1:
            print("There is still a long path ahead of you.\nYou walk forward towards your objective.")
            time.sleep(2)
            step = 1
            return step
        elif step == 2:
            print("You feel you are halfway there, you continue following the path at ease.")
            time.sleep(2)
            step = 2
            return step
        elif step == 3:
            print("You can already see the next area, the exit is only a small journey away!!\nYou feel an evil presence watching you...")
            time.sleep(2)
            step = 3
            return step
    else:
        CT = input("You foresee a big battle ahead. Do you really wish to proceed? (Y or N) ")
        if CT.upper() == "N":
            return 3
        else:
            with open ("Chars.json") as chars:
                    Char = json.load(chars)
            print("The big boss of {1}, {0} is in front of you.".format(loc["boss"],loc["nome"]))
            time.sleep(3)
            btl.Begin(jog,Char[loc['boss']])
            return 4
    if step == 4:
        print("You see the exit right in front of you, so you carry on.")
        time.sleep(2)
        return 4