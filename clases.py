import random
class Detector:
    """
    Clase para detectar mutantes en una matriz de ADN.
        En un ADN se considera mutado cuando tiene 4 bases nitrogenadas de manera consecutiva. Diagonal, horizontal o vertical.

    Atributos:
        metodo (str): Nombre del metodo para detectar mutaciones.
        siglas (str): Siglas del metodo.
        nombre (str): Nombre del detector al instanciar un objeto.
        resultadoHorizontal (bool): Resultado del metodo de deteccion horizontal.
        resultadoVertical (bool): Resultado del metodo de deteccion vertical.
        resultadoDiagonal (bool): Resultado del metodo de deteccion diagonal.
        mutado (bool): Indica si hay presencia o no de mutaciones
    """
    metodo = "Polimorfismo de conformacion de cadena sencilla" 
    siglas = "SSCP"

    def __init__(self,nombre:str)->None:

        """
        Inicializar un nuevo detector.

        Parametros:
            nombre (str): El nombre del detector.
        """
        self.nombre = nombre
        self.resultadoHorizontal = None
        self.resultadoVertical = None 
        self.resultadoDiagonal = None
        self.mutado = False

    def detector_mutantes(self,matrizADN:list)->bool:

        """
        Detecta si hay mutaciones en la matriz de ADN.

        Parametros:
            matrizADN (list): Una lista ingresada por el usuario en representacion de la matriz de ADN.

        Retorna:
            bool: Si detecta una mutacion de alguno de los metodos, horizontal, vertical o diagonal, devuelve un True. Caso contrario False
        """
        resultadoHorizontal = self.detector_horizontal(matrizADN)
        resultadoVertical = self.detector_vertical(matrizADN)
        resultadoDiagonal = self.detector_diagonal(matrizADN)
        self.mutado= resultadoHorizontal or resultadoVertical or resultadoDiagonal
        return self.mutado
    
    def detector_horizontal(self, matrizADN:list)->bool:

        """
        Detecta mutaciones horizontales en la matriz de ADN.

        Recorre la lista, palabra por palabra, hasta encontrar una secuencia de 4 bases iguales.
        La funcion set junto con len para contar los caracteres unicos, devolviendo True cuando sea igual a 1 (1 base que se repite 4 veces)

        Parametros:
            matrizADN (list)
        
        Retorna:
            bool: si detecta una mutacion horizontal devuelve True, caso contrario False.
        """
        for fila in matrizADN:

            for i in range(len(fila) - 3):
                secuencia = fila[i:i+4]

                if len(set(secuencia)) == 1:
                    return True
        return False
    
    def detector_vertical(self, matrizADN:list)->bool:

        """
        Detecta mutaciones verticales en la matriz de ADN.

        Recorre las posiciones de las columnas. Luego recorre las filas de la columna. 
        Se resta 3 para asegurar que se puede obtener 4 bases consecutivas.
        Se forma una nueva lista secuencia utilizando las letras en una columna definida, iterando las distintas palabras. Hasta formar una secuencia de 4 bases.
        Se utiliza set junto con len para contar los caracteres unicos, devolviendo True cuando sea igual a 1

        Parametros:
            matrizADN (list)
        
        Retorna:
            bool: si detecta una mutacion vertical devuelve True, caso contrario False.
        """
        
        for i in range(len(matrizADN[0])):  

            for j in range(len(matrizADN) - 3):
                secuencia = [matrizADN[j+k][i] for k in range(4)]

                if len(set(secuencia)) == 1: 
                    return True  
        return False
    
    def detector_diagonal(self, matrizADN:list)->bool:

        """
        Detecta mutaciones de manera diagonal en la matriz de ADN.
        
        Verificar diagonales descendentes (de izquierda a derecha). Recorre las filas de 0 a 3.
        Luego, recorre las columnas comprobando la secuencia diagonal descendente.
        Crea una lista en fragmentoADN iterando la matriz.
        Finalmente se compara con la funcion set junto con len para comprobar que sean 4 secuencias iguales.

        Parametros:
            matrizADN (list)
        
        Retorna:
            bool: si detecta una mutacion diagonal devuelve True, caso contrario False.
        """
        filas = len(matrizADN)
        columnas = len(matrizADN[0])
        secuencia = 4  # Número de letras consecutivas que estamos buscando

        # Verificar diagonales descendentes (de izquierda a derecha)
        for i in range(filas - secuencia + 1):  # Iteramos sobre las filas range(0,3), filas - secuencia = 2, luego se suma 1 = 3
            for j in range(columnas - secuencia + 1):  # Iteramos sobre las columnas
            # Comprobamos la secuencia diagonal descendente
                fragmentoADN = [matrizADN[i+k][j+k] for k in range(secuencia)]
                if len(set(fragmentoADN)) == 1:
                    return True

        # Verificar diagonales ascendentes (de abajo hacia arriba)
        for i in range(secuencia - 1, filas):  # Comenzamos desde la fila inferior range(3,6)-(3,4,5)
            for j in range(columnas - secuencia + 1):  # Iteramos sobre las columnas
            # Comprobamos la secuencia diagonal ascendente
                fragmentoADN = [matrizADN[i-k][j+k] for k in range(secuencia)]
                if len(set(fragmentoADN)) == 1:
                    return True

        return False
    
