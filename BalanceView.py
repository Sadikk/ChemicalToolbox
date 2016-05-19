#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from Event import Event

class BalanceView(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        
        #event declenché lorsqu'on veut equilibrer l'equation
        #signale au controller de declencher l'equilibrage
        self.balanceRequest = Event()
        
        #region Reactifs
        Label(self, text="Reactif 1: ").grid(row = 0, column = 0)
        self.R1= StringVar()
        Entry(self,textvariable=self.R1).grid(row = 0, column = 1)
        
        Label(self, text="Reactif 2: ").grid(row = 1, column = 0)
        self.R2= StringVar()
        Entry(self,textvariable=self.R2).grid(row = 1, column = 1)
        #endregion
        
        #region Produits
        Label(self, text="Produit 1: ").grid(row = 2, column = 0)
        self.P1= StringVar()
        Entry(self,textvariable=self.P1).grid(row = 2, column = 1)
        
        Label(self, text="Produit 2: ").grid(row = 3, column = 0)
        self.P2= StringVar()
        Entry(self,textvariable=self.P2).grid(row = 3, column = 1)
        #endregion
        
        #bouton pour equilibrer
        Button(self, text="Equilibrer", command=self.balance).grid(row = 4, column = 0, columnspan = 2)
        
        self.equation = StringVar()
        Label(self, textvariable=self.equation).grid(row = 5, column= 0, columnspan=2, pady=10)
        
    def balance(self):
        #on declenche l'event
        self.balanceRequest()
