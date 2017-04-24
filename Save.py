# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:17:00 2017

@author: Raphael
"""

import json


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
        
        
        
def SaveAll(PD,BD,ID,AD):
    SaveGameP(PD)
    SaveGameB(BD)
    SaveGameI(ID)
    SaveGameA(AD)
        
SaveAll(A,A,A,A)


        

    
    
    