class Mutador:
    
    """
    Clase base para los mutadores de ADN.
    
    Atributos:
        base_nitrogenada (str): Base nitrogenada que se usara para la mutacion.
        mutacion (str): Nombre de la mutacion que se implementara.
        intensidad (str): Grado de intensidad de la mutacion.
    """
    def __init__(self, base_nitrogenada: str, mutacion: str, intensidad: str)->None:

        """
        Inicializa un nuevo mutador.

        Parametros:
            base_nitrogenada (str): Base nitrogenada que se usara para la mutacion.
            mutacion (str): Nombre de la mutacion que se implementara.
            intensidad (str): Grado de intensidad de la mutacion.
        """
        self.base_nitrogenada = base_nitrogenada.strip().upper()
        self.mutacion = mutacion
        self.intensidad = intensidad
    def crear_mutante():
        """
        Crea un mutante en la matriz de ADN.
        
        Metodo vacio que implementan las clases hijas
        """
        pass

class Radiacion(Mutador):
    
    """
    Clase que representa un mutador por radiacion. 

    Hereda de la clase Mutador y realiza mutaciones de manera horizontal y vertical.

    Metodos:
        crear_mutante
        mutacion_horizontal
        mutacion_vertical
            
    """
    def __init__(self,base_nitrogenada:str,mutacion:str,intensidad:str)->None:

        """
        Inicializa un mutador de radiacion.

        Parametros:
            base_nitrogenada (str): Base nitrogenada que se usara para la mutacion.
            mutacion (str): Nombre de la mutacion que se implementara.
            intensidad (str): Grado de intensidad de la mutacion.
        """
        super().__init__(base_nitrogenada,mutacion,intensidad)

    def crear_mutante(self, base_nitrogenada:str, posicion_inicial:list, orientacion_de_la_mutacion:str,matrizADN:list):
        
        """
        Crea una mutacion en la matriz de ADN, horizontal o vertical.

        Primero hace una validacion de los parametros.
        Pasada la validacion se llama al metodo correspondiente.

        Parametros:
            base_nitrogenada (str): base nitrogenada que se desea agregar 4 veces.
            posicion_inicial (list): Punto inicial de donde se comenzaria la mutacion (fila, columna).
            orientacion_de_la_mutacion (str): Orientacion de la mutacion, puede ser "H"(horizontal) o "V"(vertical).
            matrizADN: La matriz de ADN a modificar.

        Retorna:
            Matriz de ADN (list) modificada con la mutacion.
        """
        self.base_nitrogenada = base_nitrogenada.strip().upper()
        self.orientacion_de_la_mutacion=orientacion_de_la_mutacion.strip().upper()
        self.fila_inicial, self.columna_inicial = posicion_inicial #De una lista, desglosa en 2 variables
        print(f"Posición inicial: {self.fila_inicial}, {self.columna_inicial}")
        print(f"Orientación: {self.orientacion_de_la_mutacion}")
        while True:
            try:
                #Comprobar si la posicion esta fuera del rango
                if self.fila_inicial >= len(matrizADN) or self.columna_inicial >= len(matrizADN[0]):
                    raise IndexError("La posicion elegida se encuentra fuera de la cadena de ADN")
               #Verificar que tenga 2 elementos
                elif len(posicion_inicial) != 2:
                    raise ValueError("Para mutar se debe tener solo 2 numeros")
                #Verificar que sea H o V
                elif self.orientacion_de_la_mutacion not in ["H","V"]:
                    raise IndexError("Direccion no valida")
               # Verificar la base nitrogenada
                elif self.base_nitrogenada not in ["A","C","G","T"]:
                    raise ValueError("Base nitrogenada no valida")
                
                self.mutacion_horizontal(self.base_nitrogenada,matrizADN)
                self.mutacion_vertical(self.base_nitrogenada,matrizADN)

                return matrizADN
                
            except (IndexError, ValueError) as e:
                print("Intente nuevamente, error", e)
                break

    def mutacion_horizontal (self, base_nitrogenada:str,matrizADN:list):

        """
        Realiza la mutacion horizontal.

        Si la columna inicial se encuentra en los valores de 0 a 2, la mutacion se aplica de izquierda a derecha.
        Si la columna inicial se encuentra en los valores de 3 a 5, la mutacion se aplica de derecha a izquierda.

        Parametros:
            base_nitrogenada (str): Base nitrogenada que se agrega 4 veces.
            matrizADN (list): Matriz de ADN a modificar.
        """
        if (self.orientacion_de_la_mutacion == "H") and (self.columna_inicial in [0,1,2]):       
            for i in range(self.columna_inicial,self.columna_inicial+4):
                secuencia_ADN = list(matrizADN[self.fila_inicial])
                secuencia_ADN[i] = base_nitrogenada
                matrizADN[self.fila_inicial] = ''.join(secuencia_ADN)
        elif (self.orientacion_de_la_mutacion == "H") and (self.columna_inicial in [3,4,5]):
            for i in range(self.columna_inicial,self.columna_inicial-4,-1): #iria del n° columna, de manera inversa, como el ultimo valor no lo cuenta llegaria hasta -1 (sin contarlo)
                secuencia_ADN = list(matrizADN[self.fila_inicial])
                secuencia_ADN[i] = base_nitrogenada
                matrizADN[self.fila_inicial] = ''.join(secuencia_ADN)

    def mutacion_vertical (self, base_nitrogenada:str,matrizADN:list):

        """
        Realiza la mustacion horizontal.

        Si la fila inicial se encuentra en los valores de 0 a 2, la mutacion se aplica de arriba hacia abajo.
        Si la fila inicial se encuentra en lso valores de 3 a 5, la mutacion se aplica de abajo hacia arriba.

        Parametros:
            base_nitrogenada (str): Base nitrogenada que se agrega 4 veces.
            matrizADN (list): Matriz de ADN a modificar.
        """
        if (self.orientacion_de_la_mutacion == "V") and (self.fila_inicial in [0,1,2]):
            for i in range(self.fila_inicial, self.fila_inicial+4):
                secuencia_ADN = list (matrizADN[i])
                secuencia_ADN[self.columna_inicial] = base_nitrogenada
                matrizADN[i] = ''.join(secuencia_ADN)

        elif (self.orientacion_de_la_mutacion == "V") and (self.fila_inicial in [3,4,5]):
            for i in range(self.fila_inicial, self.fila_inicial -4 , -1):
                secuencia_ADN = list (matrizADN[i])
                secuencia_ADN[self.columna_inicial] = base_nitrogenada
                matrizADN[i] = ''.join(secuencia_ADN)

