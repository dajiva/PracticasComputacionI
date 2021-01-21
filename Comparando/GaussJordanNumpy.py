import numpy as np
import math
import time

num = int(input("Número de ecuaciones: ")) 
print("\n")

def LlenarMatriz(n):
    matriz = np.zeros((n,n+1))
    for i in range(n):
        for j in range(n+1):
            matriz[i][j]=float(input(f"Valor elemento [{i}][{j}]: "))
    return matriz

def GaussJordan(matriz,n):
    #Gauss
    p = 0
    for x in range(n-1):
        renglon = 1
        while matriz[x][x] == 0:
            if renglon == n:
                return math.nan
            IntercambiarRenglones(matriz, x,renglon)
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


def IntercambiarRenglones(matriz,x,r):
    var = len(matriz)
    temp = matriz[x]
    
    matriz[x]= matriz[x+r]
    matriz[x+r] = temp
        
def ImprimirSolucion(sol):
    print("Solución:")
    var = len(sol)
    for i in range(var):
        s = float(sol[i][-1])
        noSol = math.isnan(s) or math.isinf(s)
        if noSol:
            print("El sistema no tiene solucion o tiene infinitas soluciones")
        else:
            print(f"x{i} = {s}")

miMatriz = LlenarMatriz(num)

start = time.time()
GaussJordan(miMatriz, num)
print("\n")
ImprimirSolucion(miMatriz)
end = time.time()
print("Running time: ")
print((end - start)*1000000)