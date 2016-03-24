#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Classe représentant le tableau périodique des élements
"""
from Model import Model

class PeriodicTable:
	def __init__(self):
		self.elements = Model.instance.getElements()
		
		
	
