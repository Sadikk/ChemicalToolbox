#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from Event import Event

class ComputerView(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        
        self.MTDChanged = Event()
        self.MSChanged = Event()
        self.VolumeChanged = Event()
        self.ConcentrationChanged = Event()
        
        
        Label(self, text=u"Masse à dissoudre :").grid(row = 0, column = 0)
        self.MassToDissolve = StringVar()
        Entry(self, textvariable=self.MassToDissolve).grid(row = 0, column = 1)
        self.MassToDissolve.trace("w",lambda name, index, mode, var=self.MassToDissolve:self.onMTDChanged(var))
        
        Label(self,text=u"Masse molaire :").grid(row = 1, column = 0)
        self.MolarMass = StringVar()
        Entry(self, textvariable=self.MolarMass).grid(row= 1, column = 1)
        self.MolarMass.trace("w", lambda name, index, mode, var=self.MolarMass:self.onMSChanged(var))
        
        Label(self,text=u"Volume recherché :").grid(row = 2, column = 0)
        self.Volume = StringVar()
        Entry(self, textvariable=self.Volume).grid(row = 2, column = 1)
        self.Volume.trace("w", lambda name, index, mode, var=self.Volume:self.onVolumeChanged(var))
        
        Label(self,text=u"Concentration :").grid(row = 3, column = 0)
        self.Concentration = StringVar()
        Entry(self, textvariable=self.Concentration).grid(row = 3, column = 1)
        self.Concentration.trace("w", lambda name, index, mode, var=self.Concentration:self.onConcentrationChanged(var))
        
        

    def onMTDChanged(self, sv):
        self.MTDChanged(sv.get())
        
    def onMSChanged(self, sv):
		self.MSChanged(sv.get())
		
    def onVolumeChanged(self, sv):
        self.VolumeChanged(sv.get())
		
    def onConcentrationChanged(self, sv):
        self.ConcentrationChanged(sv.get())

        

