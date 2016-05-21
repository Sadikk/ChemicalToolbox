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
def computeRequestHandler():
    """
        Lance le calcul de concentration
    """
	model.computer.setMassToDissolve(float(window.toolView.MassToDissolve.get()))
	model.computer.setMolarmass(float(window.toolView.MolarMass.get()))
	model.computer.setConcentration(float(window.toolView.Concentration.get()))
	model.computer.setVolume(float(window.toolView.Volume.get()))
	model.computer.checkMissing()	 
	  
def computedHandler():
    """
        Affiche les résultats du calcul sur l'interface
    """
    window.toolView.MassToDissolve.set(model.computer.getMassToDissolve())
    window.toolView.MolarMass.set(model.computer.getMolarmass())
    window.toolView.Concentration.set(model.computer.getConcentration())
    window.toolView.Volume.set(model.computer.getVolume())
#endregion

#region BalanceHandler
def balanceHandler():
    """
        Lance l'équilibrage de l'équation et envoie les resultats sur 
        l'interface graphique
    """
    coef = model.balance.balanceEquation(window.toolView.R1.get(), \
    window.toolView.R2.get(), \
    window.toolView.P1.get(), \
    window.toolView.P2.get())
    
    window.toolView.equation.set(str(coef[0]) + window.toolView.R1.get() + \
    " + " + str(coef[1]) + window.toolView.R2.get() + " -> " + \
    str(coef[2]) + window.toolView.P1.get() + \
    " + " + str(coef[3]) + window.toolView.P2.get())
#endregion

#region MainHandler
def clickHandler(param):
    """
        Crée la vue correspondant à l'outil sélectionné sur l'interface
        principale
    """
    if param == "TABLEAU":
        window.createTableView()
    elif param == "EQUATION":
        window.createBalanceView()
        window.toolView.balanceRequest.append(balanceHandler)
    elif param == "CONCENTRATION":
        window.createComputerView()
        window.toolView.computeRequest.append(computeRequestHandler)
#endregion
    
    	      
def onClosing():
    #fermer la base de données à la fermeture de la fenêtre
    model.db.close()
    window.destroy()

#handle le signal de sortie
window.protocol("WM_DELETE_WINDOW", onClosing)
model.computer.computed.append(computedHandler)
window.click.append(clickHandler)
window.mainloop()
