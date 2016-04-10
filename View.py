#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Vue du pattern MVC - Presentation des données et interaction avec 
l'utilisateur
"""

from Tkinter import *
from Event import Event
from PeriodicTable import PeriodicTable
from ComputerView import ComputerView
from BalanceView import BalanceView

class View(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Boite à outils - Chimie")
        
        #region MainFrame
        self.mainFrame = Frame(self)
        self.mainFrame.grid(row=0, column=0)
        
        self.headerLb = Label(self.mainFrame,width=50,bg="blue",fg="white",text="BOITE A OUTILS POUR LA CHIMIE")
        self.headerLb.grid(row=0, column=0, columnspan=2, pady=5)
        
        self.tableBt = Button(self.mainFrame,width=20,bg ="blue", fg="white",\
        text="Tableau periodique", command = lambda : self.onClick("TABLEAU"))
        self.tableBt.grid(row = 1, column=0, pady=5)
        
        self.equationBt = Button(self.mainFrame,width=20, bg="blue",fg="white",\
        text="Equilibrer une equation", command = lambda : self.onClick("EQUATION"))
        self.equationBt.grid(row=1,column=1, pady=5)
        
        self.concentrationBt=Button(self.mainFrame,width=50,bg="blue",fg="white", \
        text="Concentration", command = lambda : self.onClick("CONCENTRATION"))
        self.concentrationBt.grid(row=2, column=0, columnspan=2, pady=5)
        #endregion
        
        
        self.toolFrame = Frame(self, height=30, width=50)
        self.toolFrame.grid(row=4, column=0, columnspan=2, pady = 20)
        self.toolView = None
        self.click = Event()
        
    def onClick(self, param):
        self.click(param)
        
    def createTableView(self):
        self.clear()
        self.toolView = PeriodicTable(self.toolFrame)
        self.toolView.pack()
        
    def createComputerView(self):
        self.clear()
        self.toolView = ComputerView(self.toolFrame)
        self.toolView.pack()
        
    def createBalanceView(self):
        self.clear()
        self.toolView = BalanceView(self.toolFrame)
        self.toolView.pack()
        
    def clear(self):
        #supprime les anciens widgets si il y a 
        for widget in self.toolFrame.winfo_children():
            widget.destroy()
        
    
