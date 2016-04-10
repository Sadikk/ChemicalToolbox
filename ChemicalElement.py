#!/usr/bin/env python
# -*- coding: utf-8 -*-



"""
Classe représentant un élément chimique du tableau périodique des élements
"""

from Tkinter import Button
import tkMessageBox

class ChemicalElement:
    #atomes dont le fond sera violet/rose (le reste sera vert)
    pinkAtoms = [ 1 , 2 , 3 , 4 , 11 , 12 ] 
    
    def __init__(self, name, symbol, an, aw, vw, mt, bt):
        self.name = name     #nom
        self.symbol = symbol #symbole 
        self.atomicNumber = an #numéro atomique
        self.atomicWeight = aw #masse atomique
        self.volumicWeight = vw #masse volumique
        self.meltingTemp = mt #température de fusion
        self.boilingTemp = bt #température d'ébullition
        
    def getButton(self, master):
        """
            Crée un label contenant la chaîne de texte formatée des 
            informations de l'élément
            
            :param master: Fenêtre parente du label
            :type master: Tkinter window ou tkinter frame
            :return: Un label contenant la chaîne formatée
            :rtype: Label
        """
        return Button(master, height = 5, width = 5, \
        bg="purple" if self.atomicNumber in ChemicalElement.pinkAtoms else "green", \
         text=self.symbol, command = self.show)
        
    def show(self):
        """
            Affiche une boîte d'informations affichant les propriétés
            chimiques de l'élement
            
            :return: None
            :rtype: void
        """
        tkMessageBox.showinfo("Infos sur : " + self.name, \
        "Nom : " + self.name + " \n" + \
        "Symbole : " + self.symbol + " \n" + \
        "Numéro atomique : " + str(self.atomicNumber) + " \n" + \
        "Masse atomique : " + str(self.atomicWeight) + " \n" + \
        "Masse volumique : " + str(self.volumicWeight) + " \n" + \
        "Température de fusion : " + str(self.meltingTemp) + " \n" + \
        "Température d'ébullition : " + str(self.boilingTemp) + " \n")

        
    def __repr__(self):
        return self.name + " " + self.symbol + " " + str(self.atomicWeight) + " " + \
        self.volumicWeight
        
    

    
        
    
