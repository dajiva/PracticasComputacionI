# Práctica 2: Notación Asintótica y Complejidad Computacional

## Introducción

### Complejidad computacional

La complejidad computacional es la rama de las ciencias de la computación que como principal objetivo tiene la clasificación y comparación de las solucionaciones a problemas finitos, según su dificultad para lograrlo. (Adaptado de [Dean, W. (2016), *Computational Complexity Theory*](https://plato.stanford.edu/entries/computational-complexity/))

Esta clasificación está dada por el número intrínseco de operaciones necesarias para llevar a cabo un conjunto de pasos (algoritmo) para lograr un objetivo. Estos algoritmos pueden tener diferentes niveles de *eficiencia*, la cual depende del número de operaciones necesarias para completar su objetivo. De forma práctica se tiene una distinción general, la cual divide los algoritmos en dos secciones: [algoritmos con tiempo de ejecución polinómico](https://es.wikipedia.org/wiki/P_(clase_de_complejidad)) también conocidos como algoritmos P, y los de [tiempo no polinómicos](https://es.wikipedia.org/wiki/Teor%C3%ADa_de_la_complejidad_computacional#Clases_de_complejidad_importantes) de los cuales existe una gran variedad.

La siguiente gráfica tiene como propósito mostrar la diferencia entre algoritmos con diferentes complejidades computacionales:

![Comparación de complejidades computacionales](Images/Complejidades.svg)
(Tomada de [Wikipedia](https://en.wikipedia.org/wiki/Big_O_notation#Infinite_asymptotics))

Donde el eje horizontal (*n*) representa la cantidad de elementos del arreglo con el que se opera, y el eje vertical (*N*) representa el número de operaciones para realizar el algoritmo.

Existen diferentes notaciones para indicar la complejidad de un algoritmo en diversas situaciones, a continuación se presentan tres de ellas.

#### Complejidad de cota superior asintótica (Big O Notation)
Para determinar el máximo de operaciones a realizar por un algoritmo se utiliza una notación conocida como de cota superior (también llamada de *orden superior*) y se denota con la letra *O*. La función de esta notación es indicar qué función acota o delimita por la parte superior el número de operaciones realizadas por un algoritmo. En otras palabras, es una forma de indicar, con una función matemática, cuántas operaciones se requieren como máximo para resolver un problema con un cierto algoritmo. Esta función va a depender del número de elementos sobre el que se va a llevar a cabo el algoritmo.

Por ejemplo, si quisieramos calcular la suma de todos los elementos de un arreglo es necesario pasar por cada uno de los elementos y sumarlo a una variable con la suma total. En este caso es necesario pasar una única vez por cada uno de los elementos, de forma que si el arreglo tiene 100 elementos, necesitaremos 100 operaciones, si cuenta con 1000 elementos, serán necesarias 1000 operaciones, 10 elementos requerirán 10 operaciones y así sucesivamente; rápidamente se puede identificar que el número de operaciones ncesarias es igual al número de elementos, en otras palabras, tiene un comportamiento acotado por una función lineal. Esto de denotaría como *O(n)*. Que en la figura superior correspondería con la línea verde.

#### Complejidad de cota inferior asintótica (Big Ω Notation)
Así como se determina la función que acota de forma superior al algoritmo, generalmente también se busca la función que acota por la parte inferior. A esta notación se conoce como cota inferior u *orden inferior* y se denota con la letra griega Ω.
Así como la notación *O*, Ω determina una función, pero en este caso hace referencia al número mínimo de operaciones que requiere llevar a cabo un algoritmo para encontrar una solución. Por ejemplo, si contamos con un arreglo de elementos ordenados, no es necesario buscar en todos los elementos, sino que podemos comenzar por uno de los extremos y detenernos si encontramos un número ya sea más grande o más pequeño (dependiendo del extremo que hayamos comenzado) de forma que, si somos afortunados, nuestro algoritmo podría encontrar el elemento buscado incluso en la primera iteración. Para denotar esto se utiliza la siguiente notación Ω(1) que indica que en el mejor de los casos podríamos encontrar la respuesta de nuestro algoritmo sin necesidad de pasar por todos los elementos.

#### Complejidad promedio asintótica (Big Θ Notation)
En ocasiones, los extremos de los algoritmos no son del todo expresivos del comportamiento, ya que puede menospreciar o subestimar el verdadero tiempo de ejecución necesario para En estos casos, se considera una tercera notación que indica el promedio de ejecución del algoritmo, el cual indica, en promedio, cuál es la función que determina el comportamiento. Esta notación es igualmente utilizada en casos particulares como en aquellos en que tanto el orden *O* y Ω son exactamente iguales, de forma que el promedio de ejecución va a ser el mismo, por ejemplo si se tiene un algoritmo con complejidad *O(n)* y Ω(n) va a tener por tanto también Θ(n).

### Pseudocódigo
Una forma de representar algoritmos de forma independiente al lenguaje de programación es a través de pseudocódigo. Este consiste en la escritura de los pasos o instrucciones del algoritmo en palabras y símbolos más cercanos al lenguaje natural que al lenguaje máquina. Como tal no existen reglas ni espeicificaciones para escribir pseudocódigo, pero sí existen buenas prácticas y recomendaciones. Algunas de las principales es el uso de instrucciones de control como comandos `if`, `else`, ciclos como `for` y `while` y operadores lógicos como `and` u `or`. De esta forma se busca describir el comportamiento y funcionamiento de un algoritmo con lenguaje cercano al empleado comúnmente por las personas.
Por ejemplo, un posible pseudocódigo para un algoritmo que regrese la suma de dos números si el primero `x` es mayor al segundo `y` y en caso contrario regrese la resta; podría lucir como lo siguiente:

```
Entradas:
x
y
------
resultado <- 0
if x > y:
  resultado <- x + y
else:
  resultado <- x - y
return resultado
```

Donde `<-` hace referencia a una asignación, `<` es el operador de comparación *menor que* y por último la sentencia `return` indica el valor que va a regresar el algoritmo.


## Descripción

En este proyecto tendrás que describir, para cada algoritmo, la complejidad computacional de cada uno de ellos, y tendrás que anotar el resultado del algoritmo para un conjunto de valores de entrada determinado.

### Algoritmo 1
```
Entradas:
x
y
------
resultado <- 1
for i from 1 to y:
  resultado <- resultado * x
return resultado
```

##### Resultados
Escribe en la siguiente sección, para el conjunto de entradas indicado, el resultado que daría el algoritmo.

|x|y|resultado|
|-|-|-|
|2|5|32|
|3|3|27|
|10|8|100000000|


##### Complejidad
Escribe en esta sección la complejidad computacional que coresponde con el algoritmo anterior en las diferentes notaciones que creas correspondientes (*O* y/o Ω y/o Θ).

Θ(y)  

### Algoritmo 2
```
Entradas:
x
valores
------
for each val in valores:
  if val > x:
    return false
  else if val == x:
    return true
return false
```

##### Resultados
Escribe en la siguiente sección, para el conjunto de entradas indicado, el resultado que daría el algoritmo.

|x|valores|resultado|
|-|-|-|
|4|[1, 2, 4, 7, 9]|true|
|9|[1, 3, 5, 6, 7]|false|
|3|[5, 6, 7, 8, 9, 10]|false|


##### Complejidad
Escribe en esta sección la complejidad computacional que coresponde con el algoritmo anterior en las diferentes notaciones que creas correspondientes (*O* y/o Ω y/o Θ).

O(n) y Ω(1)  

### Algoritmo 3
```
Entradas:
valores_x
valores_y
------
for each valx in valores_x:
  y_contiene_x <- false
  for each valy in valores_y:
    if valx == valy:
      y_contiene_x <- true
  if y_contiene_x == false:
    return false
return true
```

##### Resultados
Escribe en la siguiente sección, para el conjunto de entradas indicado, el resultado que daría el algoritmo.

|valores_x|valores_y|resultado|
|-|-|-|
|[1, 2, 3]|[1, 2, 3, 4, 5]|true|
|[2, 4]|[7, 5, 2, 8, 3]|false|
|[3, 5, 2]|[6, 5, 3, 7, 1, 2]|true|


##### Complejidad
Escribe en esta sección la complejidad computacional que coresponde con el algoritmo anterior en las diferentes notaciones que creas correspondientes (*O* y/o Ω y/o Θ).

O(n<sup>2</sup>) y Ω(n)
