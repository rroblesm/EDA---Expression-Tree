# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:21:57 2021

@author: R
"""

class Node:
    def __init__(self, data):
        self.dato = data
        self.izquierdo = None
        self.derecho = None

    def __str__(self):
        return self.dato
        
    def __repr__(self):
        print("El dato del nodo es:", self.dato, "\n Su hijo izquierdo", self.izquierdo, "\n Su hijo derecho", self.derecho)