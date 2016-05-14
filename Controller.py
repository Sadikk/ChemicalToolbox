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


#region ConcentrationHandlers
def MTDHandler(param):
    if str.isdigit(param):
        model.computer.setMassToDissolve(int(param))
    else:
        model.computer.setMassToDissolve(0)

def MSHandler(param):
    if str.isdigit(param):
        model.computer.setMolarmass(int(param))
    else:
        model.computer.setMolarmass(0)
	  
def ConcentrationHandler(param):
    if str.isdigit(param):
	    model.computer.setConcentration(int(param))
    else:
        model.computer.setConcentration(0)
	  
def VolumeHandler(param):
    if str.isdigit(param):
        model.computer.setVolume(int(param))
    else:
        model.computer.setVolume(0)
		 
	  
def ComputedHandler():
    window.toolView.MassToDissolve.set(model.computer.getMassToDissolve())
    window.toolView.MolarMass.set(model.computer.getMolarmass())
    window.toolView.Concentration.set(model.computer.getConcentration())
    window.toolView.Volume.set(model.computer.getVolume())
#endregion

#region BalanceHandler
def balanceHandler():
    #todo envoyer les resultats à la view
    coef = model.balance.balanceEquation(window.toolView.R1.get(), \
    window.toolView.R2.get(), \
    window.toolView.P1.get(), \
    window.toolView.P2.get())
#endregion

#region MainHandler
def clickHandler(param):
    if param == "TABLEAU":
        window.createTableView()
    elif param == "EQUATION":
        window.createBalanceView()
        window.toolView.balanceRequest.append(balanceHandler)
    elif param == "CONCENTRATION":
        window.createComputerView()
        window.toolView.MTDChanged.append(MTDHandler)
        window.toolView.MSChanged.append(MSHandler)
        window.toolView.ConcentrationChanged.append(ConcentrationHandler)
        window.toolView.VolumeChanged.append(VolumeHandler)
#endregion
    
    	      
def onClosing():
    #fermer la base de données à la fermeture de la fenêtre
    model.db.close()
    window.destroy()

#handle le signal de sortie
window.protocol("WM_DELETE_WINDOW", onClosing)
model.computer.computed.append(ComputedHandler)
window.click.append(clickHandler)
window.mainloop()
