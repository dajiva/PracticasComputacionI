#include <iostream>
#include <string>
#include <array>

using namespace std;

// Incluimos las clases a ocupar
#include "Bodega.h"

//Declaración de funciones
Bodega CrearBodega(int i);
string CrearArticulo(int i);
void AgregarArticuloABodega(string* artPtr, Bodega& bodega);


int main()
{
    const int numBodegas = 2, numArticulos = 3;
    // Arreglo que contendrá todas las bodegas
    array<Bodega, numBodegas> misBodegas;

    /*
     * Para cada bodega a crear le pedimos al usuario que nos dé la información
     * y la nueva instancia regresada la agregamos al final del vector misBodegas
    */
    for (int i = 0; i < numBodegas; i++)
        misBodegas[i] = CrearBodega(i);

    // Arreglo que contendrá todos los artículos
    array<string, numArticulos> misArticulos;

    /*
     * Para cada artículo a crear le pedimos al usuario que nos dé la información
     * y para cada nuevo artículo le preguntamos al usuario si la desea agregar a
     * cada bodega, si el usuario quiere agregar el artículo a la bodega la
     * agregamos PASANDO EL APUNTADOR A ESE ARTÍCULO y aregándolo a los artículos
     * de la bodega seleccionada
    */
    for (int i = 0; i < numArticulos; i++)
    {
        string nom = CrearArticulo(i);
        misArticulos[i] = nom;
        for (int j = 0; j < numBodegas; j++) {
            int agregar;
            do {
                cout << "¿Desea agregar " << nom << " a la bodega " << misBodegas[j].ObtenerNombre()<< "? (1 sí, 0 no): ";
                cin >> agregar;
                if(agregar == 1){
                    AgregarArticuloABodega(&misArticulos[i], misBodegas[j]);
                }
                else if (agregar == 0){
                    cout << "Artículo no agregado" << endl;
                }
            } while (agregar!=1 && agregar!=0);

        }
    }

    // Imprimimos el inventario de cada bodega
    cout << endl;
    for (int i = 0; i < numBodegas; i++)
    {
        cout << "Inventario bodega " << misBodegas[i].ObtenerNombre() << endl;
        cout << misBodegas[i].ObtenerInventario() << endl;
    }

    // Si salió bien, regresamos el valor cero
    return 0;
}


// Crea y regresa un string con el nombre de un articulo
string CrearArticulo(int i)
{
    string nombreArt;
    cout << "Nombre del articulo " << i << ": ";
    cin >> nombreArt;
    return nombreArt;
}


// Intenta agregar un artículo a una bodega, si ese artículo ya existe no lo agrega
void AgregarArticuloABodega(string* artPtr, Bodega& bodega)
{
    if (bodega.AgregarArticulo(artPtr))
        cout << "Articulo agregado exitosamente." << endl;
    else
        cout << "Articulo duplicado. No fue agregado." << endl;
}


// Crea y regresa una nueva bodega con los datos ingresados por el usuario
Bodega CrearBodega(int i)
{
    string nombreBodega;
    cout << "Nombre bodega " << i << ": ";
    cin >> nombreBodega;
    Bodega nuevaBodega(nombreBodega);
    return nuevaBodega;
}