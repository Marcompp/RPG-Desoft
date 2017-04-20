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
    rend = rd.randint(0, len(loc["inimigos"])-1)
    print("Você foi atacado por {0}!!!".format(loc['inimigos'][rend]))
    time.sleep(3)
    btl.Comando(jog,Char[loc['inimigos'][rend]])
    

def Passear(jog,loc,step):
    if step < 3:
        print("Você está n{0}.".format(loc["nome"]))
        time.sleep(1.5)
        rand = rd.randint(0, 10)
        if rand <= loc["encounter"]:
            Encount(jog,loc)
            step+=1
        elif rand == loc['loot']:
            a = input("Você encontrou um tesouro, deseja abrir?(S ou N?) ")
            if a == 'S':
                randi = rd.randint(0, len[loc]['treasure']-1)
                print("Você achou {0}!".format(loc['treasure'][randi]))
        else:
            print("Você andou por horas sem achar nada de interesse")
        if step == 0:
            print("Ainda há um grande caminho a percorrer.\nVocê anda um pouco em direção a seu próximo objetivo")
            step = 1
            return step
        elif step == 1:
            print("Você sente já estar no meio do caminho, com isso em mente você continua seu caminho sossegado")
            step = 2
            return step
        elif step == 2:
            print("Já é possivel ver a próxima área, falta pouco para sair desse local!!\nVocê sente uma presença maligna olhando para você")
            step = 3
            return step
    else:
        CT = input("Você preve uma grande luta a frente. Deseja realmente ir a frente?(S ou N) ")
        if CT == "N":
            return 3
        else:
            print("O chefe da área {0} aparece!!".format(loc["boss"]))
            btl.Comando(jog,Char[loc['boss']])
            return 4
    if step == 4:
        print("Você ve a saída na sua frente, siga com sua jornada")
        