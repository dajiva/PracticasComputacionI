from sympy import *
from sympy.abc import x
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

class GaussJordan:
    
    def IntercambiarRenglones(self, matriz,x,r):
        var = len(matriz)
        temp = []
        for i in range(var + 1):
            temp.append(matriz[x][i])
        for i in range(var + 1): 
            matriz[x][i] = matriz[x+r][i]
            matriz[x+r][i] = temp[i]

    def doGaussJordan(self, matriz, n):
        #Gauss
        p = 0
        for x in range(n-1):
            renglon = 1
            while matriz[x][x] == 0:
                if renglon == n:
                    return math.nan
                self.IntercambiarRenglones(matriz, x,renglon)
                renglon += 1
            for i in range(x+1, n): 
                p = matriz[i][x]/matriz[x][x]    
                matriz[i][x] = 0
                for j in range(x+1, n+1):
                    matriz[i][j] -= p*matriz[x][j]
        #Jordan
        x = n -1
        while x > 0:
            for i in range(x):
                p = matriz[i][x]/matriz[x][x]
                matriz[i][x] = 0
                matriz[i][-1] -= p*matriz[x][-1]
            x -= 1
        for i in range(n):
            matriz[i][-1] /= matriz[i][i]
            matriz[i][i]= 1
        
        return matriz

class Regresiones:
    
    def MinimosCuadrados(self, X, Y, orden):
        m2 = 2*orden
        if len(X) == len(Y):
            Xcoeff = [0] * m2
            XiY = [0] * (orden +1)
            sumY = 0
            
            for i in range(len(X)):
                sumY += Y[i]
                for j in range(len(Xcoeff)):
                    Xcoeff[j] +=  X[i] ** (j+1)
                    if j < orden + 1:
                        XiY[j] +=  X[i] ** j * Y[i]
                                    
            m = np.zeros((orden+1,orden+2))
            
            for i in range(orden+1):
                m[i][orden+1] = XiY[i]
                for j in range(orden+1):
                    m[i][j] = Xcoeff[i+j-1]
                    
            m[0][0] = len(X)
            self.m = m
            
            gj= GaussJordan()
            results = gj.doGaussJordan(m,orden+1)
            
            f = 0
            for i in reversed(range(orden+1)):
                f += results[i][-1]*x**i
                
            return f
            
        else:
            print("Los vectores no tienen el mismo número de elementos")
            return
        
        
    def squareMeanError(self, X, Y, func):
        meanError = 0
    
        for i in range(len(X)):
            meanError += (Y[i] - func.subs(x, X[i]))**2
        meanError /= len(X)
            
        return meanError
    
    def evaluate(self, X, func):
        y = list()
        for i in range(len(X)):
            y.append(func.subs(x, X[i]))
        return y

# Importar datos
df = pd.read_csv("https://raw.githubusercontent.com/dajiva/PracticasComputacionI/master/Regresion/tech%24overtime.csv")
df = df[df['Entity'] == 'DNA Sequencing' ]  

numDatos = len(df)
df['Idx'] = range(numDatos)
df = df.set_index('Idx') 

X = df['Year'].astype(int)
Y = df['J. Doyne Farmer and François Lafond (2016)'].astype(int)

reg = Regresiones()
orders = [1,2, 4, 6, 8,10]
error = list()
minE = np.inf

# Generar gráfica
'''
fig, ax = plt.subplots()  
ax.scatter(X, Y, label='Datos')  


for o in orders:
    func = reg.MinimosCuadrados(X,Y,o)
    print("Regresion orden ", str(o), ": ", func)
    e = reg.squareMeanError(X, Y, func)
    if e < minE:
        minE = e
        minEord = o
    error.append(e)
    if o < 5:
        y = reg.evaluate(X,func)
        ax.plot(X, y, label= str(o))


ax.set_xlabel('Año')  
ax.set_ylabel('Costo')  
ax.set_title("Regresiones de costo de secuenciación de DNA por año, según orden")  
ax.legend()
'''

print("El grado con el menor error es: ", minEord)

# Grafica error por grado de polinomio
'''
plt.plot(orders, error)
plt.yscale("log")
plt.title("Error según el orden de regresión")
'''

# Generar regresiones con un polinomio de grado 10
A = range(20)
expr = 0
for i in range(11):
    a = random.randint(0,9)
    expr += a *x**i
print(expr)

B = list()
for i in A:
    B.append(expr.subs(x, i))
print(B)
fig, ax = plt.subplots()  
ax.scatter(A,B, label='f(x)')
    
for o in orders:
    func = reg.MinimosCuadrados(A,B,o)
    #rint("Regresion orden ", str(o), ": ", func)
    e = reg.squareMeanError(A, B, func)
    if e < minE:
        minE = e
        minEord = o
    error.append(e)
    y = reg.evaluate(A,func)
    ax.plot(A, y, label= str(o))
        
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title("Regresiones para un polinomio de grado 10")
ax.legend()