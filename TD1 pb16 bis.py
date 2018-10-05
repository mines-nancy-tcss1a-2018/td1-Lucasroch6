# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def probleme16(p):
	x=2**p
	L=str(x)
	somme_chiffres=0
	for k in range (len(L)):
		somme_chiffres+=int(L[k])
	return somme_chiffres

assert (probleme16(1000)==1366)
print(probleme16(1000))