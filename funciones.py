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

def _solicitar_texto_no_vacio(mensaje):
    while True:
        texto_ingresado = input(mensaje).strip()
        if texto_ingresado:
            return texto_ingresado
        else:
            print("Error: La entrada no puede estar vacía. Intente de nuevo.")

def _solicitar_entero_rango(mensaje, rango_minimo, rango_maximo):
    while True:
        try:
            opcion_ingresada = int(input(mensaje))
            if rango_minimo <= opcion_ingresada <= rango_maximo:
                return opcion_ingresada
            else:
                print(f"Error: La opción debe estar entre {rango_minimo} y {rango_maximo}.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido. Intente de nuevo.")

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
    busqueda = _solicitar_texto_no_vacio("\nIngrese nombre del país que desea buscar: ") #Le pide al usuario el pais que desea buscar.
    
    # El if not busqueda: original se elimina porque la función ya lo valida.
    
    busqueda_lower = busqueda.lower() #Cambia a minusculas para busarlo en la lista.

    pais_encontrado = []# Define que todavia no encuentra ningun pais que coincida.

    for pais in lista_paises: # Recorre la lista de paies, elemento por elemento.
        nombre_pais_lower = pais["nombre"].lower() # Cambia a minusculas el pais de la lista para luego compararlo.

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
    
    continente_buscado = _solicitar_texto_no_vacio("\nPor favor, ingrese un continente de la lista: ").strip().capitalize() #Le pide al usuario que ingrese el continente a filtrar.

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
    
    # Inicia un bucle infinito para solicitar el valor mínimo.
    while True: 
        # Pide al usuario el valor mínimo, indicando que vacío significa 0.
        minimo = input(f"\nIngrese la {atributo} minima[EJ: 100000] [Vacio para 0]: ") 
        # Si la entrada está vacía (el usuario solo presionó Enter)...
        if not minimo:
            minimo = 0 # Asigna 0 como valor mínimo.
            break # Sale del bucle while True.
        try:
            # Intenta convertir el valor ingresado a un número entero.
            minimo = int(minimo)
            
            # Verifica si el número es negativo
            if minimo < 0:
                print(f"\nError: El valor no puede ser negativo. Intente de nuevo.")
                continue # Vuelve al inicio del bucle para pedir el dato de nuevo.

            break # Si lo logra (y no es negativo), sale del bucle.
        except ValueError:
            # Si la conversión falla (ej. ingresó "hola"), muestra un error.
            print(f"\nEl numero ingresado no es valido, vuelva a intentarlo...")
            continue # Vuelve al inicio del bucle para pedir el dato de nuevo.

    # Inicia un bucle infinito para solicitar el valor máximo.
    while True:
        # Pide al usuario el valor máximo, indicando que vacío significa "sin límite".
        maximo = input(f"\nIngrese la {atributo} maxima [EJ: 5000000] [Vacio para sin limite]: ")
        # Define un valor numérico muy alto para representar "sin límite".
        valor_maximo = 9999999999999
        # Si la entrada está vacía
        if not maximo:
            maximo = 9999999999999 # Asigna el valor "sin límite".
            break # Sale del bucle.
        try:
            # Intenta convertir el valor ingresado a un número entero.
            maximo = int(maximo)
            
            # Verifica si el número es negativo
            if maximo < 0:
                print(f"\nError: El valor no puede ser negativo. Intente de nuevo.")
                continue # Vuelve al inicio del bucle para pedir el dato de nuevo.
            
            break # Si lo logra (y no es negativo), sale del bucle.
        except ValueError:
            # Si la conversión falla, muestra un error y vuelve a pedir.
            print("\nEl numero ingresado no es valido, vuelva a intentarlo...")
            continue

    # Comprueba que el rango sea lógico (mínimo no puede ser mayor que máximo).
    if minimo>maximo:
        print(f"\nLa {atributo} minima no puede ser mayor a la {atributo} maxima.")
        return # Termina la función si el rango es inválido.
    
    # Crea una lista vacía para almacenar los países que coincidan.
    paises_encontrados = []
    
    # Recorre la lista completa de países, uno por uno.
    for pais in lista_paises:
        # Comprueba si el atributo del país (población o superficie) está dentro del rango.
        if minimo <= pais[atributo] <= maximo:
            paises_encontrados.append(pais) # Si cumple, lo agrega a la lista de encontrados.
            
    # Después de revisar todos los países, comprueba si la lista de encontrados tiene algo.
    if paises_encontrados:
        # Ordena la lista de encontrados de mayor a menor (reverse=True).
        paises_encontrados = sorted(paises_encontrados, key=lambda pais: pais[atributo], reverse=True)
        
        # Si el valor de 'maximo' sigue siendo el número gigante, lo cambia por texto.
        if maximo == valor_maximo:
            maximo = "Sin limite"
            
        # Informa al usuario cuántos resultados se encontraron.
        print(f"\nSe encontraron {len(paises_encontrados)} con {atributo} entre {minimo:,} y {maximo:,}")
        # Recorre la lista de encontrados y muestra cada país format
        for pais in paises_encontrados:
            _mostrar_pais(pais)
    else:
        # Si la lista de encontrados está vacía, informa al usuario.
        print(f"\nNo se encontraron paises en ese rango de {atributo}.")


#Funcion de ordenar.

#Funcion de ordenar.

