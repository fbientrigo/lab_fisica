import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy import *
import convenios

def main():
  symb = "x, y, z"
  XX = simbolos(symb)
  print(z)
  expr = x * y + z
  print(f"antes de subs: {expr}")
  res = expr.subs([ (x,1),(y,2),(z,6) ])
  print(f"despues de subs: {res}")

  print(XX[0])

def simbolos(symb):
  """
  "x y z t", crea las variables simbolicas, es importante que nos de 
  una lista o arreglo con estas variables, de manera que sea expandible

  utiliza exec de manera global, por tanto las definiciones de variables solo funcionan aqui
  en el modulo main
  """
  lista_string = symb.split(",")
  simb_espacio = ' '.join( lista_string )

  codigo = symb + "=" + "symbols(\"" + simb_espacio + "\")"
  #el equivalente a:
  # x,y,z = symbols("x y z")
  # se corre de manera global para que esta definicion llegue a main.py
  # y no se quede dentro de la funcion
  exec(codigo, globals(), globals())
  print("variables creadas con exito")

  #extraer una lista con las variables en caso necesario
  exec("lista = " + "[" + symb + "]", globals(),globals() )
  #debo de agregar que el hechon de extraer las variables symbolicas, permite extraerlas
  return lista

def derivadas(expresion, variables):
  """
  toma la funcion, y los simbolos
  nos entrega una lista o arreglo con las derivadas simbolicas
  """
  return list(  map( lambda x: diff(expr, x), variables )   )


def subrule( funciones, variables, medicion ):
  """
  sustituye todos los simbolos en nuestras derivadas simbolicas
  por mediciones
  esta necesitara acceso a la derivada (funciones), y valor del simbolo (lista simbolos) o (variables)
  """
  # >> x = symbols('x')
  # >> expr = x + 1
  # >> expr.subs(x,2) 
  # 3
  pass



if __name__ == '__main__':
  init_printing(use_unicode = True) #al imprimir, imprimira LaTex
  main()
