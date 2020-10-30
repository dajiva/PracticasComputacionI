#include <iostream>
#include <array>
#include <cstdlib>
#include <ctime>

//Tamaño matriz
#define size 3

using namespace std;

void llenarMatriz(array<array<int, size>, size> &);
array<array<int, size>, size> transpuesta(array<array<int, size>, size>);
bool esSimetrica(array<array<int, size>, size>);

int main() {
    bool sim= true;
    array<array<int, size>, size> A= {0};
    llenarMatriz(A);
    sim= esSimetrica(A);

    cout << "La matriz"<< endl;
    for (int i = 0; i < size; i++){
        for (int j = 0; j < size; j++){
            cout << A[i][j] << "  ";
        }
        cout << endl;
    }
    if (sim){
        cout << "es simétrica";
    } else{
        cout << "no es simétrica";
    }

}

void llenarMatriz(array<array<int, size>, size> &A)
{
    int valor;
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            cout << "Valor elemento [" << i << "][" << j << "]: ";
            cin >> valor;
            A[i][j] = valor;
        }
    }
}

array<array<int, size>, size> transpuesta(array<array<int, size>, size> M){
    array<array<int, size>, size> MT= {};
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            MT[i][j] = M[j][i];
        }
    }
    return MT;
}

bool esSimetrica(array<array<int, size>, size> Matriz){
    bool simetria =false;
    array<array<int, size>, size> Transpuesta= {};
    Transpuesta= transpuesta(array<array<int, size>, size> (Matriz));
    if (Transpuesta == Matriz){
        simetria=true;
    }
    return simetria;
}
