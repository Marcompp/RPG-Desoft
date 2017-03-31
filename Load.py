# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 10:49:03 2017

@author: marco
"""

import json

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

Weapons= {"Broadsword":{"Mgt":11,"Acc":65,"Wgt":10,"Crit":5},"Poleaxe":{"Mgt":11,"Acc":65,"Wgt":10,"Crit":5}}
Agnes["Weapon"]= Weapons["Broadsword"]
Borin["Weapon"]=Weapons["Poleaxe"]

import Batalha.py as blt
blt.turno(Agnes,Borin)