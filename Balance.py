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
        self.A = dict()
        self.B = dict()
        self.C = dict()
        self.D = dict()
        self.coeffA = 1
        self.coeffB = 1
        self.coeffC = 1
        self.coeffD = 1
        self.LIMIT = 20
        
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
        print "balance equation"
        return self.parseCoef(rOne, rTwo, pOne, pTwo)
        
    def parseCoef(self, rOne, rTwo, pOne, pTwo):
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
        self.A = self.parseEntry(rOne)
        self.B = self.parseEntry(rTwo)
        self.C = self.parseEntry(pOne)
        self.D = self.parseEntry(pTwo)
        
        print "A =>"
        print self.A
        print "B =>"
        print self.B
        print "C =>"
        print self.C
        print "D =>"
        print self.D

        # BruteForce : Tq l'equation n'est pas equilibre, on incremente les coeffs jusqu'a la limite
        while (not(self.isEquilibry())) :
            self.upCoeff()

        if (not(self.D)) :
            print str(self.coeffA) + str(rOne) + "+" + str(self.coeffB) + str(rTwo) + "="  + str(self.coeffC) + str(pOne) 
        else :
            print str(self.coeffA) + str(rOne) + "+" + str(self.coeffB) + str(rTwo) + "="  + str(self.coeffC) + str(pOne) + "+" + str(self.coeffD) + str(pTwo) 


        
        
        result = []
        result.append(self.coeffA)
        result.append(self.coeffB)
        result.append(self.coeffC)
        result.append(self.coeffD)
        
        # Re initialise les coeffs pour la prochaine execution
        self.coeffA = 1
        self.coeffB = 1
        self.coeffC = 1
        self.coeffD = 1
        return result

    def upCoeff(self) :
        if (self.coeffD == self.LIMIT or not(self.D)) :
            self.coeffD = 1
            if (self.coeffC == self.LIMIT) :
                self.coeffC = 1
                if (self.coeffB == self.LIMIT):
                    self.coeffB = 1
                    if (self.coeffA == self.LIMIT):
                        self.coeffA = 1
                    else :
                        self.coeffA += 1
                else :
                    self.coeffB += 1
            else : 
                self.coeffC += 1
            
        else :
            self.coeffD += 1
        
    def isEquilibry(self):
        if (self.equilibreA()) :
            if (self.equilibreB()):
                return True
            
        return False

    def equilibreA(self) :
        numberL = ""
        letterL = ""
        numberR = ""
        letterR = ""
        
        for k, v in self.A.items() :
            numberL = v
            letter = k
            numberL_B = self.getResultForLetter(k, self.B)
            numberR_C = self.getResultForLetter(k, self.C)
            numberR_D = self.getResultForLetter(k, self.D)

            if (numberR_C != -1 and numberR_D != -1) :
                if (numberL_B != -1) :
                    #print str(numberL) + "x" + str(self.coeffA) + "+" + str(numberL_B) + "x" + str(self.coeffB) + "=" + str(numberR_C) + "x" + str(self.coeffC) + "+" + str(numberR_D) + "x" + str(self.coeffD)
                    if (int(numberL) * int(self.coeffA) + int(numberL_B) * int(self.coeffB) != int(numberR_C) * int(self.coeffC) + int(numberR_D) * int(self.coeffD)):
                        return False
                else :
                    #print str(numberL) + "x" + str(self.coeffA) + "=" + str(numberR_C) + "x" + str(self.coeffC) + "+" + str(numberR_D) + "x" + str(self.coeffD)
                    if (int(numberL) * int(self.coeffA) != int(numberR_C) * int(self.coeffC) + int(numberR_D) * int(self.coeffD)):
                        return False
            elif (numberR_C != -1 and numberR_D == -1):                 
                if (numberL_B != -1) :
                    #print str(numberL) + "x" + str(self.coeffA) + "+" + str(numberL_B) + "x" + str(self.coeffB) + "=" + str(numberR_C) + "x" + str(self.coeffC)
                    if (int(numberL_B) * int(self.coeffB) + int(numberL) * int(self.coeffA) != int(numberR_C) * int(self.coeffC)):
                        return False
                else :
                    #print str(numberL) + "x" + str(self.coeffA) + "=" + str(numberR_C) + "x" + str(self.coeffC)
                    if (int(numberL) * int(self.coeffA) != int(numberR_C) * int(self.coeffC)):
                        return False
            elif (numberR_C == -1 and numberR_D != -1):
                if (numberL_B != -1) :
                    #print str(numberL) + "x" + str(self.coeffA) + "+" + str(numberL_B) + "x" + str(self.coeffB) + "=" + str(numberR_D) + "x" + str(self.coeffD)
                    if (int(numberL_B) * int(self.coeffB) + int(numberL) * int(self.coeffA) != int(numberR_D) * int(self.coeffD)):
                        return False
                else :
                    #print str(numberL) + "x" + str(self.coeffA) + "=" + str(numberR_D) + "x" + str(self.coeffD)
                    if (int(numberL) * int(self.coeffA) != int(numberR_D) * int(self.coeffD)):
                        return False

        return True

    def equilibreB(self) :
        numberL = ""
        letterL = ""
        numberR = ""
        letterR = ""
        
        for k, v in self.B.items() :
            numberL = v
            letter = k
            numberL_A = self.getResultForLetter(k, self.A)
            numberR_C = self.getResultForLetter(k, self.C)
            numberR_D = self.getResultForLetter(k, self.D)
            if (numberR_C != -1 and numberR_D != -1) :
                if (numberL_A != -1) :
                    #print str(numberL) + "x" + str(self.coeffB) + "+" + str(numberL_A) + "x" + str(self.coeffA) + "=" + str(numberR_C) + "x" + str(self.coeffC) + "+" + str(numberR_D) + "x" + str(self.coeffD)
                    if (int(numberL) * int(self.coeffB) + int(numberL_A) * int(self.coeffA) != int(numberR_C) * int(self.coeffC) + int(numberR_D) * int(self.coeffD)):
                        return False
                else :
                    #print str(numberL) + "x" + str(self.coeffB) + "=" + str(numberR_C) + "x" + str(self.coeffC) + "+" + str(numberR_D) + "x" + str(self.coeffD)
                    if (int(numberL) * int(self.coeffB) != int(numberR_C) * int(self.coeffC) + int(numberR_D) * int(self.coeffD)):
                        return False
            elif (numberR_C != -1 and numberR_D == -1):                 
                if (numberL_A != -1) :
                    #print str(numberL) + "x" + str(self.coeffB) + "+" + str(numberL_A) + "x" + str(self.coeffA) + "=" + str(numberR_C) + "x" + str(self.coeffC)
                    if (int(numberL_A) * int(self.coeffA) + int(numberL) * int(self.coeffB) != int(numberR_C) * int(self.coeffC)):
                        return False
                else :
                    #print str(numberL) + "x" + str(self.coeffB) + "=" + str(numberR_C) + "x" + str(self.coeffC)
                    if (int(numberL) * int(self.coeffB) != int(numberR_C) * int(self.coeffC)):
                        return False
            elif (numberR_C == -1 and numberR_D != -1):
                if (numberL_A != -1) :
                    #print str(numberL) + "x" + str(self.coeffB) + "+" + str(numberL_A) + "x" + str(self.coeffA) + "=" + str(numberR_D) + "x" + str(self.coeffD)
                    if (int(numberL_A) * int(self.coeffA) + int(numberL) * int(self.coeffB) != int(numberR_D) * int(self.coeffD)):
                        return False
                else :
                    #print str(numberL) + "x" + str(self.coeffB) + "=" + str(numberR_D) + "x" + str(self.coeffD)
                    if (int(numberL) * int(self.coeffB) != int(numberR_D) * int(self.coeffD)):
                        return False

        return True

    def getResultForLetter(self, letter, collec) :
        if letter in collec :
            return collec[letter]
        else :
            return -1
        
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
                if (element != ""):
                    result[element] = value
                element = ""
                value = ""
            else:
                if (element != ""):
                    result[element] = 1
                    element = ""
                element += char

        if (element != ""):
            result[element] = 1
        print result        
        return result
