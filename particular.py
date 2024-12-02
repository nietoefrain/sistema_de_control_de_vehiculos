from automovil import Automovil

class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self._nro_puestos = nro_puestos

    def get_nro_puestos(self):
        return self._nro_puestos

    def set_nro_puestos(self, nro_puestos):
        if nro_puestos < 0:
            raise ValueError("El número de puestos no puede ser negativo.")
        self._nro_puestos = nro_puestos

    def __str__(self):
        return f"{super().__str__()}, Puestos: {self._nro_puestos}"
