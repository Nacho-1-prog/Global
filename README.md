<h1 align="center"> Global de Python </h1>

<h2 align="center"> Programación 1 comisión 4 - UTN - Mendoza </h2>

<ins>**Integrantes:**</ins>
  * Aguilar Tiago Ignacio
  * Baggio Miguel Josué
  * Castro Marcos Nicolás
  * Osorio Alejo Marcelino

<ins>**Ejecucion del programa:**</ins>
1. Clonar el [repositorio](https://github.com/GrupoPython-9/Global) en tu máquina local.
2. Ejecutar el archivo "ejecutable.py".
3. Ingresar la matriz de ADN.
4. Seleccionar las opciones que desee ejecutar.

<ins>**Introduccion del programa:**</ins>

El programa consiste en tomar una secuencia de ADN la cual cuenta con cuatro bases nitrogenadas:
  * Adenina **(A)**
  * Timina **(T)**
  * Citosina **(C)**
  * Guanina **(G)**

La misma se puede representar en una matriz de 6x6. Para la realizacion del programa se utilizo una lista, donde cada String equivale a una fila de la matriz. Por ejemplo:

> matriz = ["AGATCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]

El problema consiste en que cuando cuatro bases nitrogenadas iguales se encuentran de manera consecutiva, ya sea de forma horizontal, vertical o diagonal. Esa matriz de ADN se considera que posee una mutacion.

Cuenta con diferentes clases. Cada una con un funcionamiento distinto. Las cuales son:
  * Detector: Detecta presencia de mutaciones
  * Mutador: Realiza mutaciones
    * Radiacion: Realiza mutaciones de manera horizontal o vertical
    * Virus: Realiza mutaciones de manera diagonal
  * Sanador: Genera una nueva matriz sin mutaciones en caso que este mutada.

Durante la ejecucion del programa, el usuario ingresara una matriz de ADN. Al finalizar, se imprimira un menu con distintas opciones. Ahi el usuario selecciona la que desee.

<ins>**Entradas y salidas esperadas**</ins>

El ejecutar el programa se le pedira que ingrese la secuencia de ADN, con una breve introduccion de como debe ser. 
Para guiar al usuario se va ingresando fila por fila, comenzando por la fila 1 hasta la fila 6.

Entrada (inputs):
* _Fila 1:_ **AGATCA**
* _Fila 2:_ **GATTCA**
* _Fila 3:_ **CAACAT**
* _Fila 4:_ **GAGCTA**
* _Fila 5:_ **ATTGCG**
* _Fila 6:_ **CTGTTC**

En caso que se ingrese una base nitrogenada que no este entre A, C, G o T; y se ingrese un número mayor o menor que las 6 permitidas. Se le notifica al usuario que ingrese una secuencia permitida

> Secuencia no permitida. Debe tener solo 6 bases nitrogenadas (A, T, G y C)

Terminados los inputs. Se imprime por pantalla un menu con diferentes opciones:

1. Detectar mutaciones
2. Crear mutacion
4. Sanar mutaciones
5. Mostrar matriz actual
6. Salir

<ins>Desglose del menu de opciones</ins>

* Detectar mutaciones
  * Recorre la matriz de ADN en busca de cuatro bases nitrogenadas iguales de manera consecutiva.
  * Si encuentra devuelve un "True" junto con un mensaje. Caso contrario, devuelve un "False" con un mensaje.
 
* Crear mutacion
  * Entrada (inputs): 2
  * Al seleccionar la opcion, se habilita otro menu con 2 opciones.
    
    * Entrada (inputs): 1
      * Radiacion: Es un tipo de mutacion que genera mutaciones de manera horizontal o vertical.
        * Entradas (inputs):
      
          En este caso se debe ingresar la base que desea mutar (Agregarla 4 veces en la secuencia de ADN)
          * _Selecciones una base nitrogenada (A/T/C/G):_ **T**

          Luego, se pregunta desde donde comenzaria la mutacion, empezando por la fila (desde la fila 0 hasta la 5).
          * _Fila en la cual inicie la mutacion (0-5):_ **0**

          Seguido de la columna inicial (Desde la columna 0 hasta la 5)
          * _Columna en la cual inicie la mutacion (0-5):_ **5**
     
          Finalmente la orientacion, como la Radiacion puede generarlos de manera horizontal **(H)** o vertical **(V)**, se le pide que se ingrese la inicial
          * _Orientacion de la mutacion, Horizontal (H) o Vertical (V), ingrese la inicial:_ **H**
        * Salida (outputs):
      
               Matriz con la nueva mutacion
      
              AGTTTT
              GATTCA
              CAACAT
              GAGCTA
              ATTGCG
              CTGTTC
      
               Se completo la mutacion correctamente
      
    * Entrada (inputs): 2
      * Virus: Es un tipo de mutacion que genera mutaciones de manera diagonal.
        * Entradas (inputs)
      
          En este caso se debe ingresar la base que desea mutar (Agregarla 4 veces en la secuencia de ADN)
          * _Selecciones una base nitrogenada (A/T/C/G):_ **T**

          Luego, se pregunta desde donde comenzaria la mutacion, empezando por la fila (desde la fila 0 hasta la 5).
          * _Fila en la cual inicie la mutacion (0-5):_ **0**

          Seguido de la columna inicial (Desde la columna 0 hasta la 5)
          * _Columna en la cual inicie la mutacion (0-5):_ **5**
     
          Finalmente, como solo tiene una direccion no se ingresa una orientacion
      * Salida (outputs):

             Matriz con la nueva mutacion
    
               AGTTTT
               GATTTA
               CAATAT
               GATCTA
               ATTGCG
               CTGTTC
    
            Se completo la mutacion correctamente

* Sanar mutaciones
  * Si presenta mutaciones. Se genera una nueva matriz de ADN aleatoriamente sin mutaciones.
    * Entrada (inputs): 3
    * Salida (outputs):
      
          Matriz Sanada
      
            TATGCG
            GCCCAC
            GCGTCG
            GGTGGG
            CCTGTC
            GATTCA
      
          Felicidades, su matriz de ADN ya no presenta mutaciones.

  * Si no presenta mutaciones. Se imprime por pantalla.
    * Entrada (inputs): 3
    * Salida (outputs):
      
          La matriz ya esta sanada.
          Matriz Sanada
      
              TATGCG
              GCCCAC
              GCGTCG
              GGTGGG
              CCTGTC
              GATTCA
      
          Felicidades, su matriz de ADN ya no presenta mutaciones.

* Mostrar matriz actual: Imprime por pantalla la matriz con la cual se esta trabajando.
  * Entrada (inputs): 4
  * Salida (outputs):

          Matriz actual
    
              TATGCG
              GCCCAC
              GCGTCG
              GGTGGG
              CCTGTC
              GATTCA

* Por ultimo "Salir": Termina la ejecucion del programa". Imprimiendo un mensaje al finalizar.
  * Entrada (inputs): 5
  * Salida (outputs):
      _Gracias por utilizar el programa. Vuelva pronto._
