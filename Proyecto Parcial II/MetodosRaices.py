import numpy as np
from sympy.abc import x, y
from sympy import diff
from time import time
import math
import matplotlib.pyplot as plt

   
class RootsMethods:
    
    def IncrementalSearch(self, a, b, tol, func):
        X = np.arange(a, b, tol)
        Y = np.zeros_like(X)
        root = np.inf
        for i in range(len(X)):
            if round(func.subs(x, X[i]), 2) == 0:
                root = X[i]
                
        return root
    
    def bisectionMethod(self, a, b, tol, maxIter, func):
        
        if(func.subs(x, a) * func.subs(x, b)) > 0:
            print("No es posible hallar raíces reales en el intervalo")
            return 
            
        root = np.inf
        error = np.inf
        iter = 0
        
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
       
        return root
    
    def NewtonRaphson(self, tol, maxIter, x0, func):
        der = diff(func, x)

        error = np.inf
        iter =0
        
        while error > tol and iter < maxIter:
            if der.subs(x,x0) == 0:
                print("No es posible hallar raíces reales")
                return 
            
            xp = x0
            x0 = float(xp - (func.subs(x, xp)/ der.subs(x,xp)))
            iter += 1
            
            if x0 != 0:
                error = abs((x0-xp)/x0)*100
            else:
                error = abs(x0-xp)
                
        if error > tol:
            root = x0
        else:
            root = xp
       
        return root
            
    def secantMethod(self, tol, maxIter, x_1, x0, func):
        
        error = np.inf
        iter = 0
        
        while error > tol and iter < maxIter:
            
            fx0 = func.subs(x, x0)
            x1 = float(x0 - (fx0 * (x0 - x_1)) / (fx0 - func.subs(x, x_1)))
            error = abs(x1 - x0)
            
            x_1 = x0
            x0 = x1
            iter += 1
            
        root = x0
            
        return root
        
        
    def brentDekkerMethod(self, a, b, tol, func):
        fa = func.subs(x, a)
        fb = func.subs(x, b)
        
        if fa*fb >= 0:
            print("No es posible hallar raíces reales en el intervalo")
            return False
        
        if abs(fa) < abs(fb):
            a, b = b,a
            fa, fb = fb, fa
        
        c = a
        fc = fa
        
        d = np.inf
        flag = True
        
        while True:
            
            if fa != fc and fb != fc:
                # Interpolación cuadrática inversa
                s1 = (a* fb * fc) / ((fa - fb) * (fa - fc))
                s2 = (b* fa * fc) / ((fb - fa) * (fb - fc))
                s3 = (c* fb * fa) / ((fc - fb) * (fc - fa))
                s = s1 + s2 + s3
            else:
                #Método de la secante
                s = b - fb * (b-a) / (fb - fa)
            
            c1 = s < (3*a + b)/4 or s > b
            c2 = flag == True and abs(s-b) >= abs(b-c)/2
            c3 = flag == False and abs(s-b) >= abs(c-d)/2
            c4 = flag == True and abs(b-c) < abs(tol)
            c5 = flag == False and abs(c-d) < abs(tol)
            
            if c1 or c2 or c3 or c4 or c5:
                # Método de la bisección
                s = (a+b)/2
                flag = True
            else:
                flag = False
            
            d = c
            c = b
            
            if fa*func.subs(x, s) < 0:
                b = s
            else:
                a = s
            
            if abs(fa) < abs(fb):
                a,b = b,a
                fa, fb = fb, fa
            
            # Terminar
            if abs(b-a) < tol or fb == 0:
                return b
            elif func.subs(x, s) == 0:
                return s
