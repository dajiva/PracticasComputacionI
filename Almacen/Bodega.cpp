//
// Created by Daniela Jimenez Vargas on 04/12/20.
//

#include "Bodega.h"

#include <iostream>

/*
 * Agrega un artículo a la bodega, si se intenta agregar un artículo
 * que ya existe regresa "false", de lo contrario agrega el apuntador
 * al artículo al final del vecor de artículos y regresa "true"
*/
bool Bodega::AgregarArticulo(string* artPtr)
{
    for (int i = 0, n = articulos.size(); i < n; i++)
    {
        if (articulos[i] == artPtr)
            return false;
    }
    articulos.push_back(artPtr);
    return true;
}

/*
 * Regresa un string con la descripción del inventario
 * de la forma `Articulo <i> es <nombreArticulo>`
 * para cada artículo en la bodega
*/
string Bodega::ObtenerInventario()
{
    string inv = "";
    for (int i = 0, n = articulos.size(); i < n; i++)
    {
        inv.append("Articulo ");
        inv.append(to_string(i));
        inv.append(" es ");
        string articulo = *articulos[i];
        inv.append(articulo);
        inv.append("\n");
    }
    return inv;
}