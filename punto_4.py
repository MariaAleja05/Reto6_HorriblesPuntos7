# -*- coding: utf-8 -*-
"""Punto_4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RyLPKr76XsXXICfinr2kBoVhA43Up0iB

# **Cuarto Punto**

**Enunciado:** Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
"""

def CalcularVueltas(P:int, M:int, H:int, B:int) -> int:
  precio = (300*P) + (3300*M) + (350*H)
  vueltas = B-precio
  return vueltas

if __name__ == "__main__":
  P = int(input("Ingrese el número de panes:"))
  M = int(input("Ingrese el número de bolsas de leche:"))
  H = int(input("Ingrese el número de huevos:"))
  B = int(input("Ingrese el billete con el que va a pagar:"))
  vueltas_t = CalcularVueltas(P, M, H, B)
  print("----------------------------------------------------------------")
  if vueltas_t>0:
    print("Las vueltas son " + str(vueltas_t))
  elif vueltas_t<0:
    print("Se deben al vendedor " + str(vueltas_t))
  else:
    print("No hay vueltas " + str(vueltas_t))