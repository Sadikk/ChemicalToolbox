#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Modele du pattern MVC - Manipule les données
"""
from DatabaseManager import DatabaseManager
from ConcentrationComputer import ConcentrationComputer
from Balance import Balance

class Model():
    instance = None
    
    def __init__(self):
        Model.instance = self
        self.db = DatabaseManager("periodic.sqlite")
        self.computer = ConcentrationComputer()
        self.balance = Balance()
        
    def getElements(self):
        """
            Retourne les elements chimiques depuis la base de données
        """
        elements = self.db.fetchElements()
        return elements
        