class Virus (Mutador):
    
    """
    Clase que representa un mutador de tipo Virus.

    Hereda de la clase Mutador y realiza mutaciones de manera diagonal.

    Metodos:
        crear_mutante
        mutacion_diagonal
        
    """
    def __init__(self, base_nitrogenada: str, mutacion:str, intensidad:str)->None:

        """
        Inicializa un mutador viral.

        Parametros:
            base_nitrogenada (str): Base nitrogenada que se usara para la mutacion.
            mutacion (str): Nombre de la mutacion que se implementara.
            intensidad (str): Grado de intensidad de la mutacion.
        """
        super().__init__(base_nitrogenada, mutacion,intensidad)

    def crear_mutante(self,base_nitrogenada:str, posicion_inicial:list, matrizADN:list):

        """
         Crea una mutacion en la matriz de ADN, diagonalmente.

        Primero hace una validacion de los parametros.
        Pasada la validacion se llama al metodo correspondiente.

        Parametros:
            base_nitrogenada (str): base nitrogenada que se desea agregar 4 veces.
            posicion_inicial (list): Punto inicial de donde se comenzaria la mutacion (fila, columna).
            orientacion_de_la_mutacion (str): Orientacion de la mutacion, puede ser "H"(horizontal) o "V"(vertical).
            matrizADN: La matriz de ADN a modificar.

        Retorna:
            Matriz de ADN (list) modificada con la mutacion.
        """
        self.base_nitrogenada = base_nitrogenada.strip().upper()
        self.fila_inicial, self.columna_inicial = posicion_inicial #De una lista, desglosa en 2 variables
        
        while True:
            try:
                #Comprobar si la posicion esta fuera del rango
                if self.fila_inicial >= len(matrizADN) or self.columna_inicial >= len(matrizADN[0]):
                    raise IndexError("La posicion elegida se encuentra fuera de la cadena de ADN")
               #Verificar que tenga 2 elementos
                elif len(posicion_inicial) != 2:
                    raise ValueError("Para mutar se debe tener solo 2 numeros")
                # Verificar la base nitrogenada
                elif self.base_nitrogenada not in ["A","C","G","T"]:
                    raise ValueError("Base nitrogenada no valida")

                self.mutacion_diagonal(self.base_nitrogenada,matrizADN)

                return matrizADN
                
            except (IndexError, ValueError) as e:
                print("Intente nuevamente, error", e)
                break
        
    def mutacion_diagonal (self, base_nitrogenada:str, matrizADN:list):

        """
        Realiza la mutacion de manera diagonal.

        Si la fila y la columna van de 0 a 2. Se crea la mutacion de izquierda a derecha, de arriba hacia abajo.
        Si la fila va de 0 a 2 y la columna de 3 a 5. Se crea la mutacion de derecha a izquierda, de arriba hacia abajo.
        Si la fila va de 3 a 5 y la columna de 0 a 2. Se crea la mutacion de izquierda a derecha, de abajo hacia arriba.
        Si la fila y la columna van de 3 a 5. Se crea la mutacion de derecha a izquierda, de abajo hacia arriba.

        Parametros:
            base_nitrogenada (str): Base nitrogenada que se agrega 4 veces.
            matrizADN (list): Matriz de ADN a modificar.
        """
        if (self.fila_inicial in [0,1,2]) and (self.columna_inicial in [0,1,2]): 
            for i in range(self.fila_inicial, self.fila_inicial +4):
                secuencia_ADN = list(matrizADN[i])
                secuencia_ADN[self.columna_inicial] = base_nitrogenada
                matrizADN[i] = ''.join(secuencia_ADN)
                self.columna_inicial += 1

        elif (self.fila_inicial in [0,1,2]) and (self.columna_inicial in [3,4,5]):
            for i in range(self.fila_inicial, self.fila_inicial +4):
                secuencia_ADN = list(matrizADN[i])
                secuencia_ADN[self.columna_inicial] = base_nitrogenada
                matrizADN[i] = ''.join(secuencia_ADN)
                self.columna_inicial -= 1

        elif (self.fila_inicial in [3,4,5]) and (self.columna_inicial in [0,1,2]): 
            for i in range(self.fila_inicial, self.fila_inicial -4 , -1):
                secuencia_ADN = list(matrizADN[i])
                secuencia_ADN[self.columna_inicial] = base_nitrogenada
                matrizADN[i] = ''.join(secuencia_ADN)
                self.columna_inicial += 1

        elif (self.fila_inicial in [3,4,5]) and (self.columna_inicial in [3,4,5]): 
            for i in range(self.fila_inicial, self.fila_inicial -4 , -1):
                secuencia_ADN = list(matrizADN[i])
                secuencia_ADN[self.columna_inicial] = base_nitrogenada
                matrizADN[i] = ''.join(secuencia_ADN)
                self.columna_inicial -= 1
        

