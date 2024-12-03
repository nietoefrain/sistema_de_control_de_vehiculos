# Sistema de Control de Vehículos 🚗

¡Bienvenido al **Sistema de Control de Vehículos**! Este proyecto es el resultado de la práctica de consolidación del Módulo 4 de Programación Orientada a Objetos (POO). Su objetivo es gestionar de manera eficiente diferentes tipos de vehículos y sus características utilizando los principios de la POO. 

## Tabla de Contenidos 📋

- [Descripción](#descripción)
- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)

## Descripción 📝

Este sistema permite registrar y gestionar información de diversos vehículos, incluyendo automóviles, motocicletas, bicicletas y vehículos de carga. Implementa principios de POO para garantizar un diseño modular y escalable.

## Características ✨

- **Gestión de Vehículos:** Registro de datos de diferentes tipos de vehículos.
- **Herencia Múltiple:** Uso de herencia para compartir y especializar comportamientos entre clases de vehículos.
- **Persistencia de Datos:** Almacenamiento y recuperación de información de vehículos desde archivos CSV.
- **Interfaz de Usuario:** Menús interactivos para facilitar la navegación y operación del sistema.
- **Diagrama de Clases:** se adjunta el diagrama de clases que representa la estructura del sistema para gestionar vehículos, aplicando herencia, polimorfismo y manejo de datos con archivos CSV en Python.


![Sistema Control de Vehiculos](https://github.com/user-attachments/assets/c21053c5-38e5-411c-baa0-c4909963369e)


## Instalación 🛠️

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/nietoefrain/sistema_de_control_de_vehiculos.git

2. **Navegar al directorio del proyecto**
   ```bash
   cd sistema_de_control_de_vehiculos
   
3. **Instalar las dependencias necesarias:**

  Asegurate de tener Python 3.7 (version mínima) instalado en tu sistema.

## Uso 🚀
Ejecutar el programa principal:
```bash
python main.py
```
<img width="946" alt="img_init" src="https://github.com/user-attachments/assets/f785b084-43f0-4bbc-b7f9-74e6acd76d41">

## Opción 1: Insertar Vehículos
* Permite al usuario ingresar manualmente información sobre nuevos vehículos.
* Solicita datos como marca, modelo, número de ruedas, velocidad, y cilindrada.
* Valida que los datos ingresados sean correctos y no permite campos vacíos ni valores inválidos.
  
## Opción 2: Verificación de Instancias
* Muestra información detallada de vehículos predeterminados (como Particular, Carga, Bicicleta, Motocicleta).
* Realiza una verificación de la relación de instancias entre Motocicleta y las clases principales (Vehiculo, Automovil, etc.).
* Proporciona resultados como True o False según las relaciones de herencia y pertenencia.

## Opción 3: Guardar y Leer en CSV con Clasificación
* Guarda los vehículos predeterminados en un archivo CSV con formato adecuado.
* Lee el archivo CSV y clasifica los vehículos según su tipo (Particular, Carga, Bicicleta, Motocicleta).
* Muestra en consola la clasificación y los datos guardados.

## Opción 4: Salir
Finaliza el programa.
Imprime un mensaje de despedida con un saludo personalizado según la hora del sistema (buenos días, tardes o noches).


