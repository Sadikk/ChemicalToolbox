#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Classe s'occupant de la relation avec la base de données
"""

import sqlite3
import os.path
from ChemicalElement import ChemicalElement

class DatabaseManager:
	def __init__(self, fname):
		self.filename = fname
		self.connection = sqlite3.connect(self.filename)
		self.connection.text_factory = str
		self.cursor = self.connection.cursor()
		
	def fetchElements(self):
		"""
			Récupère tous les éléments chimiques de la base de données
			et les renvoie sous forme d'une liste
		"""
		result = []
		self.cursor.execute('SELECT * FROM elements')
		for row in self.cursor.fetchall():
			result.append(ChemicalElement(row[0], row[1], float(row[2]),\
			 float(row[3]), row[4]))
		return result
		
		
	def close(self):
		"""
			Ferme la connexion courante
		"""
		self.cursor.close()
		self.connection.close()
		
		

