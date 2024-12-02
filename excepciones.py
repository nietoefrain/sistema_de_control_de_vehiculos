# Archivo general de excepciones

class ErrorDeLecturaCSV(Exception):
    def __init__(self, mensaje="Error al leer el archivo CSV"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ErrorDeEscrituraCSV(Exception):
    def __init__(self, mensaje="Error al escribir en el archivo CSV"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ErrorDeValidacion(Exception):
    def __init__(self, mensaje="Error de validación de datos"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ValorNegativoError(ErrorDeValidacion):
    def __init__(self, campo):
        mensaje = f"El valor para '{campo}' no puede ser negativo."
        super().__init__(mensaje)


class ValorNoNumericoError(ErrorDeValidacion):
    def __init__(self, campo):
        mensaje = f"El valor para '{campo}' debe ser numérico."
        super().__init__(mensaje)
