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
    self._molarMass = (self._massToDissolve) / (self._concentration * self._volume)
    
def computeVolume(self):
    """
        Calcule le volume
    """
    self._volume = (self._massToDissolve)/(self._concentration * self._molarMass)
    
def computeConcentration(self):
    """
        Calcule la concentration
    """
    self._concentration = (self._massToDissolve) / (self._molarMass * self._volume)
    
def computeMassToDissolve(self):
    """
        Calcule la masse à dissoudre
    """
    self._massToDissolve = self.concentration * self._molarMass * self._volume
    
def checkMissing(self):
    """
        Verifie si chaque valeur a été remplie et calcule la valeur
        manquante si nécessaire
    """
    if self._massToDissolve !=0 and if self._concentration !=0 and if self._volume !=0:
           computeMolarMass(self)
    if self._massToDissolve !=0 and if self._concentration !=0 and if self._molarMass !=0:
            computeVolume(self)
    if self._massToDissolve !=0 and if self._molarMass !=0 and if self._volume !=0:
            computeConcentration(self)
    if self._concentration !=0 and if self._molarMass !=0 and if self._volume !=0:
            computeMassToDissolve(self)
    
    
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
    

    

