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
        self.MassToDissolve.trace("w", lambda name, index, mode, \
			self.MassToDissolve=self.MassToDissolve: self.onMTDChanged(self.MassToDissolve))
        
        
        Label(self,text=u"Masse molaire :").grid(row = 1, column = 0)
        self.MolarMass = StringVar()
        Entry(self, textvariable=self.MolarMass).grid(row= 1, column = 1)
        self.MolarMass.trace("w", lambda name, index, mode, \
			self.MolarMass=self.MolarMass: self.onMSChanged(self.MolarMass))
        
        Label(self,text=u"Volume recherché :").grid(row = 2, column = 0)
        self.Volume = StringVar()
        Entry(self, textvariable=self.Volume).grid(row = 2, column = 1)
        self.Volume.trace("w", lambda name, index, mode, \
			self.Volume=self.Volume: self.onVolumeChanged(self.Volume))
        
        Label(self,text=u"Concentration :").grid(row = 3, column = 0)
        self.Concentration = StringVar()
        Entry(self, textvariable=self.Concentration).grid(row = 3, column = 1)
        self.Concentration.trace("w", lambda name, index, mode, \
			self.Concentration=self.Concentration: self.onConcentrationChanged(self.Concentration))
        
    
    def onMTDChanged(self, sv):
		self.MTDChanged(sv.get())
		
	def onMSChanged(self, sv):
		self.MSChanged(sv.get())
		
	def onVolumeChanged(self, sv):
		self.VolumeChanged(sv.get())
		
	def onConcentrationChanged(self, sv):
		self.ConcentrationChanged(sv.get())

        

