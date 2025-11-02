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
    print(f"\nCargando datos...")
    import time
    time.sleep(1)
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
    print("\n1 - Buscar país por nombre.") 
    busqueda = input("\nIngrese nombre del país que desea buscar: ").strip() #Le pide al usuario el pais que desea buscar.
    
    busqueda_lower = busqueda.lower() #Cambia a minusculas para busarlo en la lista.

    pais_encontrado = None #Define que todavia no encuentra ningun pais que coincida.

    for pais in lista_paises: #Recorre la lista de paies, elemento por elemento.
        nombre_pais_lower = pais["nombre"].lower() #Cambia a minusculas el pais de la lista para luego compararlo.

        if nombre_pais_lower == busqueda_lower: #Compara el pais con el pais buscado.
            pais_encontrado = pais #Si lo encuentra le asigna el diccionario de ese pais para mostrar luego los datos.
            break
    
    if pais_encontrado: #Si pais_encontrado tiene algun elemento hace lo siguiente.
        print(f"\nSe ha encontrado 1 resultado para la busqueda de {busqueda}...")
        
        _mostrar_pais(pais_encontrado) #Llama a la funcion mostrar pais para mostrar los datos del pais ordenadamente.

    else:
        print(f"\nNo se encontro ningun resultado para {busqueda}") #Si no lo encuentra muestra el mensaje.

#Funcion ordenar pais.

def ordenar_paises(lista_paises): 
    print("\nSelecciona un criterio de Ordenamiento: \n"
          "A. Nombre\n"
          "B. Población\n"
          "C. Superficie")
    criterio = input("Ingrese la Opción a elegir (A/B/C): ").upper().strip() # Permitimos al usuario Ingresar el criterio

    match criterio:
        case "A":
            opcion = 'nombre'
        case "B":
            opcion = 'poblacion'
        case "C":
            opcion = 'superficie'
        case _:
            print(f"\n Error: La opción '{criterio}' no es válida.")
            return  # corta la función

    print(f"\nOrdenando por: {opcion}...\n")
    import time
    time.sleep(1)

    # Usa sorted() según el criterio
    # En caso de elegir la opcion nombre o población se ordena utilizando Sorted(Funciona para ordenar diccionarios)
    # Y key=lambda devuelve el valor 
    if opcion == 'nombre': # Asignamos valor a la variable dependiendo del case
        paises_ordenados = sorted(lista_paises, key=lambda pais: pais['nombre'].lower())
    elif opcion == 'poblacion': # Asignamos valor a la opcion dependiendo del case
        paises_ordenados = sorted(lista_paises, key=lambda pais: pais['poblacion'])
    elif opcion == 'superficie': # Asignamos valor a la opcion dependiendo del case
    # Validamos que se ingrese bien Ascendente o Descendente
        while True:
            try:
                ascendente_descendente = int(input("\nDesea ordenar la superficie de manera:\n1. Ascendente\n2. Descendente\n👉 Opción: "))
                if ascendente_descendente not in (1, 2):
                    print("Error: opción fuera de rango. Intente nuevamente.")
                    continue  # Vuelve al inicio del while
                # Ordena según la opción
                if ascendente_descendente == 1:
                    paises_ordenados = sorted(lista_paises, key=lambda pais: pais['superficie'])
                elif ascendente_descendente == 2:
                    paises_ordenados = sorted(lista_paises, key=lambda pais: pais['superficie'], reverse=True)
                break  # Sale del while si todo está correcto
            except ValueError:
                print("Error: debe ingresar un número (1 o 2).")

    # Mostrar el resultado
    print(f"--- 🌍 Lista de países ordenada por {opcion} ---")
    for pais in paises_ordenados:
        print(f"{pais['nombre']:15} | Población: {pais['poblacion']:>10,} | Superficie: {pais['superficie']:>10,} km²")




    

        
    