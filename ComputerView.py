#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

class ComputerView(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        Label(self, text=u"Masse à dissoudre :").grid(row = 0, column = 0)
        self.MassToDissolve = StringVar()
        Entry(self, textvariable=self.massToDissolve).grid(row = 0, column = 1)
        Label(self,text=u"Masse molaire :").grid(row = 1, column = 0)
        self.MolarMass = StringVar()
        Entry(self, textvariable=self.molarMass).grid(row= 1, column = 1)
        Label(self,text=u"Volume recherché :").grid(row = 2, column = 0)
        self.Volume = StringVar()
        Entry(self, textvariable=self.volume).grid(row = 2, column = 1)
        Label(self,text=u"Concentration :").grid(row = 3, column = 0)
        self.Concentration = StringVar()
        Entry(self, textvariable=self.concentration).grid(row = 3, column = 1)
        

