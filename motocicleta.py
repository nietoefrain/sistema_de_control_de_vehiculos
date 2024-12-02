from bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self._motor = motor
        self._cuadro = cuadro
        self._nro_radios = nro_radios

    def get_motor(self):
        return self._motor

    def set_motor(self, motor):
        self._motor = motor

    def get_cuadro(self):
        return self._cuadro

    def set_cuadro(self, cuadro):
        self._cuadro = cuadro

    def get_nro_radios(self):
        return self._nro_radios

    def set_nro_radios(self, nro_radios):
        if nro_radios < 0:
            raise ValueError("El número de radios no puede ser negativo.")
        self._nro_radios = nro_radios

    def __str__(self):
        return f"{super().__str__()}, Motor: {self._motor}, Cuadro: {self._cuadro}, Número de Radios: {self._nro_radios}"
