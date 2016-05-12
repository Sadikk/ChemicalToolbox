#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Classe gérant l'equilibrage d'équation
"""


class Balance:
    def __init__(self):
        self.p_coef = dict()
        self.r_coef = dict()
        
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
        rOne_p = self.parseEntry(rOne)
        rTwo_p = self.parseEntry(rTwo)
        pOne_p = self.parseEntry(pOne)
        pTwo_p = self.parseEntry(pTwo)
        self.r_coef = dict(rOne_p.items() + rTwo_p.items() +
    [(k, rOne_p[k] + rTwo_p[k]) for k in set(rTwo_p) & set(rOne_p)])
		self.p_coef = dict(pOne_p.items() + pTwo_p.items() +
    [(k, pOne_p[k] + pTwo_p[k]) for k in set(pTwo_p) & set(pOne_p)])
        
    def parseEntry(self, entry):
		"""
			Filtre une entrée et retourne un Dictionary atome/coefficient stochiometrique
		"""
		result = dict()
		element = ""
		value = ""
		for char in entry:
			if str.isdigit(char):
				value += char
				result[element] = value
				element = ""
				value = ""
			else:
				element += char
				
		return (element, int(value))
        
