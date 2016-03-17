#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Classe s'occupant de la relation avec la base de données
"""

import sqlit3
import os.path

class DatabaseManager:
	def __init__(self, fname):
		self.filename = fname
		self.connection = sqlit3.connect(self.filename)
		self.cursor = connection.cursor()
		if not os.path.isfile(self.filename):
			self.setup()
		
		
	def setup(self):
		"""
			Installe le fichier de base de données
		"""
		self.cursor.execute("CREATE TABLE elements")
		data = [("Oxygene", 16, 22)]
		for elem in data:
			cursor.execute("INSERT INTO elements VALUES(?,?,?)", elem)
		self.connection.commit()
		
	def close():
		"""
			Ferme la connexion courante
		"""
		self.cursor.close()
		self.connection.close()
		
		

