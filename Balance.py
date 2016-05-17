#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Classe gérant l'equilibrage d'équation
"""

#Disclaimer : Pour tester, utiliser l'equation de combustion du méthane
#dans le dioxygene :
#CH4 + O2 -> CO2 + H2O
class Balance:
    def __init__(self):
        self.p_coef = dict()
        self.r_coef = dict()
        self.rOne_p = dict()
        self.rTwo_p = dict()
        self.pOne_p = dict()
        self.pTwo_p = dict()
        
    def balanceEquation(self, rOne, rTwo, pOne, pTwo):
        """
            Equilibre une equation en calculant les différents 
            coefficients stoechiométriques.
            
            :param rOne: Premier reactif de l'équation
            :param rTwo: Second reactif de l'équation
            :param pOne: Premier produit de l'équation
            :param pTwo: Second produit de l'équation
            :type rOne: ChemicalElement
            :type rTwo: ChemicalElement
            :type pOne: ChemicalElement
            :type pTwo: ChemicalElement
            :return: Les coefficients stoechiometriques de chaque element
            :rtype: int[3]
        """
        self.parseAtoms(rOne, rTwo, pOne, pTwo)
        
        #todo Manon
        
    def parseAtoms(self, rOne, rTwo, pOne, pTwo):
        """
            Analyse une equation pour recuperer le nombre d'atomes
            de chaque côté de l'équation
            
            :param rOne: Premier reactif de l'équation
            :param rTwo: Second reactif de l'équation
            :param pOne: Premier produit de l'équation
            :param pTwo: Second produit de l'équation
            :type rOne: ChemicalElement
            :type rTwo: ChemicalElement
            :type pOne: ChemicalElement
            :type pTwo: ChemicalElement
            :return: - (les resultats sont sauvegardés dans l'instance de classe)
            :rtype: void
        """
        self.rOne_p = self.parseEntry(rOne)
        self.rTwo_p = self.parseEntry(rTwo)
        self.pOne_p = self.parseEntry(pOne)
        self.pTwo_p = self.parseEntry(pTwo)
        self.r_coef = dict(rOne_p.items() + rTwo_p.items() + \
    [(k, rOne_p[k] + rTwo_p[k]) for k in set(rTwo_p) & set(rOne_p)])
        print self.r_coef
        self.p_coef = dict(pOne_p.items() + pTwo_p.items() + \
    [(k, pOne_p[k] + pTwo_p[k]) for k in set(pTwo_p) & set(pOne_p)])
        print self.p_coef
        
        
    def parseEntry(self, entry):
        """
            Filtre une entrée et retourne 
            
            :param entry: Molecule
            :type entry: string
            :return: Le nombre de chaque atome
            :rtype: dictionary<string, int>
        """
        result = dict()
        element = ""
        value = ""
        for char in entry:
            if str.isdigit(char):
                value += char
                if len(element) > 1:
                    result[element[0]] = 1
                    result[element[1]] = value
                else:
                    result[element] = value
                element = ""
                value = ""
            else:
                element += char
                
        return result
        
"""
todo:
enregistrer chaque molecule comme structure

Molecule A 
 {
   1 C
   4 H
   reactif=true
 }

Molecule B 
 {
   2 O
   reactif=true
 }

Molecule C 
 {
   1 C
   2 O
   reactif=false
 }

Molecule D
 {
   2 H
   1 O
   reactif=false
 }
pour toutes.
verifier equilibre
resoudre le systeme:
 { a*Molecule A.C = c*Molecule C.C
 { a*Molecule A.H = d*Molecule D.H
 { b*Molecule B.O = c*Molecule C.O + d*Molecule D.D

toString(a + MoleculeA + b + MoleculeB + c + MoleculeC + d + MoleculeD)
"""
