#ifndef TIENDA_ALMACEN_H
#define TIENDA_ALMACEN_H

#include <vector>
#include <string>

using namespace std;

struct Articulo
{
    string nombre = "";
    string fabricante = "";
    float precio = 0;
};

struct ArticuloAlmacenado
{
    Articulo* articulo;
    int cantidad;
};

class Almacen
{
private:
    string nombre;
    vector<ArticuloAlmacenado> articulos;
public:
    Almacen() : nombre("") {};
    Almacen(string nom) : nombre(nom) {};
    string ObtenerNombre() const;
    bool ModificarInventarioArticulo(Articulo* artPtr, int cantidad);
    string ObtenerInventario() const;
};

#endif // !TIENDA_ALMACEN_H