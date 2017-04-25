# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:40:37 2017

@author: Raphael
"""
import random as rd
import time
import Batalha as btl
import json
import os
import Save as sav

def Village():
    with open ("Chars.json") as chars:
        Char = json.load(chars)
    with open ("Player.json") as play:
        player = json.load(play)
    print('"Welcome to our village, take a look around and see if you anything interesting."')
    TTD = ["1)Shop","2)Promote","3)Train","4)Challenge","5)Leave"]
    while True:
        command="aaaa"
        os.system("cls")#ClearScreen
        while command not in range(1,6):
            print("What will you do?")
            for z in TTD:
                time.sleep(0.5)
                print(z)
            command = (input(""))
            if command == (""):
                continue
            else:
                command = int(command)
        if command == 1:
            print("We are currently not open for business, but have these as a token of my gratitude for coming by.")
            time.sleep(2)
            print("You got 5 potions!!")
            with open("Inventario.json","r") as inv:
                Inv = json.load(inv)
            Inv["Potion"]["quant"] += 5
            sav.SaveGameI(Inv)
            pass
        elif command == 2:
            sav.Promote()
            pass
        elif command == 3:
            btl.Begin(player,Char["Trainer"])
        elif command == 4:
            u = input("Are you sure? You're up for a great challenge.(Y or N) ")
            if u.upper() == "Y":
                rand = rd.randint(0,3)
                if rand == 0:
                    btl.Begin(player,Char["Agnes"])
                elif rand == 1:
                    btl.Begin(player,Char["Borin"])
                elif rand == 2:
                    btl.Begin(player,Char["Lala"])
        elif command == 5:
            break
        


def Passar(loc):
    if loc == "Apple Woods":
        print("Through an opening amongst the trees, you have arrived at the legendary Caves of Light.")
        time.sleep(3)
        return "Caves of Light"
    elif loc == "Caves of Light":
        print("After endless venturing through the mazelike caves, \nyou finally arrive at the exit to the Sundown Plateau.")
        time.sleep(3)
        print("At the plateau, you find the small village of Bertunia.")
        time.sleep(2)
        Village()
        return "Sundown Plateau"
    elif loc == "Sundown Plateau":
        print("On the horizon you spot your next destination, Mt. Legory, and make your way there.")
        time.sleep(3)
        return "Mt. Legory"
    elif loc == "Mt. Legory":
        print("You find an entrance on the cliffside and follow it until you discover the Core Cavern.")
        time.sleep(3)
        return "Core Cavern"
    elif loc == "Core Cavern":
        print("At the exit of the Cavern you find yourself at the Lost Swamp,\n a place few have ever escaped from.")
        time.sleep(3)
        print("Next to swamp there lies Muggle Town, a small fishing village.")
        time.sleep(2)
        Village()
        return "Lost Swamp"
    elif loc == "Lost Swamp":
        print("Treading through the accursed swamp, you find your final destination,\n the Arcmat Ruins, said to be the birthplace of all magic.")
        time.sleep(3)
        return "Arcmat Ruins"
    elif loc == "Arcmat Ruins":
        print("After finishing your epic quest,\n you decide to chill and kill monsters and let off some steam at the ARENA!!!")
        time.sleep(3)
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
        print("You are currently at {0}.".format(loc["nome"]))
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
            step += 1
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