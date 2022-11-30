#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 10:17:40 2022

@author: dominiosdera
"""

#Transformada rápida de Fourier (FFT)

#Los paquetes de estas funciones están en numpy t scipy
#fft calcula la transformada de fourier en 1-D usando el algoritmo FFT
#ifft calcula la transformada inversa usando FFT

#rfft cuando se tienen datos que son reales (Entrega sólo la mitad de coeficientes, ya que la otra mitad son complejos conjugados)

#Si los datos son reales y simétricos, podemos aumentar aún más la eficiencia usando la función dct
#dct calcula la serie discreta de cosenos de Fourier

#fft2 calcula la transformada rápida en 2 dimensiones

#(Hay caleta de funciones para las transformadas xd)

#%%

#Ejemplo

import numpy as np
from scipy.fft import fft,rfft,ifft,irfft
#from scipy.fftpack import fft,rfft,ifft
#from numpy.fft import fft,rfft,ifft

x=np.array([1.0,2.0,1.0,-1.0,1.5,1.0])

y1=fft(x);print('Coeficiente de FFT = ',y1)
print()
y2=rfft(x);print('Coeficiente de RFFT = ',y2)
print()
x1=ifft(y1); x2=irfft(y2)
print('Los valores de X= ',x) #rfft no funciona ya que no da los valores complejos
print('Los valores de x1 = ',x1)
print('Los valores de x2 = ',x2) #irfft funciona con rfft

#%%

#Ejemplo

import numpy as np
import matplotlib.pyplot as pl
from scipy.fft import fft,rfft,ifft,irfft,fftfreq

N = 600 #Número de datos
T = 1.0 / 1000.0 #Periodo
x = np.linspace(0.0, N*T, N)
y = np.sin(50 * 2.0 * np.pi * x) + 0.5*np.sin(80 * 2.0 * np.pi * x)

yf = fft(y)
xf = fftfreq(N, T)[:N//2] #Calcula la frecuencia. [:N//2] sólo necesitamos la mitad de datos para plotear

# for n in len(xf):
#     a = np.where(xf[n] == 50)
#     print(a)

pl.clf()
pl.subplot(2, 1, 1)
pl.plot(x, y, '-b')
pl.ylabel('y');pl.xlabel('x')
pl.grid()
pl.tight_layout()

pl.subplot(2, 1, 2)
pl.plot(xf, 2.0/N*np.abs(yf[0:N//2]),'-r')
pl.ylabel('$c_k$');pl.xlabel('f')
pl.xlim(0,200)
pl.grid()
pl.tight_layout()



#%%

#Ejemplo

import numpy as np
import matplotlib.pyplot as pl
from scipy.fft import fft,rfft,ifft,irfft,fftfreq,dct,idct

N=100; t=np.linspace(0,21,N)

x=np.exp(-t/3)*np.cos(2*t)

y=dct(x,norm='ortho') #Normalizarlo de manera que sean ortogonales

#Probar con 10, 15, 20 & 25
#Al profe le dió paja hacer un ciclo así que lo hizo a mano nomás djskldsj

ventana=np.zeros(N)
ventana[:10]=1

yr10=idct(y*ventana,norm='ortho')

#Con 15 elementos
ventana[:15]=1 

yr15=idct(y*ventana,norm='ortho')

#Con 20 elementos
ventana[:20]=1

yr20=idct(y*ventana,norm='ortho')

#Con 25 elementos
ventana[:25]=1

yr25=idct(y*ventana,norm='ortho')


#También le dió paja calcular el error con un ciclo así que igual lo hizo a mano xd

print('ERR con 10 elementos = ',sum(abs(x-yr10)**2/sum(abs(x)**2)*100),'%')
print('ERR con 15 elementos = ',sum(abs(x-yr15)**2/sum(abs(x)**2)*100),'%')
print('ERR con 20 elementos = ',sum(abs(x-yr20)**2/sum(abs(x)**2)*100),'%')
print('ERR con 25 elementos = ',sum(abs(x-yr25)**2/sum(abs(x)**2)*100),'%')

pl.clf()
pl.plot(t,x,'-k')
pl.plot(t,yr10,'-b')
pl.plot(t,yr15,'-g')
pl.plot(t,yr20,'-m')
pl.plot(t,yr25,'-r')

pl.legend(['x','$x_10$','$x_15$','$x_20$','$x_25$'])
pl.xlabel('t');pl.ylabel('x')
pl.grid()