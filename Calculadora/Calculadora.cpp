/* Author: Daniela Jiménez Vargas
 * Email: dajiva@comunidad.unam.mx
 * 08/09/2020
 *
 * Imprime el resultado de una operación elegida por el usuario entre dos variables de entrada
 */
#include <iostream>

using namespace std;

int main() {
    // Inicializar variables
    float n1{0}, n2{0};
    float result{0};
    int n1int = 0;
    int n2int = 0;
    string continuar;
    string op;
    bool cont = true;
    bool repeat = true;

    while (cont) {
        // Pedir números al usuario
        cout << "Primer número: ";
        cin >> n1;
        cout << "Operación: ";
        cin >> op;
        cout << "Segundo número: ";
        cin >> n2;

        // Realizar operaciones
        if (op == "+") {
            result = n1 + n2;
        } else if (op == "-") {
            result = n1 - n2;
        } else if (op == "*" || op == "x") {
            result = n1 * n2;
        } else if (op == "/") {
            if (n2 == 0) {
                cout << "Error. No es posible dividir entre 0";
            }
            else {
                result = n1 / n2;
            }
        } else if (op == "%") {
            n1int= static_cast<int>(n1);
            n2int = static_cast<int>(n2);
            result = n1int % n2int;
        } else {
            cout << "Operación no válida";
        }
        cout << result<< endl;
        repeat = true;
        while (repeat) {
            cout << "¿Desea hacer otra operación? Escriba sí o no" << endl;
            cin >> continuar;
            if (continuar == "sí" || continuar == "si") {
                cont = true;
                repeat = false;
            } else if (continuar == "no") {
                repeat = false;
                cont = false;
            }
            else {
                cout << "Escriba solo sí o no";
            }
        }
    }
        return 0;
}
