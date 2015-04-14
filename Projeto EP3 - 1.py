# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:55:49 2015

@author: vitor_000
"""
import tkinter 

limpa = []
arquivo = open("alimentos.csv", "r+")
leitura = arquivo.readlines()
#print(leitura)

for i in leitura:
    #i =i.replace("\n","")
    i = i.strip()
    limpa.append(i)
print(limpa)

nome 

for i in range(len(limpa)):