class Sanador(Detector):

    """
    Clase que representa un sanador de ADN.

    Hereda de la clase Detector el metodo detector_mutantes para detectar mutaciones.

    Metodos:
        sanar_mutantes
    """
    def __init__(self,nombre:str, metodo_sanacion:str)->None:

        """
        Inicializa un sanador.

        Parametros:
            nombre (str): El nombre correspondiente del sanador.
            metodo_sanacion (str): El metodo para realizar la sanacion.
        """
        super().__init__(nombre)
        self.metodo_sanacion = metodo_sanacion

    def sanar_mutantes(self,matrizADN:list)->list:

        """
        Verifica si la matriz de ADN tiene o no mutaciones utilizando el metodo del Detector.
        Establecen las bases nitrogenadas permitidas.

        Si hay mutacion. Genera aleatoriamente una nueva matriz de ADN con las bases permitidas.
        Se detecta nuevamente si hay mutacion. Si es True genera nuevamente otra matriz

        Caso contrario retorna la matriz sanada

        Parametros:
            matrizADN (list): Matriz de ADN a sanar.

        Retorna:
            matriz_sanada (list): Matriz de ADN generada aleatoriamente sin mutaciones.
        """
        self.mutado = super().detector_mutantes(matrizADN)
        if not self.mutado:
            print("La matriz ya esta sanada.")
            
            return matrizADN
        
        bases_permitidas = ["C","T","A","G"]
        
        while self.mutado == True:
            matriz_sanada = [''.join(random.choice(bases_permitidas)for _ in range(6)) for _ in range(6)]
            self.mutado = super().detector_mutantes(matriz_sanada) 
            
            if self.mutado == False:
                return matriz_sanada