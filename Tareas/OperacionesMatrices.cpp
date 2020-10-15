#include <iostream>
#include <array>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    int ntemp;
    cout << "Ingrese el tamaño de sus matrices " ;
    cin >> ntemp;

    const int n= ntemp;

    int sum= 0;
    string op;

    int A[n][n] = {};
    int B[n][n] = {};
    int C[n][n] = {};

    srand((int) time(0));

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            A[i][j] = (rand() % 9) +1;
            cout << A[i][j] << "  ";
        }
        cout << endl;
    }
    
    cout << endl;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            B[i][j] = (rand() % 9) +1;
            cout << B[i][j] << "  ";
        }
        cout << endl;
    }

    cout << "Operación: ";
    cin >> op;

    if (op == "+") {
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                C[i][j] = A[i][j] + B[i][j];
                cout << C[i][j] << "  ";
            }
            cout << endl;
        }
    } else if (op == "-") {
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                C[i][j] = A[i][j] - B[i][j];
                cout << C[i][j] << "  ";
            }
            cout << endl;
        }
    } else if (op == "/") {
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                C[i][j] = A[i][j] / B[i][j];
                cout << C[i][j] << "  ";
            }
            cout << endl;
        }
    } else if (op == "*") {
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                sum = 0;
                for (int x = 0; x < n; x++){
                    sum += A[i][x]*B[x][j];
                }
                C[i][j] = sum;
                cout << C[i][j] << "  ";
            }
            cout << endl;
        }
    } else {
        cout << "Operación no válida";
    }

    return 0;
}