def ordenar_paises(lista_paises): 
    # Muestra al usuario las opciones de ordenamiento.
    print("\n5. Selecciona un criterio de Ordenamiento: \n"
        "A. Nombre\n"
        "B. Población\n"
        "C. Superficie")
    # Llama a la función de validación para obtener la opción (A, B o C).
    criterio = _solicitar_texto_no_vacio("Ingrese la Opción a elegir (A/B/C): ").upper().strip() # Permitimos al usuario Ingresar el criterio

    # Usa match-case para evaluar la opción elegida.
    match criterio:
        case "A":
            # Asigna la clave del diccionario 'nombre' a la variable 'opcion'.
            opcion = 'nombre'
        case "B":
            # Asigna la clave 'poblacion'.
            opcion = 'poblacion'
        case "C":
            # Asigna la clave 'superficie'.
            opcion = 'superficie'
        case _:
            # Si el usuario ingresa algo que no es A, B o C.
            print(f"\n Error: La opción '{criterio}' no es válida.")
            return  # corta la función
            
    # Informa al usuario por cuál criterio se está ordenando.
    print(f"\nOrdenando por: {opcion}...\n")
    time.sleep(1) # Pequeña pausa para simular carga.

    # Usa sorted() según el criterio
    # En caso de elegir la opcion nombre o población se ordena utilizando Sorted(Funciona para ordenar diccionarios)
    # Y key=lambda devuelve el valor 
    if opcion == 'nombre': # Asignamos valor a la variable dependiendo del case
        paises_ordenados = sorted(lista_paises, key=lambda pais: pais['nombre'].lower())
    elif opcion == 'poblacion': # Asignamos valor a la opcion dependiendo del case
        paises_ordenados = sorted(lista_paises, key=lambda pais: pais['poblacion'])
    elif opcion == 'superficie': # Asignamos valor a la opcion dependiendo del case
    # Validamos que se ingrese bien Ascendente o Descendente
        
        mensaje_orden = "\nDesea ordenar la superficie de manera:\n1. Ascendente\n2. Descendente\n👉 Opción: "
        ascendente_descendente = _solicitar_entero_rango(mensaje_orden, 1, 2)
        
        # El bloque 'while True' original se reemplaza por la línea anterior.
        if ascendente_descendente == 1:
            paises_ordenados = sorted(lista_paises, key=lambda pais: pais['superficie'])
        elif ascendente_descendente == 2:
            paises_ordenados = sorted(lista_paises, key=lambda pais: pais['superficie'], reverse=True)

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
        # Reemplazamos el input() original por la función de validación
        opcion=_solicitar_entero_rango("Ingrese que opción desea realizar: ", 1, 4)
    except ValueError:
        # Aunque _solicitar_entero_rango ya maneja esto, mantenemos la estructura original
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
    # Verifica si la lista está vacía antes de procesarla.
    if not lista_paises:
        print("⚠️ La lista de países está vacía.")
        return
    # Ordena la lista de países usando la población como criterio (de menor a mayor).
    paises_ordenados=sorted(lista_paises, key=lambda pais: pais['poblacion'])
    # El país con menor población es el primero de la lista ordenada.
    menor=paises_ordenados[0]
    # El país con mayor población es el último de la lista ordenada.
    mayor=paises_ordenados[-1]
    
    # Muestra los resultados llamando a la función de formato.
    print(f"\nPais con Mayor población: ")
    _mostrar_pais(mayor)
    print(f"\nPais con Menor población: ")
    _mostrar_pais(menor)
    
def promedio_poblacion(lista_paises):
    # Verifica si la lista está vacía.
    if not lista_paises:
        print("\n⚠️ La lista de países está vacía.")
        return
    # Suma la población de todos los países en la lista.
    # Se usa una expresión generadora para eficiencia.
    poblacion_total_mundial=sum(pais['poblacion'] for pais in lista_paises)
    # Obtiene la cantidad total de países para calcular el promedio.
    cantidad_total_paises=len(lista_paises)
    # Calcula el promedio.
    promedio_paises=poblacion_total_mundial/cantidad_total_paises
    # Muestra el resultado formateado (:, .0f) para añadir comas de miles y sin decimales.
    print(f"\nEl promedio de poblacion Mundial es de: {promedio_paises:,.0f} habitantes")

def promedio_superficie(lista_paises):
    # Verifica si la lista está vacía.
    if not lista_paises:
        print("\n⚠️ La lista de países está vacía.")
        return
    # Suma la superficie de todos los países en la lista.
    superficie_total_mundial=sum(pais['superficie'] for pais in lista_paises)
    # Obtiene la cantidad total de países.
    cantidad_total_paises=len(lista_paises)
    # Calcula el promedio de superficie.
    promedio_superficie_mundial=superficie_total_mundial/cantidad_total_paises

    # Muestra el resultado formateado.
    print(f"\nEl promedio de superficie Mundial es de: {promedio_superficie_mundial:,.0f} km²")

def paises_continetes(lista_paises):
    # Crea un diccionario vacío para almacenar el conteo.
    conteo_continentes = {}
    if not lista_paises:
        print("No hay paises cargados.")
        return
    # Recorre cada país de la lista.
    for pais in lista_paises:
        continente = pais["continente"]
        # Verifica si el continente ya es una clave en el diccionario.
        if continente in conteo_continentes:
            # Si existe, incrementa su contador en 1.
            conteo_continentes[continente] += 1
        else:
            # Si no existe, lo añade al diccionario con un valor inicial de 1.
            conteo_continentes[continente] = 1
            
    print("\n---Conteo por Continente---")
    # Muestra los resultados ordenados alfabéticamente por continente.
    for continente, conteo in sorted(conteo_continentes.items()):
        print(f"{continente}: {conteo} países")