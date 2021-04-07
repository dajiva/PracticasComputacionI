from sympy.abc import x 
from sympy.solvers import solve
import matplotlib.pyplot as plt

# Habilitar impresión avanzada 
init_printing(use_latex='mathjax')

#Método de Newton
def NewtonRaphson(tol, x0, func):
        der = diff(func, x)

        error = np.inf
        iter =0
        
        while error > tol:
            if der.subs(x,x0) == 0:
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

func = x**4 - 4*x**3 - 2*x**2 + 12*x -5
display("Función original", func)
    
#Se grafica la función para aproximar el rango de las raíces 
# (Los valores se fueron modificando para la precisión)
'''
X = np.arange(-2,5, 0.0001)
Y = []
for i in range(len(X)):
    Y.append(func.subs(x,X[i]))

plt.plot(X,Y)
   ''' 

# Con la información de la gráfica, se utiliza el rango [-5, 5] para  
# encontrar las raíces con el método de Newton
tol = 0.000001
roots = []
rootPrev = np.inf
rng = np.arange(-5,5,0.5)
for i in rng:
    rootCurr = NewtonRaphson(tol, i, func)
    if isinstance(rootCurr, float):
        rootCurr = round(rootCurr, 6)
        if rootCurr != rootPrev:
            roots.append(rootCurr)
            rootPrev = rootCurr
    if len(roots) == 4:
        break


print("Raíces: ", roots)

