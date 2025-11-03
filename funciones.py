#Funcion mostrar menu.
import time
import csv

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
    time.sleep(1)
    print(f"\n  ------------------------------")
    print(f"  Nombre:     {pais['nombre']}")
    # f"{pais['poblacion']:,}" agrega comas como separadores de miles
    print(f"  Población:  {pais['poblacion']:,}")
    print(f"  Superficie: {pais['superficie']:,} km²")
    print(f"  Continente: {pais['continente']}")
    print(f"  ------------------------------")

#Funcion cargar datos desde CSV

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
    
    if not busqueda:
        print("Error: No ingresó un término de búsqueda.")
        return
    
    busqueda_lower = busqueda.lower() #Cambia a minusculas para busarlo en la lista.

    pais_encontrado = []#Define que todavia no encuentra ningun pais que coincida.

    for pais in lista_paises: #Recorre la lista de paies, elemento por elemento.
        nombre_pais_lower = pais["nombre"].lower() #Cambia a minusculas el pais de la lista para luego compararlo.

        if busqueda_lower in nombre_pais_lower: # Compara el pais con el pais buscado.
            pais_encontrado.append(pais) # Si lo encuentra le asigna el diccionario de ese pais para mostrar luego los datos.
    
    if pais_encontrado: # Si pais_encontrado tiene algun elemento hace lo siguiente.
        print(f"\nSe ha encontrado {len(pais_encontrado)} resultado para la busqueda de {busqueda}...")
        for pais in pais_encontrado:
            _mostrar_pais(pais) #Llama a la funcion mostrar pais para mostrar los datos del pais ordenadamente.

    else:
        print(f"\nNo se encontro ningun resultado para {busqueda}") #Si no lo encuentra muestra el mensaje.

#Funcion Filtrar continente.

def filtrar_continente(lista_paises):
    print("\n2 - Filtrar paises por continente.")

    continentes_disponibles = set() #Crea un set con los continentes disponibles, ya que elimina duplicados.
    
    for pais in lista_paises: #Recorre la lista de paises, y añande todos los continentes disponibles al set.
        continentes_disponibles.add(pais["continente"])
    
    print(f"\nContinentes disponibles en la lista: {', '.join(sorted(continentes_disponibles))}") 
    
    continente_buscado = input("\nPor favor, ingrese un continente de la lista: ").strip().capitalize() #Le pide al usuario que ingrese el continente a filtrar.

    if continente_buscado not in continentes_disponibles: #Si el continente buscado no esta en los disponibles indica que no se encuentro.
        print(f"\nEl continente {continente_buscado} no se encuentra en la lista. ")
        return
    
    paises_continente = [] #Crea la lista de paises del continente buscado, por ahora vacia.

    for pais in lista_paises: #Recorre la lista de paises pais por pais, compara el continente con el buscado y lo agrega a la lista si es necesario.
        if pais["continente"] == continente_buscado:
            paises_continente.append(pais)
    
    if paises_continente: #Si paises_continente contiene elementos indica cuantos se encontraron del continente buscado.
        print(f"\nSe han encontrado {len(paises_continente)} en {continente_buscado}...")
        for pais in paises_continente: #Recorre la lista para mostrar todos los paises y sus datos.
            _mostrar_pais(pais)
    else:
        print(f"\nNo se encontaron paises en {continente_buscado}") #Si la lista esta vacia indica que no se encontraron paises.

#Filtrar por poblacion y superficie

