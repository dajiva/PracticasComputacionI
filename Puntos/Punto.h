//
// Created by Daniela Jimenez Vargas on 04/11/20.
//

#ifndef PUNTO_PUNTO_H
#define PUNTO_PUNTO_H


class Punto2D {
private:
    float x{0}, y{0};

public:
    void SetPosicion(float posX, float posY);
    void Trasladar(float tx, float ty);
    void RotarRespectoAlOrigen(float theta);
    void Escalar(float factorx, float factory);
    float GetX();
    float GetY();

    void ConvertirARadianes(float &theta);
};


#endif //PUNTO_PUNTO_H