# Reto número 6 repo
### Fecha:  27-09-2023
**1.** Dado la figura de la imagen, desarrolle:

Una función matemática para calcular el volumen y el área superficial.

Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.

Revise como utilizar el valor de pi usando import math y math.pi

* Importe de la librería math la función de pi para realizar los cálculos. En la primera función establecí el volumen, en la segunda el area superficial, en la tercera el procedimiento para devolverme y encontrar los valores ingresados del radio, y en la cuarta el procedimiento para encontrar el radio y la altura ingresada. En la función main se solicita ingresar los valores y se ejecutan las funciones.
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

Una función matemática para calcular el área y el perimetro.

Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.

Revise como utilizar el valor de pi usando import math y math.pi

* Importe de la librería math la función de pi para realizar los cálculos. En la primera función establecí la formula para el area, en la segunda el perimetro, en la tercera el procedimiento para devolverme y encontrar el valor ingresado del radio, y en la cuarta el procedimiento para encontrar la altura y la base ingresada. En la función main se solicita ingresar los valores y se ejecutan las funciones.
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
* En la primera función establecí la ecuación para calcular la cantidad de carne teniendo en cuenta los datos del problema. En la función main se solicita ingresar los valores de base y se ejecutan las funciones.
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
* En la primera función establecí la ecuación para calcular las vueltas te teniendo en cuenta los datos del problema. En la función main se solicita ingresar los valores de base, se ejecutan las funciones, y hay un condicional que muestra si hay vueltas o no, y si quedó debiendo dinero.
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
* En la primera función establecí la ecuación para calcular el prestamo con interés compuesto teniendo en cuenta los datos del problema. En la función main se solicita ingresar los valores de base y se ejecutan las funciones.
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
* En la primera función establecí la ecuación para calcular los contagiados teniendo en cuenta los datos del problema. En la función main se solicita ingresar los valores de base y se ejecutan las funciones.
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

El promedio

La mediana

El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)

Ordenar los números de forma ascendente

Ordenar los números de forma descendente

La potencia del mayor número elevado al menor número

La raíz cúbica del menor número

