//
// Created by Daniela Jimenez Vargas on 26/11/20.
//

#ifndef PUNTOISOELECTRICO_MOLECULA_H
#define PUNTOISOELECTRICO_MOLECULA_H

#include <string>
#include <vector>
#include "Grupo.h"


using namespace std;

class Molecula {
private:
    string nombreMolecula;
    vector< Grupo > gruposMolecula;

public:
    Molecula() { nombreMolecula = "";};
    Molecula(string nom) { nombreMolecula = nom;}
    void AgregarGrupo(Grupo miGrupo);
    float CalcularPuntoIsoelectrico();

};


#endif //PUNTOISOELECTRICO_MOLECULA_H
