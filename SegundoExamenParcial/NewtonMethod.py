from sympy import *
import math
import numpy as np
import matplotlib.pyplot as plt

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

class Jacobian:
    
    def generateJacobianMat(self, X, F, n):    
        #Generar una matriz jacobiana
        J = list()
        for i in range(n):
            tmp = list()
            for j in range(n):
                tmp.append(diff(F[i], X[j]))
            J.append(tmp)
        return J
            
    def generateHessianMat(self, M, X, F):
        H = self.generateJacobianMat(M, X, F)
        H = self.generateJacobianMat(H, X, F)
        return H

class NewtonSENL():
        
    def symbolsVector(self, n, symb):
        X = list()
        for i in range(n):
            X.append(symbols(symb + str(i+1)))
        self.Xsymb = X
        return X
    
    def variableAssignation(self, X0, n):
        # Crear dictionario para asignar valor a variables
        Xsymb = self.Xsymb
        
        varAssign = dict()
        for i in range(n):
            varAssign[Xsymb[i]] = X0[i]
        return varAssign
                    
    def evaluateF(self, F, X0, n):
        F1 = np.ndarray(n)
        VA = self.variableAssignation(X0, n)
        
        #Evaluar funciones        
        for i in range(n):
            F1[i] = F[i].subs(VA)
        return F1
    
    def evaluateJ(self, J, X0, n):
        JNum = np.zeros((n, n))
        VA = self.variableAssignation(X0, n)
        
        for i in range(n):
            for j in range(n):
                JNum[i][j] = (J[i][j].subs(VA))
        return JNum
    
    def calculateY(self, F, J, n):
        #Crear matriz aumentada
        AM = np.concatenate((J, F.T * -1), axis = 1)
        
        #Resolver y por Gauss Jordan
        GJ = GaussJordan()
        y = GJ.doGaussJordan(AM, n)
        Y = list()
        for i in range(n):
            Y.append(y[i][-1])
        
        return Y
    
    def getError(self, X1, X0, n):
        suma = 0
        for i in range(n):
            suma += (X1[i] - X0[i])**2 
            
        return sqrt(suma)
                              
    def runNewtonMethod(self, tol, maxIter, X0, symb, F):
        # Error y numero de iteración
        error = np.inf
        currIter = 0
        self.symbolsVector(n, symb)
                              
        #Generar matriz jacobiana                      
        jac = Jacobian()
        J = jac.generateJacobianMat(self.Xsymb, F, n)                      

        while(error > tol and currIter < maxIter):
            Fi = np.array([self.evaluateF(F, X0, n)])
            Ji = self.evaluateJ(J, X0, n)
            yi = self.calculateY(Fi, Ji, n)    
            X1 = X0 + yi
            error = self.getError(X1, X0, n) 
            X0 = X1 
            currIter += 1
        print("\n Error: ", error)
        # Vector de resultados
        return X0 
        

#Definición de variables
n = 3
tol = float(input("Tolerancia: "))
maxIter = float(input("Número máximo de iteraciones: "))

#Definicion de objetos
newton = NewtonSENL()

#Definicion de sistema de ecuaciones
symb = 'x'
Xsymb = newton.symbolsVector(n, symb)

F = list()
F.append(33/3*Xsymb[0] - sin(Xsymb[1]*Xsymb[2]) -0.7)
F.append(52/5*Xsymb[0]**4 - 81*(Xsymb[1] + 0.1)**2 + sin(Xsymb[2]) + 1.06)
F.append(np.e**(-Xsymb[0]**2*Xsymb[1]) + 3* Xsymb[1]**2 + 43/3*Xsymb[2] - ((10 * np.pi) -3) /3)

# Definición del vector inicial
X0 = np.ndarray(n)
X0[0] = 0.1
X0[1] = 0.1
X0[2] = -0.1

X = newton.runNewtonMethod(tol, maxIter, X0, symb, F)

print("Resultados:\n x = ", X[0], "\n y = ", X[1], "\n z = ", X[2])