* En la primera función establecí la ecuación para hallar el promedio, en la segunda la mediana, en la tercera el promedio multiplicativo, y en la cuarta el procedimiento para ordenar los números de manera ascendente, en la quinta en orden descendente, en la sexta la potencia del numero mayor eleveado al numero menor, y la septima para hallar la raiz cubica del menor número. En la función main se solicita ingresar los valores y se ejecutan las funciones. (para mayor explicación mirar el repo: taller #1)
* Mirar archivo Punto_7.py
```pseudocode
def CalcularPromedio(a:float, b: float, c:float, d:float, e:float) -> float:
  suma = a+b+c+d+c
  promedio = suma/5
  return promedio

def CalcularMediana(a:float, b: float, c:float, d:float, e:float) -> float:
  #"a" es la mediana
  if c > d > a > b > e or c > d > a > e > b or c > e > a > d > b or c > e > a > b > d or c > b > a > d > e or c > b > a > e > d or d > c > a > b > e or d > c > a > e > b or d > e > a > c > b or d > e > a > b > c or d > b > a > c > e or d > b > a > e > c or e > c > a > b > d or e > c > a > d > b or e > d > a > c > b or e > d > a > b > c or c > d > a > b > e or c > d > a > e > b or c > e > a > d > b or c > e > a > b > d or c > b > a > d > e or c > b > a > e > d or d > c > a > b > e or d > c > a > e > b:
    return a
  #"b" es la mediana
  if a > c > b > d > e or a > c > b > e > d or a > d > b > c > e or a > d > b > e > c or a > e > b > c > d or a > e > b > d > c or c > a > b > d > e or c > a > b > e > d or c > d > b > a > e or c > d > b > e > a or c > e > b > a > d or c > e > b > d > a or d > a > b > c > e or d > a > b > e > c or d > c > b > a > e or d > c > b > e > a or d > e > b > a > c or d > e > b > c > a or e > a > b > c > d or e > a > b > d > c or e > c > b > a > d or e > c > b > d > a or e > d > b > a > c or e > d > b > c > a:
    return b
  #"c" es la mediana
  if a > b > c > d > e or a > b > c > e > d or a > d > c > b > e or a > d > c > e > b or a > e > c > b > d or a > e > c > d > b or b > a > c > d > e or b > a > c > e > d or b > d > c > a > e or b > d > c > e > a or b > e > c > a > d or b > e > c > d > a or d > a > c > b > e or d > a > c > e > b or d > b > c > a > e or d > b > c > e > a or d > e > c > a > b or d > e > c > b > a or e > a > c > b > d or e > a > c > d > b or e > b > c > a > d or e > b > c > d > a or e > d > c > a > b or e > d > c > b > a:
    return c
  #"d" es la mediana
  if a > b > d > c > e or a > b > d > e > c or a > c > d > b > e or a > c > d > e > b or a > e > d > b > c or a > e > d > c > b or b > a > d > c > e or b > a > d > e > c or b > c > d > a > e or b > c > d > e > a or b > e > d > a > c or b > e > d > c > a or c > a > d > b > e or c > a > d > e > b or c > b > d > a > e or c > b > d > e > a or c > e > d > a > b or c > e > d > b > a or e > a > d > b > c or e > a > d > c > b or e > b > d > a > c or e > b > d > c > a or e > c > d > a > b or e > c > d > b > a:
    return d
  #"e" es la mediana
  if b > c > e > a > d or b > c > e > a > d or b > c > e > d > a or b > c > e > d > a or b > d > e > a > c or b > d > e > a > c or b > d > e > c > a or b > d > e > c > a or c > b > e > a > d or c > b > e > a > d or c > b > e > d > a or c > b > e > d > a or c > e > b > a > d or c > e > b > a > d or c > e > b > d > a or c > e > b > d > a or d > b > e > a > c or d > b > e > a > c or d > b > e > c > a or d > b > e > c > a or d > c > e > a > b or d > c > e > a > b or d > c > e > b > a or d > c > e > b > a:
    return e

def CalcularPromedioMultiplicativo(a:float, b: float, c:float, d:float, e:float) -> float:
  multiplicacion=a*b*c*d*e
  raiz=multiplicacion**(1/5)
  return raiz

def OrdenarAscendente(a:float, b: float, c:float, d:float, e:float) -> float:
  orden1 = a
  orden2 = b
  orden3 = c
  orden4 = d
  orden5 = e
  #1
  if orden1<orden2:
    aux=orden2
    orden2=orden1
    orden1=aux
  if orden1<orden3:
    aux=orden3
    orden3=orden1
    orden1=aux
  if orden1<orden4:
    aux=orden4
    orden4=orden1
    orden1=aux
  if orden1<orden5:
    aux=orden5
    orden5=orden1
    orden1=aux
  #2
  if orden2<orden3:
    aux=orden3
    orden3=orden2
    orden2=aux
  if orden2<orden4:
    aux=orden4
    orden4=orden2
    orden2=aux
  if orden2<orden5:
    aux=orden5
    orden5=orden2
    orden2=aux
  #3
  if orden3<orden4:
    aux=orden4
    orden4=orden3
    orden3=aux
  if orden3<orden5:
    aux=orden5
    orden5=orden3
    orden3=aux
  #4
  if orden4<orden5:
    aux=orden5
    orden5=orden4
    orden4=aux
  return orden5, orden4, orden3, orden2, orden1

def OrdenarDescendente(a:float, b: float, c:float, d:float, e:float) -> float:
  orden1 = a
  orden2 = b
  orden3 = c
  orden4 = d
  orden5 = e
  #1
  if orden1<orden2:
    aux=orden2
    orden2=orden1
    orden1=aux
  if orden1<orden3:
    aux=orden3
    orden3=orden1
    orden1=aux
  if orden1<orden4:
    aux=orden4
    orden4=orden1
    orden1=aux
  if orden1<orden5:
    aux=orden5
    orden5=orden1
    orden1=aux
  #2
  if orden2<orden3:
    aux=orden3
    orden3=orden2
    orden2=aux
  if orden2<orden4:
    aux=orden4
    orden4=orden2
    orden2=aux
  if orden2<orden5:
    aux=orden5
    orden5=orden2
    orden2=aux
  #3
  if orden3<orden4:
    aux=orden4
    orden4=orden3
    orden3=aux
  if orden3<orden5:
    aux=orden5
    orden5=orden3
    orden3=aux
  #4
  if orden4<orden5:
    aux=orden5
    orden5=orden4
    orden4=aux
  return orden1, orden2, orden3, orden4, orden5

def CalcularPoteniaMayor(a, b, c, d, e) -> float:
  #mayor
  if a>b and a>c and a>d and a>e:
    mayor=a
  elif b>a and b>c and b>d and b>e:
    mayor=b
  elif c>a and c>b and c>d and c>e:
    mayor=c
  elif d>a and d>b and d>c and d>e:
    mayor=d
  elif e>a and e>b and e>c and e>d:
    mayor=e
  #menor
  if a<b and a<c and a<d and a<e:
    menor=a
  elif b<a and b<c and b<d and b<e:
    menor=b
  elif c<a and c<b and c<d and c<e:
    menor=c
  elif d<a and d<b and d<c and d<e:
    menor=d
  elif e<a and e<b and e<c and e<d:
    menor=e
  potencia=mayor**menor
  return potencia

def CalcularRaizCubica(a:float, b: float, c:float, d:float, e:float) -> float:
  if a<b and a<c and a<d and a<e:
    cubica_a=a**(1/3)
    return cubica_a
  elif b<a and b<c and b<d and b<e:
    cubica_b = float = b**(1/3)
    return cubica_b
  elif c<b and c<a and c<d and c<e:
    cubica_c = float = c**(1/3)
    return cubica_c
  elif d<b and d<a and d<c and d<e:
    cubica_d = float = d**(1/3)
    return cubica_d
  elif e<b and e<a and e<d and e<c:
    cubica_e = float = e**(1/3)
    return cubica_e

if __name__ == "__main__":
  a = float(input("Ingrese el primer numero:"))
  b = float(input("Ingrese el segundo numero:"))
  c = float(input("Ingrese el tercer numero:"))
  d = float(input("Ingrese el cuarto numero:"))
  e = float(input("Ingrese el quinto numero:"))
  promedio_f = CalcularPromedio(a, b, c, d, e)
  mediana_f = CalcularMediana(a, b, c, d, e)
  promediomultiplicativo_f = CalcularPromedioMultiplicativo(a, b, c, d, e)
  ascendente_f = OrdenarAscendente(a, b, c, d, e)
  descendente_f = OrdenarDescendente(a, b, c, d, e)
  potencia_f = CalcularPoteniaMayor(a, b, c, d, e)
  raizc_f = CalcularRaizCubica(a, b, c, d, e)
  print("----------------------------------------------------------------")
  print("El promedio es " + str(promedio_f))
  print("----------------------------------------------------------------")
  print("La mediana es " + str(mediana_f))
  print("----------------------------------------------------------------")
  print("El promedio multiplicativo es " + str(promediomultiplicativo_f))
  print("----------------------------------------------------------------")
  print("El orden ascencente es " + str(ascendente_f))
  print("----------------------------------------------------------------")
  print("El orden descedente es " + str(descendente_f))
  print("----------------------------------------------------------------")
  print("La potencia del mayor número elevado al menor número es " + str(potencia_f))
  print("----------------------------------------------------------------")
  print("La raíz cúbica de menor número es " + str(raizc_f))
```
**8.** Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.
* Para este punto primero creé un archivo en mi cpu dondé estaban solo las funciónes del punto 7 y lo añadí directamente como archivo en el que estaba haciendo para este punto. Luego haciendo uso de import, importé todas las funciones de este archivo para usarlas. En la función main se solicita ingresar los valores y se ejecutan las funciones.
* Mirar archivo Punto_8.py
```pseudocode
from funciones_punto_7 import CalcularPromedio
from funciones_punto_7 import CalcularMediana
from funciones_punto_7 import CalcularPromedioMultiplicativo
from funciones_punto_7 import OrdenarAscendente
from funciones_punto_7 import OrdenarDescendente
from funciones_punto_7 import CalcularPoteniaMayor
from funciones_punto_7 import CalcularRaizCubica

if __name__ == "__main__":
  a = float(input("Ingrese el primer numero:"))
  b = float(input("Ingrese el segundo numero:"))
  c = float(input("Ingrese el tercer numero:"))
  d = float(input("Ingrese el cuarto numero:"))
  e = float(input("Ingrese el quinto numero:"))
  promedio_f = CalcularPromedio(a, b, c, d, e)
  mediana_f = CalcularMediana(a, b, c, d, e)
  promediomultiplicativo_f = CalcularPromedioMultiplicativo(a, b, c, d, e)
  ascendente_f = OrdenarAscendente(a, b, c, d, e)
  descendente_f = OrdenarDescendente(a, b, c, d, e)
  potencia_f = CalcularPoteniaMayor(a, b, c, d, e)
  raizc_f = CalcularRaizCubica(a, b, c, d, e)
  print("----------------------------------------------------------------")
  print("El promedio es " + str(promedio_f))
  print("----------------------------------------------------------------")
  print("La mediana es " + str(mediana_f))
  print("----------------------------------------------------------------")
  print("El promedio multiplicativo es " + str(promediomultiplicativo_f))
  print("----------------------------------------------------------------")
  print("El orden ascencente es " + str(ascendente_f))
  print("----------------------------------------------------------------")
  print("El orden descedente es " + str(descendente_f))
  print("----------------------------------------------------------------")
  print("La potencia del mayor número elevado al menor número es " + str(potencia_f))
  print("----------------------------------------------------------------")
  print("La raíz cúbica de menor número es " + str(raizc_f))
```
**9.** Consultar qué es y cómo funciona pip en python.
* "PIP" es el acrónimo de «Pip Installs Packages» y es una herramienta muy útil para instalar, actualizar, eliminar y buscar paquetes de Python. Es decir, es el instalador y administrador de paquetes de Python. Se usa para descargar una librería que no teníamos antes o para actualizar la librería a una nueva versión. Este comando se utiliza desde la terminal o la consola. Funciona escribiendo: "pip <comando> <operación>", en <comando> se pueden escribir comandos como: install, download, uninstall, list dependiendo de la acción que se quiera realizar.

Fuente:
- [https://es.linkedin.com/learning/python-esencial-15349768/instalacion-de-paquetes-con-pip#:~:text=pip%20es%20el%20instalador%20y,desde%20la%20shell%20de%20Python.](https://docs.python.org/es/3.11/installing/index.html)
- https://geekland.eu/como-instalar-y-usar-el-gestor-de-paquetes-pip/#:~:text=Pip%20es%20un%20gestor%20de%20paquetes%20utilizado%20para%20instalar%20y,y%20buscar%20paquetes%20de%20Python.

**10.** Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.
| # | Módulo | Instalación | Uso |
|---|--------|-------------|-----|
| 1 |  NumPy | *pip install numpy* | Es una biblioteca para la programación numérica en Python. |
| 2 |  Pandas | *pip install pandas* | Es una biblioteca de análisis de datos que proporciona estructuras de datos y herramientas de análisis. |
| 3 |  Matplotlib | *pip install matplotlib* | Es una biblioteca para crear gráficos y visualizaciones en Python. |
| 4 |  Requests | *pip install requests* | Es una biblioteca HTTP que permite realizar solicitudes HTTP en Python de manera sencilla. |
| 5 |  Scikit-Learn | *pip install scikit-learn* | Es una biblioteca de aprendizaje automático (machine learning) que proporciona herramientas para la clasificación, regresión, clustering, etc. |
| 6 |  Django | *pip install Django* | Es un framework web de alto nivel que facilita la creación de aplicaciones web robustas y escalables en Python. |
| 7 |  Flask | *pip install Flask* | Es un microframework web que es simple y fácil de usar para construir aplicaciones web en Python. |
| 8 |  Beautiful Soup | *pip install beautifulsoup4* | Es una biblioteca para extraer datos de páginas web y analizar documentos HTML y XML. |
| 9 |  TensorFlow | *pip install tensorflow* | Es una biblioteca de código abierto para machine learning y deep learning desarrollada por Google. |
| 10 |  PyTorch | *pip install torch* | Es otra biblioteca de machine learning y deep learning, desarrollada por Facebook's AI Research lab. |
