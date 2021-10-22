# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:16:29 2021

@author: R
"""


class Pila: #Considerando que la lista de python tiene funciones de pila, solo  es restringir esas funciones
    def __init__(self):
        self.lista = []
    
    def __str__(self):
        miCadena = ""
        for x in self.lista:
            miCadena += str(x)
            miCadena += " \n"
        return miCadena
        
    def __repr__(self):
        for x in self.lista:
            print(x)
            
    def isEmpty(self):
        return (not self.lista) or (len(self.lista)==0) 
        
    def push(self, data):
        self.lista.append(data)
        
    def pop(self):
        if (self.isEmpty()==False):
            return self.lista.pop(-1)
        
    def peek(self):
        if (self.isEmpty()==False):
            return self.lista[-1]
        
    def size(self):
        return len(self.lista)
    
    
    def imprime(self):
        for x in self.lista:
            print(x)