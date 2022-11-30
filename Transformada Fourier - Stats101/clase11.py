#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 12:07:50 2022

@author: dominiosdera
"""


#Transformadas discretas de cosenos y senos
#Transformada rápida de Fourier (FFT)

#Hemos visto expresiones complejas para las series de Fourier
#También podemos construir series de Fourier que usen senos y cosenos en vez de exponenciales complejos
#Hay versiones de transformada discreta de fourier para series de senos y cosenos
#Particularmente, la serie de cosenos la usamos a diario

#f(x)= sum desde k=0 hasta infinito (a_k * cos(2*pi*k*x/L))

#NO todas las f(x) pueden representarse de esta forma

#Una vez que se iene función simétrica, la serie de Fourier de cos es sólo el caso especial de ecuación DFT

#c_k= sum desde n=0 hasta N-1 (y_n*exp(-i*2*pi*k*n/N))

#Trabajando con ecuación se llega a:

#c_k = y_0 + y_N/2 * cos(2*pi*k/(N/2)/N) + 2*sum desde n=1 hasta (N/2)-1 (y_n * cos(2*pi*k*n/N))

#También se puede hacer series de seno para la transformana, pero casi no se usa porque se necesita que sea 0 en todos sus puntos.

#Funciona para transfomar imagenes a jpeg o archivos de música a mp3.


#%%

#Calcular los coeficientes de la transformada de FOurier discreta de la onda seno

import numpy as np
import matplotlib.pyplot as pl

#x=np.arange(1000) No funcionó xd
x = np.linspace(0, 1, 500)
N = len(x)

#Definir la función
f=np.zeros_like(x)

for ii in range(N): #AAAAAAAAAAAH Se hacía con otro ciclo for
    f[ii] = np.sin(ii*np.pi/N) * np.sin(20*np.pi*ii/N)


#Se define la transformada
def dft(y):
    N=len(y)
    c=np.zeros(N//2+1,complex)
#    y=np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
#            y[n]=np.sin(np.pi*n/N) * np.sin(20*np.pi*n/N)
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c


c = dft(f)
h = np.abs(c)
m = np.where(h > 0.1, h, h)
print(m)

pl.clf()
pl.subplot(2,1,1)
pl.plot(x,f,color='blue')
pl.xlabel('x');pl.ylabel('f(x)')
pl.grid()
pl.tight_layout() #Para que no se sobrepongan los gráficos

pl.subplot(2,1,2)
pl.plot(range(len(f)//2+1),abs(c),'-r')
pl.xlabel('k');pl.ylabel('$c_k$')
pl.xlim(0,50)
pl.grid()


#%%


#Pregunta 1

import scipy.fft as sc

meses=np.loadtxt('sunspots.txt',int,usecols=0) #Para la primera columna
manchas=np.loadtxt('sunspots.txt',float,usecols=1) #Para la segunda columna
#print(meses)

pl.clf()
pl.subplot(2,1,1)
pl.plot(meses,manchas,color='yellow')
pl.title('Sunspots since 1749',loc='center')
pl.xlabel('Months');pl.ylabel('Sunspots')
pl.grid()
#pl.xlim(0,400) #Ponerle límite porque son caleta de datos, así puedes ver el periodo a ojo aprox
pl.tight_layout()


#Así como a puro ojo, igual son como 10 años el periodo

#Pregunta 2

#from scipy.fft import dct     lo intenté

ck=sc.fft(manchas)
#ck=dft(manchas)

pl.subplot(2,1,2)
pl.plot(range(ck[1:].shape[0]),abs(ck[1:])**2/10**9,'-r')
pl.xlabel('k');pl.ylabel('$c_k^{2} x 10^{-9}$')
pl.xlim(0,100)
pl.grid()
pl.show()


#Para calcular el periodo de verdad xd

pow_s=abs(ck[1:])**2
freq=pow_s.argmax()
nmons=1/freq*len(meses[1:])
years=nmons/12
print('Sunspots number has a period of',years,'years')