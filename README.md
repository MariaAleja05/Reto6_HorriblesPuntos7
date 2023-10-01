# Reto número 5 repo
### Fecha:  27-09-2023
### Link notebook: [https://colab.research.google.com/drive/1Pi8c02YPXBmrL5JBlRjQ2iLkWFhbr-iX?usp=sharing](https://colab.research.google.com/drive/1ksy4G5S3UBrs5hk11EyObZtPcBD_9bEK?usp=sharing)
### Nota: Si usted está tomando como referencia mi trabajo, porfavor déjame una estrellita por mi esfuerzo :) 

**1.** Dado la figura de la imagen, desarrolle:
- Una función matemática para calcular el volumen y el área superficial.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
- Revise como utilizar el valor de pi usando import math y math.pi
* 
* Mirar archivo Punto_1.py
```pseudocode
import math as m
p=m.pi

def CalcularVolumen(r1:float, r2:float, h:float) -> float:
  vol = ((4*p*(r1**3))/3) + (((p*(r2**2)*h))/3)
  return vol

def CalcularAreaSuperficial(r1:float, r2:float, h:float) -> float:
  asup = (4*p*(r1**2)) + (p*r2*(m.sqrt((r2**2)+(h**2))))
  return asup

def Calcularr1(r1:float) -> float:
  vol_esf = ((4*p*(r1**3))/3)
  r1c = ((3*vol_esf)/(4*p))**(1/3)
  return r1c

def CalcularR2yh(r2:float, h:float) -> float:
  vol_cono = (((p*(r2**2)*h))/3)
  r2c = m.sqrt((3*vol_cono)/(p*h))
  hc = ((3*vol_cono)/(p*(r2**2)))
  return r2c, hc

if __name__ == "__main__":
  r1 = float(input("Ingrese radio 1 de la esfera:"))
  r2 = float(input("Ingrese radio 2 del cono:"))
  h = float(input("Ingrese altura del cono:"))
  vol_total = CalcularVolumen(r1, r1, h)
  asup_total = CalcularAreaSuperficial(r1, r1, h)
  r1cal = Calcularr1(r1)
  r2yhcal = CalcularR2yh(r2, h)
  print("----------------------------------------------------------------")
  print("El volumen total es " + str(vol_total))
  print("El area superficial total es " + str(asup_total))
  print("----------------------------------------------------------------")
  print("El valor del radio de la esfera es " + str(r1cal))
  print("El valor de radio del cono y su altura es " + str(r2yhcal))
```
**2.** Dado la figura de la imagen, desarrolle:
- Una función matemática para calcular el área y el perimetro.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
- Revise como utilizar el valor de pi usando import math y math.pi
* 
* Mirar archivo Punto_2.py
```pseudocode
import math as m
p=m.pi

def CalcularArea(r:float, a:float, b:float) -> float:
  area = (2*(p*(r**2))) + (b*a)
  return area

def CalcularPerimetro(r:float, a:float, b:float) -> float:
  perimetro = (2*p*r) + (2*(b+a))
  return perimetro

def Calcularr(r:float) -> float:
  area_circulo = (p*(r**2))
  rc = m.sqrt(area_circulo/p)
  return rc

def CalcularAyB(a:float, b:float) -> float:
  area_rect = (b*a)
  a = area_rect/b
  b = area_rect/a
  return a, b

if __name__ == "__main__":
  r = float(input("Ingrese radio de los circulos:"))
  a = float(input("Ingrese la altura del rectangulo:"))
  b = float(input("Ingrese la base del rectangulo:"))
  area_total = CalcularArea(r, a, b)
  perimetro_total = CalcularPerimetro(r, a, b)
  rcal = Calcularr(r)
  AyBcal = CalcularAyB(a, b)
  print("----------------------------------------------------------------")
  print("El area total es " + str(area_total))
  print("El perimetro total es " + str(perimetro_total))
  print("----------------------------------------------------------------")
  print("El valor del radio de la esfera es " + str(rcal))
  print("El valor de radio del cono y su altura es " + str(AyBcal))
```
**3.** Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
* 
* Mirar archivo Punto_3.py
```pseudocode
def CalcularCantidadCarne(N:float, M:float, K:float) -> float:
  cantidad_carne = (6*N) + (7*M) + (1*K)
  return cantidad_carne

if __name__ == "__main__":
  N = float(input("Ingrese el número de gallinas:"))
  M = float(input("Ingrese el número de gallos:"))
  K = float(input("Ingrese el número de pollitos:"))
  carne_total = CalcularCantidadCarne(N, M, K)
  print("----------------------------------------------------------------")
  print("La cantidad de carne de aves en kilos es " + str(carne_total))
```
**4.** Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
* 
* Mirar archivo Punto_4.py
```pseudocode
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
```
**5.** Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
* 
* Mirar archivo Punto_5.py
```pseudocode
def CalcularPrestamo(c:float, i:float, n:float) -> float:
  interes_mes = i/12
  total = c*((1+interes_mes)**n)
  return total

if __name__ == "__main__":
  c = float(input("Ingrese el valor del prestamo inicial:"))
  i = float(input("Ingrese el interés anual:"))
  n = float(input("Ingrese la cantidad de meses:"))
  total_f = CalcularPrestamo(c, i, n)
  print("----------------------------------------------------------------")
  print("El interes compuesto es " + str(total_f))
```
**6.** El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
* 
* Mirar archivo Punto_6.py
```pseudocode
def CalcularContagiados(D:int, C:int) -> int:
  contagiados = C*(2**D)
  return contagiados

if __name__ == "__main__":
  D = int(input("Ingrese el numero de dias:"))
  C = int(input("Ingrese contagiados actuales:"))
  total_c = CalcularContagiados(D, C)
  print("----------------------------------------------------------------")
  print("El total de contagiados en NuncaLandia es " + str(total_c))
```
**7.** Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
- El promedio
- La mediana
- El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
- Ordenar los números de forma ascendente
- Ordenar los números de forma descendente
- La potencia del mayor número elevado al menor número
- La raíz cúbica del menor número
* 
* Mirar archivo Punto_7.py
```pseudocode

```
**8.** Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.
* 
* Mirar archivo Punto_8.py
```pseudocode

```
**9.** Consultar qué es y cómo funciona pip en python.
* 
**10.** Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.
* 
