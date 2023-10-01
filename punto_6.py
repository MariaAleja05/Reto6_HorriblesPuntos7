# -*- coding: utf-8 -*-
"""Punto_6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RyLPKr76XsXXICfinr2kBoVhA43Up0iB

# **Sexto Punto**

**Enunciado:** El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
"""

def CalcularContagiados(D:int, C:int) -> int:
  contagiados = C*(2**D)
  return contagiados

if __name__ == "__main__":
  D = int(input("Ingrese el numero de dias:"))
  C = int(input("Ingrese contagiados actuales:"))
  total_c = CalcularContagiados(D, C)
  print("----------------------------------------------------------------")
  print("El total de contagiados en NuncaLandia es " + str(total_c))