from clases import Detector, Radiacion, Virus, Sanador

def obtener_matriz():
    print("""
Ingresa la secuencia de ADN:
    Bases nitrogenadas permitidas Adenina(A), Timina(T), Guanina(G) y Citocina(C)
    Debe tener 6 bases nitrogenadas cada fila
          """)
    matriz = []
    for i in range(6):
        while True:
            fila = input(f"Fila {i + 1}: ").strip().upper()
            if len(fila) == 6 and all(base in "ATCG" for base in fila):
                matriz.append(fila)
                break
            else:
                print("Secuencia no permitida. Debe tener solo 6 bases nitrogenadas (A, T, G y C)")
    return matriz

def obtener_entrada_mutacion():
    while True:
        try:
            tipo = input("Selecciona un tipo de mutacion (1 - Radiacion, 2 - Virus): " ).strip()
            if tipo not in ["1", "2"]:
                raise ValueError("Opcion no permitida. Intente nuevamente")
            
            base = input("Seleccione una base nitrogenada (A/T/C/G): ").strip().upper()
            if base not in "ATCG":
                raise ValueError("Base nitrogenada no permitida. Intente nuevamente")
            
            fila = int(input("Fila en la cual inicie la mutacion (0-5): ").strip())
            col = int(input("Columna en la cual inicie la mutacion (0-5): ").strip())
            if not (0 <= fila < 6 and 0 <= col < 6):
                raise ValueError("Las coordenadas deben estar en el rango de 0 a 5")
            
            if tipo == "1":
                orientacion = input("Orientacion de la mutacion, Horizontal (H) o Vertical (V), ingrese la inicial: ").strip().upper()
                if orientacion not in ["H", "V"]:
                    raise ValueError("Orientacion no permitida. Intente nuevamente")
                return tipo, base, fila, col, orientacion
            elif tipo == "2":
                return tipo, base, fila, col, None
        except ValueError as e:
            print(e)

def main():
    matriz = obtener_matriz()
    while True:
        print("""
------------------------------
Seleccione una opcion:
    1. Detectar mutaciones
    2. Crear mutacion
    3. Sanar mutaciones
    4. Mostrar matriz actual
    5. Salir    
            """)
       
    
        opcion = input("Opcion: ").strip()

        match opcion:
            case "1":
                detector = Detector("Detector de ADN")
                if detector.detector_mutantes(matriz):
                    print(detector.detector_mutantes(matriz))
                    print ("Se ha detectado una mutacion en la Matriz de ADN")
                else:
                    print(detector.detector_mutantes(matriz))
                    print("No se presentaron mutaciones.")
            case "2":
                tipo, base, fila, col, orientacion = obtener_entrada_mutacion()
                if tipo == "1":
                    radiacion = Radiacion(base, "Mutacion", "Alta")
                    matriz = radiacion.crear_mutante(base, [fila, col], orientacion, matriz)
                elif tipo == "2":
                    virus = Virus(base, "Mutacion", "Alta")
                    matriz = virus.crear_mutante(base, [fila, col], matriz)
                    
                print("\nMatriz con la nueva mutacion ")
                for fila in matriz:
                    print(f"\t{fila}")
                print("Se completo la mutacion correctamente")
            case "3":
                sanador = Sanador("Sanador de ADN", "Regeneracion")
                matriz = sanador.sanar_mutantes(matriz)
                print("Matriz Sanada ")
                for fila in matriz:
                   print(f"\t{fila}")
                print("Felicidades, su matriz de ADN ya no presenta mutaciones.")
            case "4":
                print("Matriz actual")
                for fila in matriz:
                    print(f"\t{fila}")
            case "5":
                print("Gracias por utilziar el programa. Vuelva pronto.")
                
                break
            case _:
                print("Por favor seleccione una de las opciones validas.")

if __name__ == "__main__":
    main()