# Tarea Pseudocodigo
*Daniela Jiménez Vargas*
## Determinar el mayor de dos números
MayorDosNumeros(A,B)
	if A > B
		return A
	else if B > A
		return B
	else 
		return A, B
## Determinar si un numero es primo
EsPrimo(n)
	if |n| <= 2
		return true
	for i <- 2 a n-1
		if n % x = 0
			return false
	return true
## Determinar si dos cadenas son palíndromas
Palindromos(Texto1,Texto2)
	n = tamaño de Texto1
	inv <- cadena vacía de tamaño n
	for i <- 1 a n
		inv<sub>i</sub> = Texto1<sub>n-1-i</sub>
	if inv = Texto2
		return true
	else 
		return false
## Determinar si "ant" es una subcadena de "Se han establecido antecedentes desde el siglo XIX"
Subcadena(sub,cadena)
	n = tamaño de sub
	for i <- 1 a tamaño de cadena -n
		if cadena<sub>i:i+n-1</sub> = sub
			return true
	return false



	

