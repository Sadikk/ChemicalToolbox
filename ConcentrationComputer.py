#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Classe gérant tous les calculs liés à la concentration
"""
class ConcentrationComputer:
    def __init__(self):
        self._molarMass = 0
        self._volume = 0
        self._concentration = 0
        self._massToDissolve = 0
        pass
        
def computeMolarMass(self):
    """
        Calcule la masse molaire
    """
    #todo Thibaut
    
def computeVolume(self):
    """
        Calcule le volume
    """
    #todo Thibaut
    
def computeConcentration(self):
    """
        Calcule la concentration
    """
    #todo Thibaut
    
def computeMassToDissolve(self):
    """
        Calcule la masse à dissoudre
    """
    #todo Thibaut
    
def checkMissing(self):
    """
        Verifie si chaque valeur a été remplie et calcule la valeur
        manquante si nécessaire
    """
    #todo Thibaut
    
#region Properties
def getMolarmass(self):
    """
        Accesseur de la masse molaire
    """
    return self._molarMass
    
def setMolarmass(self, value):
    """
        Mutateur de la masse molaire 
    """
    self._molarMass = value
    self.checkMissing()
    
def getVolume(self):
    """
        Accesseur du volume
    """
    return self._volume
    
def setVolume(self, value):
    """
        Mutateur du volume
    """
    self._volume = value
    self.checkMissing()
    
def getConcentration(self):
    """
        Accesseur de la concentration
    """
    return self._concentration

def setConcentration(self, value):
    """
        Mutateur de la concentration
    """
    self._concentration = value
    self.checkMissing()
    
def getMassToDissolve(self):
    """
        Accesseur de la masse à dissoudre 
    """
    return self._massToDissolve
    
def setMassToDissolve(self, value):
    """
        Mutateur de la masse à dissoudre
    """
    self._massToDissolve = value
    self.checkMissing()
#endregion Properties
    

    

