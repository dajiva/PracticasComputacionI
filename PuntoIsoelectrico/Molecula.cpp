//
// Created by Daniela Jimenez Vargas on 26/11/20.
//

#include "Molecula.h"
#include "Grupo.h"

using namespace std;


int CalcularCarga(float& ph, float& phSup, vector<Grupo> todosGrupos);

void Molecula::AgregarGrupo(Grupo grupo){
    gruposMolecula.push_back(grupo);
}

float Molecula::CalcularPuntoIsoelectrico(){
    float ph{0}, phSup{0};
    if(gruposMolecula.size() == 2){
        ph = gruposMolecula[0].GetpK();
        phSup = gruposMolecula[1].GetpK();
    }else
        {
        for(int i=0, num = gruposMolecula.size()-1; i < num; i++){
            ph = gruposMolecula[i].GetpK();
            if(CalcularCarga(ph, phSup, gruposMolecula) == 0){
                break;
            }
        }
    }
    return (ph+phSup)/2;
}


int CalcularCarga(float& ph, float& phSup, vector<Grupo> todosGrupos)
{
    int carga = 0, indInf;
    float phInf= 0;
    int numGrupos = todosGrupos.size();
    phSup = 14;

    for(int i=0; i < numGrupos; i++){
        float pK = todosGrupos[i].GetpK();
        if( pK <= ph && pK > phInf) {
            indInf = i;
            phInf = pK;
        } else if( pK > ph && pK < phSup){
            phSup = pK;
        }
    }

    for(int i=0; i < numGrupos; i++){
        int cargaMax = todosGrupos[i].GetCarga();
        int cargaMin = cargaMax + 1;
        if(i <= indInf){
            carga += cargaMax;
        } else{
            carga += cargaMin;
        }
    }

    return carga;
}