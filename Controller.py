#!/usr/bin/env python
# -*- coding: utf-8 -*-

from DatabaseManager import DatabaseManager
"""
Main file
"""

db = DatabaseManager("db.sql")
print db.fetchElements()
db.close()
#todo
