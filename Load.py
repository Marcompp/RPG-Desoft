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
    Agn = json.load(chars)
    
for b in Agn:
    #print(b)
    mostra(Agn[b])