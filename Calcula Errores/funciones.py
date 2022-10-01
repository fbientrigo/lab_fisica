import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import convenios

print("funciones para labs, usa help() para averiguar mas o funciones.help()")

def main():
    """
    
    """
    pass

def help():
    print("""
    import funciones as fn
    > XX = fn.simbolos("x,y,z")
    or >> x, y, z = XX
    > mediciones = #mediciones para cada variable
    > expresionn = F(XX[0], XX[1]) #crear funcion
    or >> expresion = F(x,y,z)

    #camino explicito
    > dels = fn.derivada(expresion, variables)
    > substitucion = sub_lista(variables, mediciones) #[(x,1),..]
    > delsx0 =  subrule(expresion, substitucion)


    # camino modulado
    > delsx0 = derivada_en_xo(expresion, variables, mediciones)

    # luego utilizamos el convenio
    > convenio.ejemplo(delsx0, errores)
    """
    )


def simbolos(symb, debug = False):
    """
    "x,y,z,t", crea las variables simbolicas, es importante que nos de 
    una lista o arreglo con estas variables, de manera que sea expandible

    utiliza exec de manera global
    """
    lista_string = symb.split(",")
    simb_espacio = ' '.join( lista_string )

    codigo = symb + "=" + "symbols(\"" + simb_espacio + "\")"
    if debug:
        print("El siguiente codigo:")
        print(codigo)
        print("sera ejecutado")
    #el equivalente a:
    # x,y,z = symbols("x y z")
    # se corre de manera global para que esta definicion llegue a main.py
    # y no se quede dentro de la funcion
    exec(codigo, globals(), globals())
    if debug:
        print("codigo y variables exitosos")
        print("se procede a crear lista")

    #extraer una lista con las variables en caso necesario
    exec("lista = " + "[" + symb + "]", globals(),globals() )
    #debo de agregar que el hechon de extraer las variables symbolicas, permite extraerlas
    return lista

def derivadas(expresion, variables):
    """
    toma la funcion, y los simbolos
    nos entrega una lista o arreglo con las derivadas simbolicas
    """
    if type(variables)==list:
        return list(  map( lambda x: diff(expresion, x), variables )   )
    else :
        return diff(expresion, variables)

def sub_lista( XX, XX0 ):
    """
    Lista de  Subs
    el formato es
    [(x,x0),(y,y0),...]
    """
    return list(zip(XX, XX0))


def subrule( expresion , substitucion ):
    """
    sustituye todos los simbolos en nuestras derivadas simbolicas
    por mediciones
    esta necesitara acceso a la derivada (funciones), y valor del simbolo (lista simbolos) o (variables)
    
    # >> x = symbols('x')
    # >> expr = x + 1
    # >> expr.subs(x,2) 
    # 3
    """
    return [exp.subs(substitucion) for exp in expresion]


def derivada_en_xo(expresion, variables, mediciones):
    """
    variables = [x, B, t]
    mediciones = [1, 3, 5] #1cm 3 Webers y 5 segundos
    x,t,B = 
    expresion =  ( x / t ) * B


    dFdxi_en_punto_x0 = derivada_en_xo(expresion, variables, mediciones)
    error = convenio.ejemplo(dFdxi) #este sera el error calculado
    """
    dels = derivadas(expresion, variables)
    substitucion = sub_lista(variables, mediciones) #[(x,1),..]
    return subrule(dels, substitucion)

    


if __name__ == '__main__':
    init_printing(use_unicode = True) #al imprimir, imprimira LaTex
    main()
