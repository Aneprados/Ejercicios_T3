class Termino:
    """Clase que representa un término de un polinomio."""
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente

    def __repr__(self):
        return f"{self.coeficiente}x^{self.exponente}"