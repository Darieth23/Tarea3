# Tarea3
Tarea 3, curso modelos probabilísticos de señales y sistemas.
Estudiante: Darieth Fonseca Zuñiga
Carné: B62738

Se procede a explicar el camino seguido para obtener los resultados presentes en las figuras y en los prints del programa main.py.
Punto 1:
Primeramente se procedió a buscar una curva que representará los valores obtenidos para cada una de las funciones de densidad marginal, sin embargo, no se tenia un gráfico continuno, por lo que se procedió a calcular los parámetros, en este caso, de un modelo gaussiano, para ambas variables, y de esta forma se procede a encontrar la curva de mejor ajuste, generada en el punto 4. Los parámetros se pueden ver al correr el programa main.py

Punto 2:
Se obtuvo que la curva de mejor ajuste es gaussiana, por lo que se procedió a encontrar los parámetros que se imprimen en pantalla. En la figura formula.png se puede ver la forma de esta ecuación de densidad probabilística, cabe mencionar que si se usa esta ecuación, junto a la curva de ajuste se puede encontrar una mejor figura en 3D, como se muestra en el punto 4, sin embargo, no se logró conseguir realizar esta tarea, sin embargo, es completamente posible.

Punto 3:
Covarianza: indica cuantro varían conjuntamente dos variables aleatorias respecto al valor de sus medias.
Correlación: este valor se encarga de indicar si dos variables aleatorias, en este caso, se encuentra relacionadas entre sí.
Coeficiente de correlación:
Cabe mencionar que el valor de estas variables se pueden observar al correr el programa.

Punto 4:
a) Para generar las ecuaciones 2D, se usaron las curvas de los modelos aproximados mediante una ecuación Gaussiana, esto con los valores de los parámetros encontrados, tanto para X, como para Y.

b) Se generó con los vectores X[5:15], como para Y[5:25], con pasos de 1 entre cada valor, además de la probabilidad adjuntada para cada punto de (x,y),sin embargo, esta no es la mejor aproximación, se debió haber usado idealmente el modelo de fx,y(x,y) mostrado en el punto 2, para encontrar P(x,y), además de que los vectores X, Y, con más valores entre el intervalo, es decir, dando pasos más pequeños. Se adjunta también el resultado de esta gafica, se puede observar los puntos más altos, confirmando lo esperado tabularmente.
