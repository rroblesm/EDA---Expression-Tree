# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:10:35 2021

@author: R
"""

from Pila import Pila
from Node import Node

class ArbolDeExpresiones:
    def __init__(self, listaDeTokens):
        self.raiz = self.construccionDeArbol(listaDeTokens)
        self.expresion_infija = None
        self.expresion_postfija = None
        self.valor_de_expresion = None
       
    def construccionDeArbol(self, listaDeTokens):
        self.PilaA = Pila()
        self.PilaB = Pila()
        
        for x in listaDeTokens:
            if (x.isdecimal() or x.__contains__(".") or x.__contains__("n")):##puedo hacer algo asi de burdo porque ya cheque el la clase Tokenizadora la validez de la expresion                
                if(x.__contains__("n")):
                    x = x.replace("n", "-")
                nuevoArbol = Node(x)
                self.PilaB.push(nuevoArbol)
            
            if x == "(":
                self.PilaA.push(x)
            
            if x == ")":
                tokenEliminado = self.PilaA.pop()
                while (tokenEliminado != "("):
                    P = self.PilaB.pop()
                    S = self.PilaB.pop()
                    
                    nuevoArbolDeExpresion = Node(tokenEliminado)
                    nuevoArbolDeExpresion.derecho = P
                    nuevoArbolDeExpresion.izquierdo = S
                    
                    self.PilaB.push(nuevoArbolDeExpresion)
                    
                    tokenEliminado = self.PilaA.pop()
                
            if x=="+" or x=="-"  or x=="*" or x=="/":
                interruptor_de_prioridad = False
                prioridad = False
                tope_de_pila = self.PilaA.peek()
                if (x == "*" or x == "/"):
                    prioridad = True
                    if(tope_de_pila == "+" or tope_de_pila == "-"):
                        interruptor_de_prioridad = True

                    
                while (self.PilaA.peek() != "(" ) and (not self.PilaA.isEmpty()) and (interruptor_de_prioridad == False):
                    #usando PilaA.peek y no tope_de_pila me aseguro que no creare un arbol de expresiones con raiz "("
                    tope_de_pila = self.PilaA.pop()
                    P = self.PilaB.pop()
                    S = self.PilaB.pop()
                    
                    nuevoArbolDeExpresion = Node(tope_de_pila)
                    nuevoArbolDeExpresion.derecho = P
                    nuevoArbolDeExpresion.izquierdo = S
                    
                    self.PilaB.push(nuevoArbolDeExpresion)
                    
                    if prioridad == True:
                        if(tope_de_pila == "+" or tope_de_pila == "-"):
                            interruptor_de_prioridad = True
                            
                self.PilaA.push(x)
        
        while (not self.PilaA.isEmpty()):
            operador = self.PilaA.pop()
            P = self.PilaB.pop()
            S = self.PilaB.pop()
            nuevoArbolDeExpresion = Node(operador)
            nuevoArbolDeExpresion.derecho = P
            nuevoArbolDeExpresion.izquierdo = S
            self.PilaB.push(nuevoArbolDeExpresion)
                    
        return self.PilaB.peek()

    def get_raiz(self):
        return self.raiz

    def impresion_inorder(self):
        if self.raiz is not None:
            self.inorder(self.raiz)
            
    def inorder(self, nodo):
        if self.nodo is not None:
            self.inorder(nodo.izquierdo)
            print (nodo.dato)
            self.inorder(nodo.derecho)
    
    def evaluacion(self):
        respuesta = self.evaluacion_de_arbol(self.raiz)
        if respuesta - int(respuesta)==0.0:
            respuesta = int(respuesta)
        
        return respuesta

        
    def evaluacion_de_arbol(self, nodo):
        # empty tree
        if nodo is None:
            return 0
      
        # leaf node
        if nodo.izquierdo is None and nodo.derecho is None:
            return float(nodo.dato)
      
        # evaluate left tree
        valor_izquierda = self.evaluacion_de_arbol(nodo.izquierdo)
      
        # evaluate right tree
        valor_derecha = self.evaluacion_de_arbol(nodo.derecho)
      
        # check which operation to apply
        if nodo.dato == '+':
            return valor_izquierda + valor_derecha
      
        elif nodo.dato == '-':
            return valor_izquierda - valor_derecha
      
        elif nodo.dato == '*':
            return valor_izquierda * valor_derecha
      
        else:
            if(valor_derecha == 0):
                Exception("No se puede dividir entre 0")
            else:
                return valor_izquierda / valor_derecha        
                