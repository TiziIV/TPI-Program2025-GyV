#Programa principal

import csv

with open("paieses.csv","r") as archivo:
    contenido = archivo.read()
    print(contenido)

import funciones

decision = 1
while decision != 0:
    
    funciones.mostrar_menu()
    
    decision = input("Por favor, ingrese una opción: ")

