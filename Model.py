#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Modele du pattern MVC - Manipule les données
"""
from DatabaseManager import DatabaseManager

class Model(self):
	instance = None
	
	def __init__(self):
		Model.instance = self
		
	def getElements(self):
		return DatabaseManager.fetchElements()
		
