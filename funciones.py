#Funcion mostrar menu.
def mostrar_menu():
    print("\n--- 🌍 Menú de Gestión de Países ---")
    print("1. Buscar país por nombre")
    print("2. Filtrar países por continente")
    print("3. Filtrar países por rango de población")
    print("4. Filtrar países por rango de superficie")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("0. Salir")

#Funcion Mostrar pais, la utiliza para cada vez que sea necesario mostrar un pais con el formato correcto.

def _mostrar_pais(pais):
    print(f"\n  ------------------------------")
    print(f"  Nombre:     {pais['nombre']}")
    # f"{pais['poblacion']:,}" agrega comas como separadores de miles
    print(f"  Población:  {pais['poblacion']:,}")
    print(f"  Superficie: {pais['superficie']:,} km²")
    print(f"  Continente: {pais['continente']}")
    print(f"  ------------------------------")

#Funcion cargar datos desde CSV

import csv

def cargar_csv (nombre_archivo):
    lista_paises = [] #Crea lista de paises vacias.
    try:
        with open(nombre_archivo, mode="r", newline="") as archivo: #Abre el archivo en modo lectura y utilizando newline para no modificar los saltos de linea.
            lector_csv = csv.DictReader(archivo) #Lee el archivo y cada fila la vuelve un diccionario.
            for fila in lector_csv: #Recorre los datos del archivo fila por fila
                try:
                    fila["poblacion"] =  int(fila["poblacion"]) #Intenta convertir los datos de superficie y poblacion en INT
                    fila["superficie"] = int(fila["superficie"])
                    lista_paises.append(fila) #Agrega la fila a la lista de diccionarios. 
                except ValueError:
                    print(f"Error: La fila para '{fila['nombre']}' tiene datos numéricos inválidos. Se omitirá.") #Si hay datos numericos erroneos arroja un error.
        return lista_paises
    except FileNotFoundError: #Si no encuentra el archivo tambien arroja un error.
        print(f"Error: ¡No se encontró el archivo '{nombre_archivo}'!")
        return []
    except Exception as a: #Si ocurre cualquier otro error arroja el siguiente mensaje indicando que algo esta fallando y el fallo tecnico que arroja Python.
        print(f"Error inesperado al leer el CSV: {a}")
        return []

#Funcion Buscar pais por nombre.

def buscar_pais(lista_paises):
    print("1 - Buscar país por nombre.")
    busqueda = input("Ingrese nombre del país que desea buscar: ").strip()
    
    busqueda_lower = busqueda.lower()

    pais_encontrado = None

    for pais in lista_paises:
        nombre_pais_lower = pais["nombre"].lower()

        if nombre_pais_lower == busqueda_lower:
            pais_encontrado = pais
            break
    
    if pais_encontrado:
        print(f"Se ha encontrado 1 resultado para la busqueda de {busqueda}")
        _mostrar_pais(pais_encontrado)

    else:
        print(f"No se encontro ningun resultado para {busqueda}")