from vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)
        self._tipo = tipo

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo

    def __str__(self):
        return f"{super().__str__()}, Tipo: {self._tipo}"
