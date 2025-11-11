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
    git clone https://github.com/juanmagarciat/TPI-Program2025-GyV
    ```
2.  Navega al directorio del proyecto:
    ```bash
    cd TPI-Program2025-GyV
    ```
3.  Ejecuta el programa principal (asegúrate de tener Python 3.x instalado):
    ```bash
    python main.py
    ```
4.  Una vez en ejecución, el programa mostrará un menú en la consola. Ingresa el número de la opción deseada y presiona Enter.

## 🎬 Demostración en Video

Para ver el programa en acción y una demostración de todas las funcionalidades del menú, mira el siguiente video:

Recomendado visualizar con Google Vids

**▶️ Ver Demostración del TPI - Gestión de Datos de Países**
https://drive.google.com/file/d/1GKTtUucqyQ9-KB1kcp-NTYmPnM1EqdYQ/view?usp=drive_link


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
Menu de opciones:
### Menú de opciones
![Menu de opciones](https://github.com/user-attachments/assets/b48e9af2-a673-4f0b-88f2-2a560e4c4fdb)

### Coincidencia Exacta
![Coinicidencia Exacta](https://github.com/user-attachments/assets/4a4e8e6a-59b4-4a77-8ae4-da354ed30539)

### Coincidencia Parcial
![Coincidencia Parcial](https://github.com/user-attachments/assets/298eb55e-7393-440b-84a4-6ded03f3c2e8)

### Filtrar por continente
![Filtrar por continente](https://github.com/user-attachments/assets/048bccd9-83f2-4179-8745-92015a408f5e)

### Filtrar por población
![Filtrar por población](https://github.com/user-attachments/assets/51ef724e-5782-494d-881c-229150fa021e)

### Ordenar por nombre
![Ordenar por nombre](https://github.com/user-attachments/assets/52a13c58-47f0-4124-ba24-4fa474efb6a8)

Se adjuntan mas capturas del funcionamiento en el Informe del trabajo (PDF) para no sobrecargar el README.


## 👥 Integrantes del Equipo
1. Juan Martin Garcia

2. Tiziano Valentini

