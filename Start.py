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
player["HP"] = player["MHP"]
sav.SaveGameP(player)

location = Loca["Apple Woods"]
step = 3

#save stuff
os.system("cls")#ClearScreen
#print("What will you do?")
options = ["1)Adventure","2)Train","3)Sleep","4)Bestiary"]
command="aaaa"
while command not in range(1,5):
    print("What will you do?")
    for n in options:
        time.sleep(0.5)
        print(n)
    command = int(input(""))
if command == 1:
    step = psa.Passear(player,location,step)