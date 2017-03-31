# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 10:49:03 2017

@author: marco
"""

import json
import Batalha as blt

def mostra(b):
    for c in b:
        print("{}".format(b[c]))


with open ("Chars.json") as chars:
    Char = json.load(chars)
    
for b in Char:
    #print(b)
    mostra(Char[b])
    
Agnes = Char["Agnes"]
Borin = Char["Borin"]

Weapons= {"Broadsword":{"mgt":11,"acc":65,"wgt":10,"crit":5},"Poleaxe":{"mgt":11,"acc":65,"wgt":10,"crit":5}}
Agnes["Weapon"]= Weapons["Broadsword"]
Borin["Weapon"]=Weapons["Poleaxe"]

blt.Turno(Agnes,Borin)