import numpy as np
from sympy import symbols
from MetodosRaices import RootsMethods

v = symbols('x')

'''
Creación de diccionario 'gases' a partir de una tabla en Excel

from pandas import *
xls = ExcelFile('/Users/DAJIVA/ComputacionI/Constantes.xlsx')
df = xls.parse(xls.sheet_names[0])
df = df.set_index('Formula')
self.gases = df.to_dict('index')
'''


class MolalVolume:
    
    def __init__(self):
        self.R = 0.082054
        self.gases = {'CH3COOH': {'Nombre': 'Ácido acético', 'a': 17.82, 'b': 0.1068}, 'C4H6O3': {'Nombre': 'Anhídrido acético', 'a': 20.16, 'b': 0.1263}, 'CH3COCH3': {'Nombre': 'Acetona', 'a': 14.09, 'b': 0.0994}, 'C2H3N': {'Nombre': 'Acetonitrilo', 'a': 17.81, 'b': 0.1168}, 'C2H2': {'Nombre': 'Acetileno', 'a': 4.448, 'b': 0.05136}, 'NH3': {'Nombre': 'Amoníaco', 'a': 4.225, 'b': 0.03707}, 'Ar': {'Nombre': 'Argón', 'a': 1.363, 'b': 0.03219}, 'C6H6': {'Nombre': 'Benceno', 'a': 18.24, 'b': 0.1154}, 'C6H5': {'Nombre': 'Bromobenceno', 'a': 28.94, 'b': 0.1539}, 'C4H10': {'Nombre': 'Butano', 'a': 14.66, 'b': 0.1226}, 'CO2': {'Nombre': 'Dióxido de carbono', 'a': 3.64, 'b': 0.04267}, 'CS2': {'Nombre': 'Sulfuro de carbono', 'a': 11.77, 'b': 0.07685}, 'CO': {'Nombre': 'Monóxido de carbono', 'a': 1.505, 'b': 0.03985}, 'CCl4': {'Nombre': 'Cloruro de carbono (IV)', 'a': 19.7483, 'b': 0.1281}, 'Cl': {'Nombre': 'Cloro', 'a': 6.579, 'b': 0.05622}, 'C6H5Cl': {'Nombre': 'Clorobenceno', 'a': 25.77, 'b': 0.1453}, 'C2H5Cl': {'Nombre': 'Cloroetano', 'a': 11.05, 'b': 0.08651}, 'CH3Cl': {'Nombre': 'Clorometano', 'a': 7.57, 'b': 0.06483}, 'C2N2': {'Nombre': 'Cianógeno', 'a': 7.769, 'b': 0.06901}, 'C6H12': {'Nombre': 'Ciclohexano', 'a': 23.11, 'b': 0.1424}, 'C4H10O': {'Nombre': 'Éter dietílico', 'a': 17.61, 'b': 0.1344}, 'C4H10S': {'Nombre': 'Sulfuro de dietilo', 'a': 19.0, 'b': 0.1214}, 'C2H6O': {'Nombre': 'Éter de dimetilo', 'a': 8.18, 'b': 0.07246}, 'C2H6O4S': {'Nombre': 'Sulfuro de dimetilo', 'a': 13.04, 'b': 0.09213}, 'C2H6': {'Nombre': 'Etano', 'a': 5.562, 'b': 0.0638}, 'CH3CH2SH': {'Nombre': 'Etanotiol', 'a': 11.39, 'b': 0.08098}, 'CH3CH2OH': {'Nombre': 'Etanol', 'a': 12.18, 'b': 0.08407}, 'CH3COOCH2CH3': {'Nombre': 'Acetato de etilo', 'a': 20.72, 'b': 0.1412}, 'C2H7N': {'Nombre': 'Etilamina', 'a': 10.74, 'b': 0.08409}, 'C6H5F': {'Nombre': 'Fluorobenceno', 'a': 20.19, 'b': 0.1286}, 'CH3F': {'Nombre': 'Fluorometano', 'a': 4.692, 'b': 0.05264}, 'CFC': {'Nombre': 'Freón', 'a': 10.78, 'b': 0.0998}, 'GeCl4': {'Nombre': 'Tetracloruro de germanio', 'a': 22.9, 'b': 0.1485}, 'He': {'Nombre': 'Helio', 'a': 0.03457, 'b': 0.0237}, 'C6H14': {'Nombre': 'Hexano', 'a': 24.71, 'b': 0.1735}, 'H': {'Nombre': 'Hidrógeno', 'a': 0.2476, 'b': 0.02661}, 'HBr': {'Nombre': 'Bromuro de hidrógeno', 'a': 4.51, 'b': 0.04431}, 'HCl': {'Nombre': 'Ácido clorhídrico', 'a': 3.716, 'b': 0.04081}, 'H2Se': {'Nombre': 'Seleniuro de hidrógeno', 'a': 5.338, 'b': 0.04637}, 'H2S': {'Nombre': 'Sulfuro de hidrógeno', 'a': 4.49, 'b': 0.04287}, 'C6H5I': {'Nombre': 'Iodobenceno', 'a': 33.52, 'b': 0.1656}, 'Kr': {'Nombre': 'Kriptón', 'a': 2.349, 'b': 0.03978}, 'Hg': {'Nombre': 'Mercurio', 'a': 8.2, 'b': 0.01696}, 'CH4': {'Nombre': 'Metano', 'a': 2.283, 'b': 0.04278}, 'CH3OH': {'Nombre': 'Metanol', 'a': 9.649, 'b': 0.06702}, 'Ne': {'Nombre': 'Neón', 'a': 0.2135, 'b': 0.01709}, 'NO': {'Nombre': 'Óxido nítrico', 'a': 1.358, 'b': 0.02789}, 'N': {'Nombre': 'Nitrógeno', 'a': 1.408, 'b': 0.03913}, 'NO2': {'Nombre': 'Dióxido de nitrógeno', 'a': 5.354, 'b': 0.04424}, 'N2O': {'Nombre': 'Óxido nitroso', 'a': 3.832, 'b': 0.04415}, 'O': {'Nombre': 'Oxígeno', 'a': 1.378, 'b': 0.03183}, 'C5H12': {'Nombre': 'Pentano', 'a': 19.26, 'b': 0.146}, 'PH3': {'Nombre': 'Fosfina', 'a': 4.692, 'b': 0.05156}, 'C3H8': {'Nombre': 'Propano', 'a': 8.779, 'b': 0.08445}, 'SiH4': {'Nombre': 'Silano', 'a': 4.377, 'b': 0.05786}, 'SiF4': {'Nombre': 'Tetrafluoruro de silicio', 'a': 4.251, 'b': 0.05571}, 'SO2': {'Nombre': 'Dióxido de azufre', 'a': 6.803, 'b': 0.05636}, 'SnCl2': {'Nombre': 'Cloruro de estaño (II)', 'a': 27.27, 'b': 0.1642}, 'C5H6CH3': {'Nombre': 'Tolueno', 'a': 24.38, 'b': 0.1463}, 'H20': {'Nombre': 'Agua', 'a': 5.536, 'b': 0.03049}, 'Xe': {'Nombre': 'Xenón', 'a': 4.25, 'b': 0.05105}}
        
    def obtenerConstantes(self, gas):
        a = self.gases[gas]['a']
        b = self.gases[gas]['b']
        return a, b
        
    def calcularVm(self, P, T, gas, tol = 0.001):
        R = self.R
        RM = RootsMethods()
        a, b = self.obtenerConstantes(gas)
        f = (P + a/v**2)*(v - b)- R*T
        v0 = P*R*T
        
        Vm = RM.NewtonRaphson(tol, 90000, v0, f)
        return Vm


def validarGas(dct):    
    noValido = True
    while noValido:
        opcion = input("\n")
        if opcion not in dct:
            print('Gas no encontrado, escriba: \n 1. Intentar de nuevo   2. Añadir nuevo gas ')
            noVal = True
            while noVal:
                selec = input("\n")
                if selec == '1' :
                    break
                elif selec == '2':
                    agregarGas(dct)
                    noVal = False
                    noValido = False
                else:
                    print('Selección inválida, por favor seleccione 1 o 2')
        else:
            noValido = False
    return opcion

def agregarGas(dct):  
    formula = input("Formula: ")
    dct[formula] = dict(Nombre = input("Nombre: ") , a = float(input("Constante a (atm·L/mol^2): ")) , b = float(input("Constante b (L/mol): ")))
                         

VolMol = MolalVolume()
print("Ingrese la formula del gas del sistema")
gas = validarGas(VolMol.gases)
P = float(input('Presión (atm): '))
T = float(input('Temperatura (K): '))

Vm = VolMol.calcularVm(P, T, gas) 
print("El volumen molar es: ", Vm, "L/mol")
