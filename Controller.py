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
def ComputeRequestHandler():
	model.computer.setMassToDissolve(float(window.toolView.MassToDissolve.get()))
	model.computer.setMolarmass(float(window.toolView.MolarMass.get()))
	model.computer.setConcentration(float(window.toolView.Concentration.get()))
	model.computer.setVolume(float(window.toolView.Volume.get()))
	model.computer.checkMissing()	 
	  
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
        window.toolView.computeRequest.append(ComputeRequestHandler)
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
