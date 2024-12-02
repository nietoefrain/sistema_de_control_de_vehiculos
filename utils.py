#Algunas utilizades definidas para su uso en main.py

import os
from datetime import datetime
from excepciones import ValorNegativoError


def obtener_saludo():
    hora_actual = datetime.now().hour
    if 5 <= hora_actual < 12:
        return "🌅 Buenos días"
    elif 12 <= hora_actual < 18:
        return "🌞 Buenas tardes"
    else:
        return "🌙 Buenas noches"


def input_no_vacio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: Este campo no puede estar vacío. Por favor, regístre información.")


def input_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Se esperaba un valor numérico. Por favor, inténtelo de nuevo.")


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    input("\nPresione Enter para volver al menú principal...")
    limpiar_pantalla()
