#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

class BalanceView(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
         
        Label(self, text="reactif 1: ").grid(row = 0, column = 0)
        self.R1= StringVar()
        Entry(self,texvariable=self.R1).grid(row = 0, column = 1)
        
        Label(self, text="reactif 2: ").grid(row = 1, column = 0)
        self.R2= StringVar()
        Entry(self,texvariable=self.R2).grid(row = 1, column = 1)
        
        Label(self, text="produit 1: ").grid(row = 2, column = 0)
        self.P1= StringVar()
        Entry(self,texvariable=self.P1).grid(row = 2, column = 1)
        
        Label(self, text="produit 2: ").grid(row = 3, column = 0)
        self.P2= StringVar()
        Entry(self,texvariable=self.P2).grid(row = 3, column = 1)
        

