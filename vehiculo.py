class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self._marca = marca
        self._modelo = modelo
        self._nro_ruedas = nro_ruedas

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_nro_ruedas(self):
        return self._nro_ruedas

    def set_nro_ruedas(self, nro_ruedas):
        if nro_ruedas < 0:
            raise ValueError("El número de ruedas no puede ser negativo.")
        self._nro_ruedas = nro_ruedas

    def __str__(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}, Ruedas: {self._nro_ruedas}"
