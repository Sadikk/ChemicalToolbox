#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Vue du pattern MVC - Presentation des données et interaction avec 
l'utilisateur
"""

from Tkinter import *
class View(Tk):
	def __init__(self):
		Tk.__init__(self)
		
		self.headerLb = Label(self,bg="blue",text="BOITE A OUTILS POUR LA CHIMIE")
		self.headerLb.grid(row=0, column=0, columnspan=2)
		
		self.tableBt = Button(self,bg ="blue", text="Tableau periodique")
		self.tableBt.grid(row = 1, column=0)
		
		self.EquationBt = Button(self, bg="blue",text="Equilibrer une equation")
		self.EquationBt.grid(row=1,column=1)
		
		self.concentrationBt=Button(self,bg="blue", text="Concentration")
		self.concentrationBt.grid(row=2, column=0, columnspan=2)
		
		
		

root = View()
root.mainloop()
		
	
