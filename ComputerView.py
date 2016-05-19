#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from Event import Event

class ComputerView(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        
        self.computeRequest = Event()
        
        
        Label(self, text=u"Masse à dissoudre :").grid(row = 0, column = 0)
        self.MassToDissolve = StringVar()
        Entry(self, textvariable=self.MassToDissolve).grid(row = 0, column = 1)
        
        Label(self,text=u"Masse molaire :").grid(row = 1, column = 0)
        self.MolarMass = StringVar()
        Entry(self, textvariable=self.MolarMass).grid(row= 1, column = 1)
        
        Label(self,text=u"Volume recherché :").grid(row = 2, column = 0)
        self.Volume = StringVar()
        Entry(self, textvariable=self.Volume).grid(row = 2, column = 1)
        
        Label(self,text=u"Concentration :").grid(row = 3, column = 0)
        self.Concentration = StringVar()
        Entry(self, textvariable=self.Concentration).grid(row = 3, column = 1)
        
        Button(self,text="Calculer", command=self.compute).grid(row=4, column=0)
        Button(self,text="Reset", command=self.init).grid(row=4, column=1)
        
        self.init()

        
       
    def init(self):
		self.MassToDissolve.set(0)
		self.MolarMass.set(0)
		self.Volume.set(0)
		self.Concentration.set(0)
       
    def compute(self):
		self.computeRequest()
		
		
        
        
    
        
        
	

        

