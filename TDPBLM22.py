# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:55:25 2018

@author: roch25u
"""
def read():
    os.chdir('U:\')
    f=open('p022_names.txt', 'r')
    for ligne in f:
        chaine=ligne
        liste=chaine.split(',')
    f.close()
    return(liste)

print(read())

def indice_lettre(lettre):
    chaine='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    x=1
    for i in chaine:
        if chaine(i)==lettre:
            return x
        else:
            x+=1
            
def somme_mot(liste):
    somme=0
    for k in range (len(liste)):
        somme+=range(liste[k])*indice_lettre(liste[k])
    return somme

def somme_liste_totale(liste):
    somme_totale=0
    for k in range (len(liste)):
        somme_totale+=somme_mot(liste[k])
    return somme_totale

