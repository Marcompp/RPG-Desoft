# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:40:37 2017

@author: Raphael
"""
import random as rd
import time
import Batalha as btl
import json



    
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