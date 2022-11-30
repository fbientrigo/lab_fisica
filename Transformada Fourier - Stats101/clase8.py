#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:13:35 2022

@author: dominiosdera
"""

#%%

#Revisión de primera prueba


#Problema 1

#(V_1-V_3)/R_1 = C_1*d(V_0 * V_1)/dt + C_2*d(V_2 - V_1)/dt

#Problema 2 está bueno, creo


#%%



#Transformada de Fourier


#Una función periódoca f(x) en intervalo infinito 0<x<L puede representarse como series
#de Fourier.

#La expresión general para una función que no tiene ningún tipo de simetría es:


#Ejemplo: cómo aproximar una función triangular en series de Fourier

import numpy as np
import matplotlib.pyplot as pl


#Calcular serie de FOurier para función triangular
#Definir dominio
dx=0.001
L=np.pi
x=L*np.arange(-1+dx, 1+dx, dx)
#x = np.pi * np.linspace(-1,1,dx)
n=x.shape[0]
nquart= int(n/4)

#Definir función

f=np.zeros_like(x) #Entrega arreglo de ceros con mismo tamaño y tipo del arreglo elegido
f[nquart:2*nquart] = (4/n)*np.arange(1,nquart+1)
f[2*nquart:3*nquart] = np.ones(nquart) - (4/n)*np.arange(0,nquart)

pl.clf()
pl.subplot(2,1,1)
pl.plot(x,f,'-k')
pl.ylabel('f(x)') ; pl.xlabel('X')
pl.grid()

#Aplicando la serie
A0 = np.sum(f*np.ones_like(x))*dx  # Igual que zeros_like
fFS = A0/2

# Repito el plot de la función
pl.clf()
#plt.subplot(2,1,1)
pl.plot(x, f, '-k')
pl.ylabel('f(x)'); pl.xlabel('X')
pl.grid()

kk = 20

A = np.zeros(kk)
B = np.zeros(kk)
ERR = np.zeros(kk)

for ii in range(kk):
    A[ii] = np.sum(f*np.cos(np.pi*(ii+1)*x/L))*dx  # Inner product
    B[ii] = np.sum(f*np.sin(np.pi*(ii+1)*x/L))*dx
    fFS = fFS + A[ii]*np.cos((ii+1)*np.pi*x/L) + B[ii]*np.sin((ii+1)*np.pi*x/L)
    
    # Plot de cada término de la serie
    pl.plot(x, fFS, '-')

pl.ylabel('f(x) & Fseries'); pl.xlabel('X')

#plt.clf()
#plt.plot(x, f, '-k')
#plt.ylabel('f(x)'); plt.xlabel('X')
#plt.grid()
#
#plt.plot(x, fFS, '-')
#plt.ylabel('f(x) & Fseries'); plt.xlabel('X')


#%%

#ejercicio

import numpy as np
import matplotlib.pyplot as pl

#A0=np.sum(f*np.ones_like(x))*dx

c=np.arange(-np.pi,np.pi,0.1)
g=np.zeros([],float)

for n in range(c.shape[0]):
    cc=c[n]
    if cc<0:
            x=-1
    else:
            x=1
    np.append(g,x)
    print(g)

#dx=0.001
#L=np.pi
#x=L*np.arange(-1+dx, 1+dx, dx)
#n=x.shape[0]
#nquart= int(n/2)

#Definir la fucnión
#f=np.zeros_like

#pl.clf()
#pl.plot(cc,g,color='red')
#pl.show()
    
    
#%%

#Haciendolo bien xd

import numpy as np
import matplotlib.pyplot as pl

x=np.linspace(-np.pi,np.pi)
y=np.piecewise(x,[x<0,x>=0], [lambda x: -1, lambda x: 1])

pl.clf()
pl.plot(x,y)
pl.show()