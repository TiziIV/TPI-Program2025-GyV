#Programa principal

import funciones #Importa el archivo de funciones.

lista_paises = funciones.cargar_csv("paises.csv") #Llama a la funcion cargar_csv para cargar los datos dentro del main

if lista_paises:
    print(f"--- Se cargaron {len(lista_paises)} países exitosamente ---")  #Verifica si se cargo correcamente y se informa al usuario.
else:
    print("No se pudieron cargar los datos. Saliendo del programa...")

while True: #Usa bucle while para desplegar el menu y que el usuario elija la opcion que quiere.
    funciones.mostrar_menu()

    opcion = int(input("Por favor, ingrese una opción: ")) #Le pide al usuario la opcion del menu.

    if opcion == 1:
        funciones.buscar_pais(lista_paises) #Si el usuario elije 1, busca el pais por nombre, llamando la funcion buscar_pais.
    elif opcion == '2':    
        funciones.filtrar_continente(lista_paises)
    elif opcion == '3':
            funciones.filtrar_poblacion(lista_paises)
    elif opcion == '4':
            funciones.filtrar_superficie(lista_paises)
        
    elif opcion == '5':
            funciones.ordenar_paises(lista_paises)
        
    elif opcion == '6':
            funciones.mostrar_estadisticas(lista_paises)

    elif opcion == '0':
        print("\nSaliendo del programa.")
        break
        
    else:
            print("\n¡Opción no válida! Por favor, intente de nuevo.")