//
// Created by Daniela Jimenez Vargas on 10/12/20.
//

#include "Almacen.h"

using namespace std;

bool Almacen::ModificarInventarioArticulo(Articulo* artPtr, int cantidad)
{
    bool valida = false;
    bool existe = false;
    for (auto & articulo : articulos) {
        if (articulo.articulo == artPtr) {
            existe = true;
            if (articulo.cantidad + cantidad >= 0) {
                articulo.cantidad += cantidad;
                valida = true;
            }
        }
    }
    if(!existe && cantidad >=0){
        ArticuloAlmacenado nuevo{artPtr, cantidad};
        articulos.push_back(nuevo);
        valida = true;
    }
    return valida;
}

string Almacen::ObtenerNombre()  const
{
    return nombre;
}

string Almacen::ObtenerInventario() const
{
    string invStr = "";
    invStr.append("\nArticulo\tCantidad\n");
    for (int i = 0, n = articulos.size(); i < n; i++)
    {
        invStr.append(articulos[i].articulo->nombre);
        invStr.append("\t");
        invStr.append(to_string(articulos[i].cantidad));
        invStr.append("\n");
    }
    return invStr;
}
