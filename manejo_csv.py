import csv
from excepciones import ErrorDeLecturaCSV, ErrorDeEscrituraCSV

class ManejoCSV:
    def __init__(self, nombre_archivo="vehiculos.csv"):
        self.nombre_archivo = nombre_archivo

    def guardar_datos_csv(self, vehiculos):
        try:
            with open(self.nombre_archivo, "w", newline="") as archivo:
                archivo_csv = csv.writer(archivo)
                
                for vehiculo in vehiculos:
                    tipo = f"<class 'Vehiculo.{vehiculo.__class__.__name__}'>"
                    
                    atributos = {k.lstrip('_'): v for k, v in vehiculo.__dict__.items()}
                    
                    archivo_csv.writerow([tipo, atributos])
            
            print("Datos guardados correctamente en el archivo CSV.")
        except Exception as e:
            raise ErrorDeEscrituraCSV(f"Error al guardar los datos en CSV: {e}")

    def leer_datos_csv(self):
        """Lee y clasifica los datos de los vehículos desde un archivo CSV."""
        try:
            clasificacion = {"Particular": [], "Carga": [], "Bicicleta": [], "Motocicleta": []}

            with open(self.nombre_archivo, "r") as archivo:
                archivo_csv = csv.reader(archivo)

                for row in archivo_csv:
                    tipo, atributos = row
                    tipo_clase = tipo.split(".")[-1].replace("'>", "")
                    atributos = eval(atributos)
                    
                    if tipo_clase in clasificacion:
                        clasificacion[tipo_clase].append(atributos)

            print("\nClasificación de vehículos desde el archivo CSV:")
            for tipo, datos in clasificacion.items():
                print(f"\nLista de Vehiculos {tipo}:")
                for atributo in datos:
                    print(atributo)

        except Exception as e:
            raise ErrorDeLecturaCSV(f"Error al leer los datos desde CSV: {e}")
