#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Classe représentant le tableau périodique des élements
"""
from Model import Model
from Tkinter import *

class PeriodicTable(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.elements = Model.instance.getElements()
        self.buttons = []
        for e in self.elements:
            #pour chaque element on recupere le bouton correspondant
            self.buttons.append(e.getButton(self))
            
        #region ligne du haut du tableau
        Label(self, width=5, height=2, bg="grey", text = "1").grid(row = 0, column = 0, pady=1)
        Label(self, width=5, height=2, bg="grey", text = "2").grid(row = 0, column = 1, pady=1)
        for i in range(13,18):
            Label(self, width=5, height=2, bg="grey", text = str(i)).grid(row = 0, column = i - 11, pady=1)
        #endregion
        
        #region Insertion des elements dans le tableau
        for i in range(0,17):
            an = i + 1 #le numero atomique
            if an == 1:
                self.buttons[i].grid(row = 1, column = 0)
            elif an == 2:
                self.buttons[i].grid(row = 1, column = 6)
            elif an in range(3,10):
                self.buttons[i].grid(row = 2, column = an - 3)
            elif an in range(11, 18):
                self.buttons[i].grid(row = 3, column = an - 11)
        
        
    
