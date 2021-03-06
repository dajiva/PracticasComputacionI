import numpy as np
from sympy.abc import x, y
import time
import math

class NumericalMethods:
    
    def bisectionMethod(self, a, b, tol, maxIter, func):
        
        if(func.subs(x, a) * func.subs(x, b)) > 0:
            print("No existen raíces reales en el intervalo")
            return np.nan
            
        root = np.inf
        error = np.inf
        iter = 0
        
        start = time.time()
        while error > tol and iter < maxIter:
            c = (a + b)/2
            prod = func.subs(x, a) * func.subs(x, c)
            error = abs(b-a)
            
            if prod < 0:
                root = a
                b = c
            elif prod == 0:
                root = c
                break
            else:
                root = b
                a = c
            iter += 1
        end = time.time()
        print("Tiempo total transcurrido por el método de la bisección: ", end-start)
            
        return root 
    
    
class NaiveMethods:
    
    def IncrementalSearch(self, a, b, func):
        
        X = np.linspace(a, b, 10000)
        Y = np.zeros_like(X)
        root = np.inf
        start = time.time()
        for i in range(len(X)):
            if func.subs(x, X[i]) == 0:
                root = X[i]
        end = time.time()
        
        print("Tiempo total transcurrido en la búsqueda incremental: ", end-start)
        return root
        

def main():
    
    raiz = 0
    a = -5
    b = 2
    maxIter = 90000
    tol = 0.00000000000000001
    func = 2*x**2 - 3*x - 5
    
    objNM = NumericalMethods()
    objN = NaiveMethods()
    
    raiz1 = objNM.bisectionMethod(a, b, tol, maxIter, func)
    print("La raíz real es: ", float(raiz1))
    
    raiz2 = objN.IncrementalSearch(a, b, func)
    print("La raíz real es: ", float(raiz2))

    
if __name__ == "__main__":
    main() 