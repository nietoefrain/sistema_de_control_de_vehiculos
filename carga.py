from automovil import Automovil

class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self._carga = carga

    def get_carga(self):
        return self._carga

    def set_carga(self, carga):
        if carga < 0:
            raise ValueError("La carga no puede ser negativa.")
        self._carga = carga

    def __str__(self):
        return f"{super().__str__()}, Carga: {self._carga} Kg"
