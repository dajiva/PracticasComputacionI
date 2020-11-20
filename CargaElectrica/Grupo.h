//
// Created by Daniela Jimenez Vargas on 18/11/20.
//


#ifndef CARGAELECTRICA_GRUPO_H
#define CARGAELECTRICA_GRUPO_H

#include <string>

using namespace std;

class Grupo {
private:
    string nombreGrupo;
    float pkGrupo;
    int cargaGrupo;
public:
    Grupo() { nombreGrupo = ""; pkGrupo = 0; cargaGrupo = 0;};
    Grupo(string nom, float pk, int carga) { nombreGrupo = nom; pkGrupo = pk; cargaGrupo = carga;}
    float GetpK();
    int GetCarga();
};


#endif //CARGAELECTRICA_GRUPO_H
