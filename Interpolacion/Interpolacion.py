import pandas as pd
import numpy as np
from sympy.abc import x
import matplotlib.pyplot as plt

#Interpolación
def NewtonInt(X, Y, n, xi):
    fdd = np.zeros((n,n))
    
    for i in range(n):
        fdd[i,0] = Y[i]
    
    for j in range(1,n):
        for i in range(n-j):
            fdd[i,j] = (fdd[i+1,j-1] - fdd[i,j-1])/(X[i+j] - X[i])
    
    xterm = 1
    yint = np.zeros(n)
    ea = np.zeros(n)
    yint[0] = fdd[0,0]
    for o in range(1,n):
        xterm *= (xi - X[o-1])
        yint2 = yint[o-1] + fdd[0,o] * xterm
        ea[o-1] = yint2 - yint[o-1]
        yint[o] = yint2
        
    return yint

#Leer los dataframes
# Datos datahub
dfRef = pd.read_csv("https://raw.githubusercontent.com/dajiva/PracticasComputacionI/master/Interpolacion/population_csv.csv")
dfRef = dfRef[ dfRef['Country Name'] == 'Mexico' ] #Seleccionar datos México
#Limpiar datos
dfRef = dfRef.set_index('Year') 
dfRef = dfRef.drop(labels = ['Country Name', 'Country Code'], axis = 1)

#Datos INEGI
df = pd.read_csv("https://raw.githubusercontent.com/dajiva/PracticasComputacionI/master/Interpolacion/poblacionMX.csv")

# Generar variables y listas
X = df['Año'].astype(int)
Y = df['Poblacion'].astype(int)
n = len(X)

#Valores referencia
xRef = X[5:14]
dfRef = dfRef.drop(xRef) #Eliminar años dados por los censos

#Listas para graficar
años = dfRef.index
años = años[0:45]
errors = []

#Realizar interpolación y calcular error
for i in range(len(dfRef)-5):
    interpolation = NewtonInt(X, Y, n, años[i])
    pob = interpolation[-1]
    pobReal = dfRef.iloc[i]['Value']
    errors.append(abs(pob - pobReal)/pobReal)

#Gráfica
plt.plot(años, errors)
plt.title("Error en la interpolación de la población")
plt.xlabel("Año")
plt.ylabel("Error")

    
print("Promedio error: " ,np.mean(errors))

#Evaluación error y grados del polinomio
grado = np.arange(1, 16)
#1975
ea75 = []
pob75 = NewtonInt(X, Y, n, 1975)
pob75R = dfRef.iloc[13]['Value']
for i in pob75:
    ea75.append(abs(i - pob75R)/pob75R)
#2005
ea04 = []
pob04 = NewtonInt(X, Y, n, 2004)
pob04R = dfRef.iloc[38]['Value']
for i in pob04:
    ea04.append(abs(i - pob04R)/pob04R)

#Gráfica
fig, ax = plt.subplots()  
ax.plot(grado, ea75, label='1975') 
ax.plot(grado, ea04, label='2004') 
ax.set_xlabel('Grado del polinomio')  
ax.set_ylabel('Error')  
ax.set_title("Evolución del error con el incremento del grado en el polinomio")  
ax.legend() 