# Comparación de tiempos de ejecución: C++, Python y Python + Numpy

#### Daniela Jiménez Vargas


Para esta práctica se implementó el método de Gauss Jordan en dos lenguajes diferentes: C++ y Python. Para éste último se escribieron dos programas distintos. En el primero se utilizó una lista dentro de otra para representar la matriz. El otro método fue usar un arreglo en dos dimensiones de la librería de Numpy. Utilizando el header `chronos` de C++ y la librería `time` en Python se midió el tiempo que le tomó a cada una de las implementaciones  encontrar la solución a un sistema de tres ecuaciones. Como los tiempos varían con cada ejecución, se corrió cada programa 10 veces para obtener un promedio. Los resultados se muestras en la tabla a continuación. 

| Lenguaje  | Promedio de tiempo de ejecución ($\mu$s) |
| ------------- | ------------- |
| C++  | 101.1  |
| Python  | 844.907 |
| Python + Numpy | 1375.083  |

El tiempo de C++ resultó ser notablemente menor, pero en Python se tiene la ventaja de que es más fácil modificar el tamaño del arreglo a preferencia del usuario 


