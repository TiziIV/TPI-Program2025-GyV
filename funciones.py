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

#Funcion cargar datos desde CSV

import csv

def cargar_csv (nombre_archivo):
    lista_paises = []
    try:
        with open(nombre_archivo, mode="r", newline="") as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                try:
                    fila["poblacion"] =  int(fila["poblacion"])
                    fila["superficie"] = int(fila["superficie"])
                    lista_paises.append(fila)
                except ValueError:
                    print(f"Error: La fila para '{fila['nombre']}' tiene datos numéricos inválidos. Se omitirá.")
        return lista_paises
    except FileNotFoundError:
        print(f"Error: ¡No se encontró el archivo '{nombre_archivo}'!")
        return []
    except Exception as a:
        print(f"Error inesperado al leer el CSV: {a}")
        return []

