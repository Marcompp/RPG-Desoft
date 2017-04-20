# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:40:37 2017

@author: Raphael
"""
import random as rd
import time
import Batalha as btl
import json


with open ("Chars.json") as chars:
    Char = json.load(chars)
    
with open ("Weapons.json") as wpns:
    Wpn = json.load(wpns)

def Encount(jog,loc):
    rend = rd.randint(0, len(loc["inimigos"]))
    print("Você foi atacado por {0}!!!".format(loc['inimigos'][rend]))
    btl.Comando(jog,Char[loc['inimigos'][rend]])

def Passear(jog,loc,step):
    print("Você está n{0}.".format(loc["nome"]))
    time.sleep(1.5)
    rand = rd.randint(0, 10)
    if rand <= loc["encounter"]:
        Encount(jog,loc)
        step+=1
    elif rand == loc['loot']:
        a = input("Você encontrou um tesouro, deseja abrir?(S ou N?) ")
        if a == 'S':
            randi = rd.randint(0, len[loc]['treasure'])
            print("Você achou {0}!".format(loc['treasure'][randi]))
    if step == 0:
        print("Ainda há um grande caminho a percorrer.\nVocê anda um pouco em direção a seu próximo objetivo")
        step = 1
        return step
    elif step == 1:
        print("Você sente já estar no meio do caminho, com isso em mente você continua seu caminho sossegado")
        step = 2
        return step
    elif step == 2:
        print("Já é possivel ver a próxima área, falta pouco para sair desse local!!\n Você sente uma presença maligna olhando para você")
        step = 3
        return step