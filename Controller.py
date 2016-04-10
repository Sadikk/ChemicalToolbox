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

def clickHandler(param):
    if param == "TABLEAU":
        window.createTableView()
    elif param == "EQUATION":
        window.createBalanceView()
    elif param == "CONCENTRATION":
        window.createComputerView()
    
def onClosing():
    #fermer la base de données à la fermeture de la fenêtre
    model.db.close()
    window.destroy()

#handle le signal de sortie
window.protocol("WM_DELETE_WINDOW", onClosing)
window.click.append(clickHandler)
window.mainloop()
