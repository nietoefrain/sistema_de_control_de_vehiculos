from datetime import datetime
from vehiculo import Vehiculo
from automovil import Automovil
from particular import Particular
from carga import Carga
from bicicleta import Bicicleta
from motocicleta import Motocicleta
from manejo_csv import ManejoCSV
from excepciones import *
from utils import *


# Vehiculos predeterminaods
def vehiculos_predeterminados():
    return [
        Particular("Ford", "Fiesta", 4, 180, 500, 5),
        Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000),
        Bicicleta("Shimano", "MT Ranger", 2, "Carrera"),
        Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)
    ]


def crear_automoviles():
    automoviles = []
    n = input_numero("\n¿Cuántos Vehículos desea insertar? ")
    if n <= 0:
        print("Debe ingresar al menos un vehículo.")
        return automoviles

    for i in range(n):
        try:
            print(f"\nDatos del automóvil {i + 1}")
            marca = input_no_vacio("Inserte la marca del automóvil: ")
            modelo = input_no_vacio("Inserte el modelo: ")
            nro_ruedas = input_numero("Inserte el número de ruedas: ")
            if nro_ruedas < 0:
                raise ValorNegativoError("nro_ruedas")
            velocidad = input_numero("Inserte la velocidad en km/h: ")
            cilindrada = input_numero("Inserte el cilindraje en cc: ")

            automovil = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
            automoviles.append(automovil)
        except ValorNegativoError as e:
            print(f"Error: {e}")
    return automoviles


def verificar_instancia():
    vehiculos = vehiculos_predeterminados()
    print("\n**Información detallada de las instancias de Vehículos** \n")
    for vehiculo in vehiculos:
        print(vehiculo)

    print("\n**Verificación de la relación de instancias para la clase Motocicleta** \n")
    motocicleta = vehiculos[-1] 
    relaciones = {
        "Vehiculo": isinstance(motocicleta, Vehiculo),
        "Automovil": isinstance(motocicleta, Automovil),
        "Particular": isinstance(motocicleta, Particular),
        "Carga": isinstance(motocicleta, Carga),
        "Bicicleta": isinstance(motocicleta, Bicicleta),
        "Motocicleta": isinstance(motocicleta, Motocicleta),
    }
    for clase, es_instancia in relaciones.items():
        print(f"Motocicleta es instancia con relación a {clase}: {es_instancia}")


def menu():
    vehiculos = []
    vehiculos_predefinidos = vehiculos_predeterminados()
    manejo_csv = ManejoCSV()

    while True:
        saludo = obtener_saludo()
        limpiar_pantalla()
        print("""
            
            
            ························································································································
            :                                                                                                                      :
            : ░█▀▀░▀█▀░█▀▀░▀█▀░█▀▀░█▄█░█▀█░░░█▀▄░█▀▀░░░█▀▀░█▀█░█▀█░▀█▀░█▀▄░█▀█░█░░░░░█▀▄░█▀▀░░░█░█░█▀▀░█░█░▀█▀░█▀▀░█░█░█░░░█▀█░█▀▀ :
            : ░▀▀█░░█░░▀▀█░░█░░█▀▀░█░█░█▀█░░░█░█░█▀▀░░░█░░░█░█░█░█░░█░░█▀▄░█░█░█░░░░░█░█░█▀▀░░░▀▄▀░█▀▀░█▀█░░█░░█░░░█░█░█░░░█░█░▀▀█ :
            : ░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░▀░▀░▀░░░▀▀░░▀▀▀░░░▀▀▀░▀▀▀░▀░▀░░▀░░▀░▀░▀▀▀░▀▀▀░░░▀▀░░▀▀▀░░░░▀░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀ :
            :                                                                                                                      :
            ························································································································

                                                                                      +##.                  
                                                                                   -+.##-                   
                                                                                 ..++.-                     
                                                                                .#.+.                       
                                                                             .#-.+.                         
                                                                           -#.#-                            
                                                                        .+.-#.                              
                                         ###############-             .--#..                                
                                         -#############+            ..#+.-                                  
                                         -#.          ++           +#.#.                                    
                                         -#.          ++        .#--#                                       
                                         -#.  .###.   ++      -#-#-    -#++++++++++++++#.                   
                                         -#.  .###-   ++    -###.    .#-                +-                  
                                         -#. -#####-  +++#####+      #.                  +-                 
                                         -#..#######+ +++#####  -####.                    +####             
                                         -#############++#####  .+##-----------------------##+-             
                                         -#############++#####   .###########################+              
                                         -#############++#####   .#+. .#################-  .#+.             
                                         -#############++#####   .#+   #################-  .#+.             
                                         -#############++#####   .###########################-              
                                         -#############++#####    +####+                #####-              
                                         -#############++#####    -####-                +###+.              
        """)
        print(saludo)
        print("\nMenú:\n")
        print("1. Insertar Vehículos")
        print("2. Verificación de Instancias")
        print("3. Guardar y Leer en CSV con Clasificación")
        print("4. Salir\n")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            automoviles_ingresados = crear_automoviles()
            vehiculos.extend(automoviles_ingresados)
            print("\nVehículos ingresados por el usuario: \n")
            for i, vehiculo in enumerate(automoviles_ingresados, 1):
                print(f"Datos del automóvil {i}: {vehiculo}")
            pausar()

        elif opcion == "2":
            verificar_instancia()
            pausar()

        elif opcion == "3":
            try:
                manejo_csv.guardar_datos_csv(vehiculos_predefinidos)
                print("\nLeyendo y clasificando vehículos desde CSV:")
                manejo_csv.leer_datos_csv()
            except (ErrorDeEscrituraCSV, ErrorDeLecturaCSV) as e:
                print(e)
            pausar()

        elif opcion == "4":
            print(f"{obtener_saludo()}, gracias por usar el sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")
            pausar()


if __name__ == "__main__":
    menu()
