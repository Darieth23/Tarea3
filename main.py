#Estudiante: Darieth Fonseca Zuniga, Carne: B62738.
#Tarea 1, Modelos probabilisticos de senales y sistemas.
import numpy as np 
import scipy
from scipy import stats 
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm,rayleigh
from pylab import plot,show,hist,title
from scipy.optimize import curve_fit
from mpl_toolkits.mplot3d import Axes3D

#Lectura de datos
datos = pd.read_csv('xy.csv')
#matriz de datos
matriz = datos.to_numpy()
matriz = np.delete(matriz,0,axis=1)

#Funcion gaussiana
def gaussiana(x, mu,sigma):
  return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(x - mu)**2/(2*sigma**2))

#Punto 1. 
#funcion de densidad marginal de x
fx = np.sum(matriz, axis=1)
ejex_mod = np.linspace(5,15,11)
#Marginal X
#se ajusta a una gaussiana
param, _ = curve_fit(gaussiana,ejex_mod,fx)
x= np.linspace(5,15,200)
curva = stats.norm.pdf(x, param[0], param[1])
#funcion de densidad marginal de y
fy = np.sum(matriz, axis=0)
ejey_mod = np.linspace(5,25,21)
#Marginal Y
#se ajusta a una gaussiana
paramy, _ = curve_fit(gaussiana,ejey_mod,fy)
y= np.linspace(5,25,200)
curvay = stats.norm.pdf(y,paramy[0],paramy[1])

#Punto 2.
print("Parámetros importantes del punto 2.") 
print("Lo parámetros de fx(x) son: \nmu = ",param[0], "\nsigma = ",param[1])
print("Lo parámetros de fy(y) son: \nmu = ",paramy[0], "\nsigma = ",paramy[1])

#Punto 3.
#Correlación
filas = len(ejex_mod)
columnas = len(ejey_mod)
correlacion = 0
i = 0
j = 0
while(i < filas):
  while(j < columnas):
    correlacion = correlacion + ejey_mod[j]*ejex_mod[i]*matriz[i][j]
    j+=1
  i+=1
  j=0
print("\n\nValores obtenidos para el punto 3.")
print("La correlación Rxy es igual a ",correlacion)
#Covarianza
covarianza = 0
i = 0
j = 0
mediax = np.median(ejex_mod)
mediay = np.median(ejey_mod)
while(i < filas):
  while(j < columnas):
    covarianza = covarianza + (ejey_mod[j]-mediay)*(ejex_mod[i]-mediax)*matriz[i][j]
    j+=1
  i+=1
  j=0
print("La covarianza Cxy es igual a ", covarianza)
#Coeficiente de correlación
coef_cor = covarianza/(paramy[1]*param[1])
print("El coeficiente de correlación es igual a ", coef_cor)

#Punto 4.
#Grafica X
plot(x, curva, color = 'b')
title('Curva de ajuste de la función marginal de X.')
plt.xlabel('valor de x')
plt.ylabel('valor de fx(x)')
plt.savefig('Ajustex')
plt.cla()
#Gráfica Y
plot(y, curvay, color = 'b')
title('Curva de ajuste de la función marginal de Y.')
plt.xlabel('valor de y')
plt.ylabel('valor de fy(y)')
plt.savefig('Ajustey')
plt.cla()
#Datos escritos a mano
matriz2 = vvz=np.array([0.00262, 0.00177, 0.00325, 0.00353, 0.003, 0.00365, 0.00544, 0.00466, 0.00381,0.00445, 0.00122, 0.0049, 0.0022, 0.00359, 0.00304, 0.00212, 0.00355, 0.00247,0.00337, 0.00184, 0.00266, 0.00493, 0.00307, 0.00216, 0.00186, 0.00448, 0.00356, 0.0037, 0.00376,0.00381, 0.00318, 0.00201,0.00337, 0.00301, 0.00435, 0.00369, 0.00266, 0.00396, 0.00394, 0.00495, 0.0014, 0.00387, 0.00283,0.00333, 0.00369, 0.00387, 0.00396, 0.00275, 0.00569, 0.00223, 0.00364, 0.00362, 0.0041, 0.00441, 0.00644, 0.00316, 0.00389, 0.00328, 0.00244,0.00526, 0.00488, 0.00387, 0.00593, 0.00288, 0.00143, 0.00456, 0.00205, 0.00273, 0.00357,0.00175, 0.00551, 0.00627, 0.01, 0.00796, 0.00881, 0.0065, 0.00431, 0.00486, 0.00457,0.00339, 0.00276, 0.00339, 0.00305, 0.00195, 0.00466, 0.00404, 0.00313, 0.00318, 0.00195, 0.0043, 0.00437, 0.00666, 0.0103, 0.01257, 0.01372, 0.01399, 0.00934, 0.00784, 0.00416, 0.00298, 0.00292, 0.00323, 0.0032, 0.00334,0.00238, 0.00277, 0.00293, 0.00373, 0.00315, 0.00509, 0.00259, 0.00512, 0.00727, 0.01273, 0.01635, 0.0176, 0.015, 0.01172, 0.00766, 0.00644, 0.00498, 0.00359, 0.00396, 0.00411,0.00149,0.00321, 0.00425, 0.00405, 0.00389, 0.00315, 0.00198, 0.00418, 0.00526, 0.00645, 0.00944, 0.0125, 0.01554, 0.01179, 0.00905, 0.00792, 0.00482, 0.00462, 0.00296, 0.00112, 0.00238, 0.00271, 0.00366, 0.0023, 0.00294, 0.00217, 0.00533, 0.00328, 0.00532, 0.00596, 0.00453, 0.00395, 0.00736, 0.00752, 0.00873, 0.00635, 0.00634, 0.00205, 0.00363, 0.00528, 0.00367, 0.00467, 0.00356, 0.0034, 0.00361, 0.00461, 0.0, 0.00333, 0.00158, 0.00517, 0.00364, 0.00267, 0.00303, 0.00543, 0.00341, 0.00585, 0.0043, 0.00318, 0.00488, 0.00426, 0.00255, 0.004, 0.00351, 0.00388, 0.00397, 0.00277, 0.00257, 0.00327, 0.00428, 0.00498, 0.00214, 0.00292, 0.00218, 0.00302, 0.00436, 0.00276, 0.00121, 0.0035, 0.00121, 0.004, 0.00265, 0.00234, 0.00145, 0.00358, 0.0019, 0.00268, 0.00336, 0.0029, 0.0012, 0.00108, 0.00243, 0.00227, 0.00562, 0.00247, 0.00363, 0.00437, 0.00272, 0.00387, 0.00385, 0.00388, 0.00257, 0.00406, 0.00393, 0.00244, 0.00333, 0.00235])
X=np.array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9,9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14,14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15])
Y=np.array([5, 6, 7,8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 5, 6, 7, 8,9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21, 22, 23, 24, 25, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 5,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,17,18, 19, 20, 21, 22, 23, 24, 25, 5,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 5,6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 5, 6, 7,8,9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 5, 6,7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
#Grafica XY
figura = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(X,Y,matriz2,'b')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('fx,y(x,y)')
plt.savefig('Grafica3D')
plt.cla()