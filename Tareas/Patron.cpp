#include <iostream>
#include <array>
#include <cstdlib>
#include <ctime>

#define size 5

using namespace std;

void Patron(array<array<int, size>, size> &);


int main() {
    array<array<int, size>, size> M= {};

    srand((int) time(0));

    cout << "Matriz base: " << endl;
    for (int i = 0; i < size; i++){
        for (int j = 0; j < size; j++){
            M[i][j] = (rand() % 9) +1;
            cout << M[i][j] << "  ";
        }
        cout << endl;
    }
    cout << endl;
    cout << "Matriz con patrón: " << endl;
    Patron(M);


    return 0;
}

void Patron(array<array<int, size>, size> &M)
{
    int val;
    for (int i = 0; i < size; i++){
        val= i;
        for (int j = 0; j < size; j++){
            M[i][j] = val;
            cout << M[i][j] << "  ";
            if (j<i) {
                val--;
            } else {
                val++;
            }
        }
        cout << endl;
    }
}