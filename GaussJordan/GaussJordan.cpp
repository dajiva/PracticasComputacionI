#include <iostream>
#include <array>

// Añadir std para fácil llamado de funciones
using namespace std;

//// Declaración de funciones
//Definimos un template (un tipo de dato) para nuestra matriz
template <typename matriz>
void LlenarMatriz(matriz & miMatriz);

template <typename matriz>
void ImprimirMatriz(matriz & miMatriz);

template <typename matriz>
void GaussJordan(matriz & miMatriz);

template <typename matriz>
void IntercambiarRenglones(matriz & miMatriz, int x);

template <typename matriz>
void ImprimirSolucion(matriz & miMatriz);


int main()
{
    // Definimos el número de variables de nuestro sistema
    const int variables = 3;
    // El número de columnas será el número de variables más su solición para cada ecuación
    const int columnas = variables + 1;

    // Inicializamos la matriz que vamos a ocupar
    array <array<float, columnas>, variables> miMatriz = { 0 };

    // Pedimos al usuario que llene la matriz
    LlenarMatriz(miMatriz);

    // Aplicamos el método de Gauss-Jordan sobre nuestra matriz
    GaussJordan(miMatriz);

    // Imprimimos la solución de la matriz
    ImprimirSolucion(miMatriz);

    return 0; // Indicamos que salimos del programa con éxito
}

/*
Llena 'miMatriz' con valores ingresados por el usuario para cada elemento.
No regresa ningún valor.
*/
template <typename matriz>
void LlenarMatriz(matriz & miMatriz)
{
    int variables = miMatriz.size();
    for (int i = 0; i < variables; i++) {
        for (int j = 0; j <= variables; j++) {
            cout << "Valor elemento [" << i << "][" << j << "]: ";
            cin >> miMatriz[i][j];
        }
    }
}

/*
Imprime cada elemento de 'miMatriz' emulando una matriz con corchetes cuadrados.
No regresa ningún valor.
*/
template <typename matriz>
void ImprimirMatriz(matriz & miMatriz)
{
    int variables = miMatriz.size();
    for (int i = 0; i < variables; i++) {
        cout << "[ ";
        for (int j = 0; j < variables + 1; j++)
            cout << miMatriz[i][j] << '\t';
        cout << "]\n";
    }
}

/*
Imprime en pantalla la solución para cada variable del sistema de ecuaciones correspondiente a los valores en 'miMatriz'.
No regresa ningún valor.
*/
template <typename matriz>
void ImprimirSolucion(matriz & miMatriz)
{
    cout << endl;
    cout << "Solución: " << endl;
    bool sol=true;
    int variables = miMatriz.size();
    for (int i = 0; i < variables; i++) {
        if (isnan(miMatriz[i][variables]) || isinf(miMatriz[i][variables])){
            sol= false;
            break;
        }else{
            cout << "x"<< i <<" = " << miMatriz[i][variables]<<endl;
        }
    }
    if (!sol){
        cout << "El sistema de ecuaciones no tiene solución o tiene infinitas soluciones";
    }
}

/*
Implementa el algoritmo de Gauss-Jordan sobre 'miMatriz', finalizando en ella la solución del algoritmo.
No regresa ningún valor.
*/
template <typename matriz>
void GaussJordan(matriz & miMatriz)
{
    int variables = miMatriz.size();
    float p;
    for (int x=0; x < variables; x++) {
        if (miMatriz[x][x] == 0){
            IntercambiarRenglones(miMatriz,x);
        }
        for (int i=x+1; i < variables; i++) {
            p = miMatriz[i][x]/miMatriz[x][x];
            miMatriz[i][x] = 0;
            for (int j=x+1; j < variables+1; j++) {
                miMatriz[i][j]-= p*miMatriz[x][j];
            }
        }
    }
    for (int x=variables-1; x > 0 ; x--) {
       for (int i=0; i < x; i++) {
            p = miMatriz[i][x]/miMatriz[x][x];
            miMatriz[i][x] = 0;
            miMatriz[i][variables]-= p*miMatriz[x][variables];
        }
    }
    for (int i=0; i < variables; i++) {
        miMatriz[i][variables] /= miMatriz[i][i];
        miMatriz[i][i]=1;
    }
}

template <typename matriz>
void IntercambiarRenglones(matriz & miMatriz, int x){
    const int variables = 3;
    array<int, variables> temp= {};
    for (int i = 0; i < variables +1; i++) {
        temp[i] = miMatriz[x][i];
    }
    for (int i = 0; i < variables +1; i++) {
        miMatriz[x][i]= miMatriz[x+1][i];
        miMatriz[x+1][i]= temp[i];
    }
}