def filtrar_superficie_poblacion(lista_paises,opcion):
    if opcion == 3: #Verifica cual es la opcion que tiene que trabajar y le asigna el valor correspondiente a la variable.
        atributo = "poblacion"
    elif opcion == 4:
        atributo = "superficie"
    
    print(f"\n{opcion} - Filtrar paises por {atributo}.") 
    

    while True: 
        minimo = input(f"\nIngrese la {atributo} minima[EJ: 100000] [Vacio para 0]: ") 
        if not minimo:
            minimo = 0
            break
        try:
            minimo = int(minimo)
            break
        except ValueError:
            print(f"\nEl numero ingresado no es valido, vuelva a intentarlo...")
            continue

    while True:

        maximo = input(f"\nIngrese la {atributo} maxima [EJ: 5000000] [Vacio para sin limite]: ")
        valor_maximo = 9999999999999
        if not maximo:
            maximo = 9999999999999
            break
        try:
            maximo = int(maximo)
            break
        except ValueError:
            print("\nEl numero ingresado no es valido, vuelva a intentarlo...")
            continue

    if minimo>maximo:
        print(f"\nLa {atributo} minima no puede ser mayor a la {atributo} maxima.")
        return
    
    paises_encontrados = []
    
    for pais in lista_paises:
        if minimo <= pais[atributo] <= maximo:
            paises_encontrados.append(pais)
    if paises_encontrados:
        paises_encontrados = sorted(paises_encontrados, key=lambda pais: pais[atributo], reverse=True)
        if maximo == valor_maximo:
            maximo = "Sin limite"
        print(f"\nSe encontraron {len(paises_encontrados)} con {atributo} entre {minimo} y {maximo}")
        for pais in paises_encontrados:
            _mostrar_pais(pais)
    else:
        print(f"\nNo se encontraron paises en ese rango de {atributo}.")


#Funcion de ordenar.

def ordenar_paises(lista_paises): 
    print("\n5. Selecciona un criterio de Ordenamiento: \n"
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
        _mostrar_pais(pais)

def menu_estadisticas(lista_paises):

    print("\n---6. Menú de Estaditicas ---")
    print("1. Pais con Mayor y Menor población")
    print("2. Promedio de Población")
    print("3. Promedio superficie")
    print("4. Cantidad de Paises por continente")
    try:
        opcion=int(input("Ingrese que opción desea realizar: "))
    except ValueError:
        print("La opcion es invalida, ingrese un numero entre 1 y 4.")
        return
    match opcion:
        case 1:
            paises_mayor_menor(lista_paises)
        case 2:
            promedio_poblacion(lista_paises)
        case 3:
            promedio_superficie(lista_paises)
        case 4:
            paises_continetes(lista_paises)
        case _:
            print("Error: El valor ingresado no pertenece a la lista de opciones.")


def paises_mayor_menor(lista_paises):
    if not lista_paises:
        print("⚠️ La lista de países está vacía.")
        return
    paises_ordenados=sorted(lista_paises, key=lambda pais: pais['poblacion'])
    menor=paises_ordenados[0]
    mayor=paises_ordenados[-1]
    print(f"\nPais con Mayor población: ")
    _mostrar_pais(mayor)
    print(f"\nPais con Menor población: ")
    _mostrar_pais(menor)
    
def promedio_poblacion(lista_paises):
    if not lista_paises:
        print("\n⚠️ La lista de países está vacía.")
        return
    poblacion_total_mundial=sum(pais['poblacion'] for pais in lista_paises)
    cantidad_total_paises=len(lista_paises)
    promedio_paises=poblacion_total_mundial/cantidad_total_paises
    print(f"\nEl promedio de poblacion Mundial es de: {promedio_paises:,.0f} habitantes")

def promedio_superficie(lista_paises):
    if not lista_paises:
        print("\n⚠️ La lista de países está vacía.")
        return
    superficie_total_mundial=sum(pais['superficie'] for pais in lista_paises)
    cantidad_total_paises=len(lista_paises)
    promedio_superficie_mundial=superficie_total_mundial/cantidad_total_paises

    print(f"\nEl promedio de superficie Mundial es de: {promedio_superficie_mundial:,.0f} km²")

def paises_continetes(lista_paises):
    conteo_continentes = {}
    if not lista_paises:
        print("No hay paises cargados.")
        return
    for pais in lista_paises:
        continente = pais["continente"]
        if continente in conteo_continentes:
            conteo_continentes[continente] += 1
        else:
            conteo_continentes[continente] = 1
    print("\n---Conteo por Continente---")
    for continente, conteo in sorted(conteo_continentes.items()):
        print(f"{continente}: {conteo} países")
    
