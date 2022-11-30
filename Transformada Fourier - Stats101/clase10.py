#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:20:45 2022

@author: dominiosdera
"""

#Interpretación física de la transformada de Fourier

#Descompone función en grupo de ondas sinusoidales reales o complejas

#Cada término de la suma representa una onda con su frecuencia bien definida
#Si f(x) es función del espacio, tendremos 


#Equivalente a decir que cada f(x) puede representarse como la suma de ondas de determinadas frecuencias

#import os
import numpy as np
import matplotlib.pyplot as pl

#os.chdir('home/dominiosdera/')

data=np.loadtxt('pitch.txt',float) #Tienen que estar en la carpeta de compu3

pl.clf()
pl.plot(data)
pl.show()


def dft(y):
    N=len(y)
    c=np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c

c=dft(data)

pl.close('all')
pl.plot(abs(c))
pl.ylabel(r'Abs ($c_k$)') #Para que quede con subíndices
pl.xlabel('Múltiplos de frecuencia')
pl.xlim(0,500)
pl.grid()
pl.show()


#%%

#Ejercicio

import numpy as np
import matplotlib.pyplot as pl

x=np.linspace(0,1000,500)
#x=np.arange(-500,500)
y=np.piecewise(x,[x<500,x>=500], [lambda x: -2, lambda x: 2]) #Define la misma función que el profe pero más fácil xd


def dft(y):
    N=len(y)
    c=np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c

c=dft(y)

pl.clf()
pl.subplot(2,1,1)
pl.plot(x,y,color='blue')
pl.xlabel('x');pl.ylabel('f(x)')
pl.grid()
pl.tight_layout() #Para que no se sobrepongan los gráficos

pl.subplot(2,1,2)
pl.plot(range(len(y)//2+1),abs(c),'-r')
pl.xlabel('k');pl.ylabel('$c_k$')
pl.xlim(0,50)
pl.grid()

#%%

#Ejercicio 7.1

import numpy as np
import matplotlib.pyplot as pl

dx=0.002
L=np.pi
x=L*np.arange(-1+dx,1+dx,dx)
n=x.shape[0]
nquart= int(n/100)


def dft(y):
    N=len(y)
    c=np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c


#Definiendo la función diente de cierra
f=np.zeros_like(x)
for n in range(0,f.shape[0],100):
    f[n:n+100] = np.array(range(100),int)

c= dft(f)

pl.clf()
pl.subplot(2,1,1)
pl.plot(x,f,'-b')

pl.subplot(2,1,2)
pl.plot(range(len(f)//2+1),abs(c),'-r')


#%%

#Usando la función sawtooth

from scipy import signal

x=np.linspace(0,1,1000) #Crear la variable x con mil elementos
y=signal.sawtooth(2*np.pi*7*x) #EL 7 es la cantidad de repeticiones de dientes que tiene la función

c=dft(y)

pl.clf()
pl.subplot(2,1,1)
pl.plot(x,y,'-b')
pl.xlabel('x');pl.ylabel('f(x)')

pl.subplot(2,1,2)
pl.plot(range(len(y)//2+1), abs(c), '-r')
pl.xlabel('k');pl.ylabel('$c_k$')
pl.xlim(0,200)
# %%
