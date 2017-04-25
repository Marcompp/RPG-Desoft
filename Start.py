# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:02:00 2017

@author: marco
"""

import json
import Batalha as blt
import Passear as psa
import Misc as misc
import Save as sav
import os
import time

with open ("Chars.json") as chars:
    Char = json.load(chars)
    
with open ("Weapons.json") as wpns:
    Wpn = json.load(wpns)
    
with open ("Locations.json") as loca:
    Loca = json.load(loca)

with open ("Player.json") as play:
    player = json.load(play)

       
if player == {"Start":0}:
    player = misc.NewGame()
else:
    print("What would you like to do?")
    print("1) Continue")
    print("2) Start New Game")
    resp = int(input(""))
    if resp == 2:
        print("Are you sure you want to delete your game?(Y/N)")
        resp = input("")
        if resp == "Y":
            sav.StartOver()
            player = misc.NewGame()
    
player["HP"] = player["MHP"]
sav.SaveGameP(player)


#save stuff
#print("What will you do?")
options = ["1)Adventure","2)Train","3)Sleep","4)Bestiary"]
while True:
    with open ("Player.json") as play:
        player = json.load(play)
    with open ("Adventure.json") as adv:
        Adv = json.load(adv)
    location = Loca[Adv["loc"]]
    step = Adv["step"]
    with open ("Beast.json") as bst:
        Bst = json.load(bst)
    command="aaaa"
    os.system("cls")#ClearScreen
    while command not in range(1,5):
        print("What will you do?")
        for n in options:
            time.sleep(0.5)
            print(n)
        command = (input(""))
        if command==(""):
            continue
        else:
            command = int(command)
    if command == 1:
        step = psa.Passear(player,location,step)
        location = location["nome"]
        if step == 4:
            location = psa.Passar(location)
            step = 0
        Adv["loc"] = location
        Adv["step"] = step
        sav.SaveGameA(Adv)
    if command == 2:
        psa.Encount(player,location)
    if command == 3:
        adventure = {"loc":location,"step":step}
        with open ("Inventario.json") as inv:
            inventario = json.load(inv)
        sav.SaveAll(player,Bst,inventario,adventure)
        break
    if command == 4:
        os.system("cls")
        print("Enemies fought:")
        for h in Bst:
            time.sleep(0.5)
            print("{0} (Lv: {1}, HP:{2}, Atk:{3}, Skl:{4}, Spd:{5}, Lck:{6}, Def:{7}, Weapon: {8}, Techs: {9})".format(Bst[h]["nome"],Bst[h]["lvl"],Bst[h]["HP"],Bst[h]["atk"],Bst[h]["skl"],Bst[h]["spd"],Bst[h]["lck"],Bst[h]["def"],Bst[h]["Weapon"],Bst[h]["Techs"]))
        input("")