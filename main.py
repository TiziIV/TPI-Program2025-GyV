#Programa principal

import funciones #Importa el archivo de funciones.

lista_paises = funciones.cargar_csv("paises.csv") #Llama a la funcion cargar_csv para cargar los datos dentro del main

if lista_paises:
    print(f"\n--- Se cargaron {len(lista_paises)} países exitosamente ---")  #Verifica si se cargo correcamente y se informa al usuario.
else:
    print("\nNo se pudieron cargar los datos. Saliendo del programa...")

while True: #Usa bucle while para desplegar el menu y que el usuario elija la opcion que quiere.
    funciones.mostrar_menu()

    # Se reemplaza el try except original por la nueva función de validación
    opcion = funciones._solicitar_entero_rango("\nPor favor, ingrese una opción: ", 0, 6)

    match opcion:
        case 1:
            funciones.buscar_pais(lista_paises) #Si el usuario elije 1, busca el pais por nombre, llamando la funcion buscar_pais.
        case 2:    
            funciones.filtrar_continente(lista_paises)
        case 3:
            funciones.filtrar_superficie_poblacion(lista_paises, opcion)
        case 4:
            funciones.filtrar_superficie_poblacion(lista_paises, opcion)
        case 5:
            funciones.ordenar_paises(lista_paises)
        case 6:
            funciones.menu_estadisticas(lista_paises)
        case 0:
            print("\nSaliendo del programa.")
            break
        