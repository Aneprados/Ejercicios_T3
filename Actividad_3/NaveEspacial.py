class NaveEspacial:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros

    def __repr__(self):
        return f"Nave(nombre={self.nombre}, longitud={self.longitud}, tripulantes={self.tripulantes}, pasajeros={self.pasajeros})"
