import numpy as np
import pylab as pl
#Crea un vector (arreglo) con los valores del eje x
x = [1,2,3,4,5]
#Crea un vector (arreglo) con valores en el eje y para cada valor en el eje x
y = [1,4,9,16,25]
#Grafica el vector x contra el vector y
pl.plot(x,y)
#Guarda la grafica de formato png
pl.savefig('templ.png')
