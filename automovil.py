from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self._velocidad = velocidad
        self._cilindrada = cilindrada

    # velocidad
    def get_velocidad(self):
        return self._velocidad

    def set_velocidad(self, velocidad):
        if velocidad < 0:
            raise ValueError("La velocidad no puede ser negativa.")
        self._velocidad = velocidad

    # cilindrada
    def get_cilindrada(self):
        return self._cilindrada

    def set_cilindrada(self, cilindrada):
        if cilindrada < 0:
            raise ValueError("La cilindrada no puede ser negativa.")
        self._cilindrada = cilindrada

    def __str__(self):
        return f"{super().__str__()}, Velocidad: {self._velocidad} Km/h, Cilindrada: {self._cilindrada} cc"
