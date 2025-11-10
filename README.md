# TPI - Gestión de Datos de Países (Programación 1 - UTN)

Este proyecto es el Trabajo Práctico Integrador (TPI) de la materia **Programación 1** de la **Tecnicatura Universitaria en Programación** de la UTN.

Programa funcional en Python 3.

## 📜 Descripción del Programa

Es una aplicación de consola desarrollada en Python que permite gestionar información sobre países. El sistema carga un conjunto de datos desde un archivo CSV y ofrece un menú interactivo para consultar y analizar la información. 

El objetivo principal es aplicar los conceptos de estructuras de datos (listas y diccionarios), modularización con funciones y técnicas de filtrado y ordenamiento aprendidas en la cursada.

## ✨ Características Principales

El menú de la aplicación permite realizar las siguientes operaciones:

* **Buscar un país por nombre:** Permite una búsqueda por coincidencia parcial o exacta.
* **Filtrar países por:**
    * Continente
    * Rango de población
    * Rango de superficie
* **Ordenar países por:**
    * Nombre
    * Población (ascendente o descendente)
    * Superficie (ascendente o descendente)
* **Mostrar estadísticas:**
    * País con mayor y menor población.
    * Promedio de población total.
    * Promedio de superficie total.
    * Cantidad de países por continente.

## 🚀 Instrucciones de Uso

1.  Clona este repositorio en tu máquina local:
    ```bash
    git clone [https://github.com/](https://github.com/)[TU_USUARIO]/[TU_REPOSITORIO].git
    ```
2.  Navega al directorio del proyecto:
    ```bash
    cd [NOMBRE_DE_TU_CARPETA_DEL_PROYECTO]
    ```
3.  Ejecuta el programa principal (asegúrate de tener Python 3.x instalado):
    ```bash
    python main.py
    ```
4.  Una vez en ejecución, el programa mostrará un menú en la consola. Ingresa el número de la opción deseada y presiona Enter.

## 📊 Dataset (paises.csv)

El programa utiliza un archivo `paises.csv` que debe estar en la misma carpeta que el script.

La estructura de datos de cada país en el CSV es:
`nombre,poblacion,superficie,continente`

**Ejemplo de registros:**

```csv
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

## 🖥️ Ejemplos de Entradas y Salidas

A continuación, se muestran capturas de pantalla de la ejecución del programa:

## 👥 Integrantes del Equipo
1. Juan Martin Garcia

2. Tiziano Valentini