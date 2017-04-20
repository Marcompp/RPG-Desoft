# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 14:01:58 2017

@author: marco
"""

import json
import os
import time

with open ("Weapons.json") as wpns:
    Wpn = json.load(wpns)
    
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
            