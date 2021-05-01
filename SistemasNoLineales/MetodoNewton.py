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
        print("Error: ", error)
        # Vector de resultados
        return X0 
        

#Definición de variables
n = 3
tol = 0.1
maxIter = 999999999

#Definicion de objetos
newton = NewtonSENL()

#Definicion de sistema de ecuaciones
symb = 'x'
Xsymb = newton.symbolsVector(n, symb)

F = list()
F.append(3*Xsymb[0] - cos(Xsymb[1]*Xsymb[2]) -1/2)
F.append(Xsymb[0]**2 - 81*(Xsymb[1] + 0.1)**2 + sin(Xsymb[2]) + 1.06)
F.append(np.e**(-Xsymb[0]*Xsymb[1]) + 20* Xsymb[2] + ((10 * np.pi) -3) /3)

# Definición del vector inicial
X0 = np.ndarray(n)
X0[0] = 0.1
X0[1] = 0.1
X0[2] = -0.1



''' Recibir entradas
n = int(input("Número de ecuaciones: "))

def replaceMany(text, dic):
    for i, j in dic.items():
        text = text.replace(j, str(i))
    return text

def generateF(n):
    funcStr = list()
    functions = list()
    variables = list()
    for i in range(n):
        message = "Variable " + str(i) + ": "
        variables.append(input(message))
    for i in range(n):
        message = "Ecuacion " + str(i) + ": "
        func = input(message)
        funcStr.append(replaceMany(func, newton.variableAssignation(variables, n)))
        print(funcStr)
        functions.append(sympify(funcStr))
    return functions
    
'''
    
tol = 0.00001

X = newton.runNewtonMethod(tol, maxIter, X0, symb, F)

print("Resultados:", X)

# Tolerancias y listas de tiempos
tol = [0.1,0.01,0.001,0.0001,0.00001]
logTol = list()
for t in tol:
    logTol.append(math.log(t)* -1)

error = [0.0179944513771168, 0.00157675574918087, 1.24487810839885e-5, 1.24487810839885e-5, 7.76083329827934e-10]
plt.plot(logTol, error)
plt.title('Error de la implementación del método de Newton y tolerancia')
plt.xlabel('Tolerancia (-log)')
plt.ylabel('Error')