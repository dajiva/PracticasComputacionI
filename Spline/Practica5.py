import pandas as pd
import numpy as np
from sympy.abc import x
import matplotlib.pyplot as plt

# Datos datahub
df = pd.read_csv("https://raw.githubusercontent.com/dajiva/PracticasComputacionI/master/Interpolacion/population_csv.csv")
df = df[df['Country Name'] == 'Mexico' ] #Seleccionar datos México
dfINEGI = pd.read_csv("https://raw.githubusercontent.com/dajiva/PracticasComputacionI/master/Interpolacion/poblacionMX.csv")
#Limpiar datos
df = df.drop(labels = ['Country Name', 'Country Code'], axis = 1)

#Cambiar índices
numDatos = len(df)
df['Idx'] = range(numDatos)
df = df.set_index('Idx') 
#Agregar dato de año 2020
lastYear = list(dfINEGI.iloc[-1])
df.loc[len(df)] = lastYear

# Generar variables y listas
X = df['Year'].astype(int)
Y = df['Value'].astype(int)
year = 2019

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

class SplineInterpolation():
    
    def SplineInterpolation(self, X, Y, xValue):
        self.createAugmentedMatrix(X,Y)
        self.createFunctions()
        self.defineInterval(X, xValue)
        func = self.functions[self.index]
        return func.subs(x, xValue)

    def createAugmentedMatrix(self, X, Y):
        
        #Definir vector de nodos y resultados
        knots = list()
        results = list()

        # Generación de vector de knots
        for i in range(len(X)):
            if (i == 0 or i == (len(X)-1)):
                knots.append(X[i])
                results.append(Y[i])
            else: 
                knots.append(X[i]) #TODO: verificar inserción doble
                knots.append(X[i])
                results.append(Y[i])
                results.append(Y[i])
        
        # Generación de 3*n ecuaciones
        n = len(X)-1
        self.n = n
        
        # Matriz para almacenar sistema de ecuaciones 3*n x 3*n+1  
        eqs = np.zeros(shape=(3*n,(3*n)+1))
        
        coefIndex = 0
        idx = 0

        #Producir las primeras 2*n ecuaciones 
        for i in range(len(knots)):
            # Knots externos
            if (i == 0 or i == len(knots)):
                # Equations value
                eqs[i][coefIndex] =  knots[i]**2
                eqs[i][coefIndex+1] =  knots[i]
                eqs[i][coefIndex+2] = 1
                #results in the last column
                eqs[i][-1] = results[i]
            # Knots internos
            else:
                eqs[i][coefIndex] =  knots[i]**2
                eqs[i][coefIndex+1] =  knots[i]
                eqs[i][coefIndex+2] = 1
                #results in the last column
                eqs[i][-1] = results[i]
                # incrementar en 3 cada par de elementos
                coefIndex += (i%2) * 3
            
        
            idx = i + 1
            
        kIdx = 1
        j = 0
        # Add n-1 equations
        for i in range(idx, idx + n-1):
            eqs[i][j] = knots[kIdx] *2
            eqs[i][j+1] = 1
            j += 3
            eqs[i][j] = knots[kIdx] * -2
            eqs[i][j+1] = -1
            kIdx += 2
  
        
        # add final equation a1=1
        eqs[3*n-1][0] = 1
    
        self.eqs = eqs
    
    def createFunctions(self):
        n = self.n
        GJ = GaussJordan()
        GJ.doGaussJordan(self.eqs, 3*n)
        
        functions = list()
        idx = 0
        for i in range(n):
            functions.append(self.eqs[i*3][-1] * x**2 + self.eqs[i*3+1][-1] * x + self.eqs[i*3+2][-1])
        self.functions = functions
    
    def defineInterval(self, X, xVal):
        index = 0
        for i in range(len(X)):
            if xVal >= X[i] and xVal <= X[i+1]:
                index = i
                break
            
        self.index = index

        
objS = SplineInterpolation()
print("Población",  X[numDatos-1], ": ", Y[numDatos-1])
print("Población", X[numDatos], ": ", Y[numDatos])
print("Población interpolada para", year, ": ", int(objS.SplineInterpolation(X, Y, year)))