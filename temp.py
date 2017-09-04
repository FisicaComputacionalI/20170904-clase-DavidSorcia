import numpy as np
import pylab as pl
#Crea un vector (arreglo) con los valores del eje x
x = [1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
#Crea un vector (arreglo) con valores en el eje y para cada valor en el eje x
y = [0,0,0,0,0,1,1,1,2,1,1,1,2,2,2,2,2,2,2,3,3]

pl.title('Novias y mascotas obtenidas a lo largo de la vida', fontsize = 20, color = 'blue')
pl.xlabel('Anios de vida', fontsize = 12, color = 'red')
pl.ylabel('Novias y mascotas', fontsize = 12, color = 'green')

#Grafica el vector x contra el vector y
pl.plot(x,y)
#Guarda la grafica de formato png
pl.savefig('templ.png')
