#!/usr/bin/env python
# -*- coding: utf-8 -*-

from DatabaseManager import DatabaseManager
from View import View
from Model import Model

"""
Main file
"""

model = Model()
window = View()



def MTDHandler(param):
	model.computer.setMassToDissolve(int(param))

def MSHandler(param):
	model.computer.setMolarmass(int(param))
	  
def ConcentrationHandler(param):
	model.computer.setConcentration(int(param))
	  
def VolumeHandler(param):
	model.computer.setVolume(int(param))	 
	  
def ComputedHandler():
	window.toolView.MassToDissolve.set(model.computer.getMassToDissolve())
	    
def clickHandler(param):
    if param == "TABLEAU":
        window.createTableView()
    elif param == "EQUATION":
        window.createBalanceView()
    elif param == "CONCENTRATION":
        window.createComputerView()
        window.toolView.MTDChanged.append(MTDHandler)
        window.toolView.MSChanged.append(MSHandler)
        window.toolView.ConcentrationChanged.append(ConcentrationHandler)
        window.toolView.VolumeChanged.append(VolumeHandler)
    
    	      
def onClosing():
    #fermer la base de données à la fermeture de la fenêtre
    model.db.close()
    window.destroy()

#handle le signal de sortie
window.protocol("WM_DELETE_WINDOW", onClosing)
model.computer.computed.append(ComputedHandler)
window.click.append(clickHandler)
window.mainloop()
