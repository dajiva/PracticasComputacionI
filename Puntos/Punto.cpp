//
// Created by Daniela Jimenez Vargas on 04/11/20.
//

#include "Punto.h"
#include <cmath>

void Punto2D::SetPosicion(float posX, float posY){
    x = posX;
    y = posY;
}

void Punto2D::Trasladar(float tx, float ty){
    x += tx;
    y += ty;
}

void Punto2D::ConvertirARadianes(float &theta) {
    theta *= M_PI / 180;
}

void Punto2D::RotarRespectoAlOrigen(float theta) {
    float xtemp = x, ytemp = y;
    ConvertirARadianes(theta);
    x = xtemp * cos(theta) - ytemp* sin(theta);
    y = xtemp * sin(theta) + ytemp* cos(theta);
}

void Punto2D::Escalar(float factorx, float factory) {
    x *= factorx;
    y *= factory;
}

float Punto2D::GetX() {
    return x;
}

float Punto2D::GetY() {
    return y;
}