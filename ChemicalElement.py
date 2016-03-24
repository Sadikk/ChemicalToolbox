#!/usr/bin/env python
# -*- coding: utf-8 -*-



"""
Classe représentant un élément chimique du tableau périodique des élements
"""

from Tkinter import Label

class ChemicalElement:
	def __init__(self, name, symbol, an, density, appearance):
		self.name = name
		self.symbol = symbol
		self.atomicNumber = an
		self.density = density
		self.appearance = appearance
		
	def getLabel(self, master):
		"""
			Crée un label contenant la chaîne de texte formatée des 
			informations de l'élément
			
			:param master: Fenêtre parente du label
			:type master: Tkinter window ou tkinter frame
			:return: Un label contenant la chaîne formatée
			:rtype: Label
		"""
		return Label(master, text="Nom : " + name + " \n" + \
		"Symbole : " + symbol + " \n" + \
		"Numéro atomique : " + an + " \n" + \
		"Densité : " + density + " \n" + \
		"Apparence : " + appearance + " \n")
		
	def __repr__(self):
		return self.name + " " + self.symbol + " " + str(self.density) + " " + \
		self.appearance

	
		
	
