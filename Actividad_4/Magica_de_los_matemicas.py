class Termino:
    """Clase que representa un término de un polinomio."""
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente

    def __repr__(self):
        return f"{self.coeficiente}x^{self.exponente}"


class Polinomio:
    """Clase que representa un polinomio como un conjunto de términos."""
    def __init__(self):
        self.terminos = []

    def agregar_termino(self, coeficiente, exponente):
        """Agrega un término al polinomio."""
        self.terminos.append(Termino(coeficiente, exponente))

    def eliminar_termino(self, exponente):
        """Elimina un término del polinomio dado su exponente."""
        self.terminos = [t for t in self.terminos if t.exponente != exponente]

    def existe_termino(self, exponente):
        """Determina si un término con un exponente específico existe en el polinomio."""
        return any(t.exponente == exponente for t in self.terminos)

    def restar(self, otro):
        """Resta otro polinomio de este polinomio."""
        resultado = Polinomio()
        for t in self.terminos:
            resultado.agregar_termino(t.coeficiente, t.exponente)
        for t in otro.terminos:
            resultado.agregar_termino(-t.coeficiente, t.exponente)
        return resultado.simplificar()

    def dividir(self, otro):
        """Divide este polinomio por otro polinomio (división sintética)."""
        cociente = Polinomio()
        residuo = Polinomio()
        for t in self.terminos:
            residuo.agregar_termino(t.coeficiente, t.exponente)

        while residuo.terminos and residuo.terminos[0].exponente >= otro.terminos[0].exponente:
            coef = residuo.terminos[0].coeficiente / otro.terminos[0].coeficiente
            exp = residuo.terminos[0].exponente - otro.terminos[0].exponente
            termino_division = Termino(coef, exp)
            cociente.agregar_termino(coef, exp)

            # Resta el resultado de la multiplicación del divisor por el término actual
            divisor_multiplicado = Polinomio()
            for t in otro.terminos:
                divisor_multiplicado.agregar_termino(t.coeficiente * coef, t.exponente + exp)
            residuo = residuo.restar(divisor_multiplicado)

        return cociente, residuo

    def simplificar(self):
        """Simplifica el polinomio combinando términos con el mismo exponente."""
        terminos_dict = {}
        for t in self.terminos:
            if t.exponente in terminos_dict:
                terminos_dict[t.exponente] += t.coeficiente
            else:
                terminos_dict[t.exponente] = t.coeficiente

        self.terminos = [Termino(c, e) for e, c in terminos_dict.items() if c != 0]
        self.terminos.sort(key=lambda t: t.exponente, reverse=True)
        return self

    def __repr__(self):
        return " + ".join(map(str, self.terminos)) if self.terminos else "0"


# Ejemplo de uso
if __name__ == "__main__":
    p1 = Polinomio()
    p1.agregar_termino(3, 2)
    p1.agregar_termino(5, 1)

    p2 = Polinomio()
    p2.agregar_termino(1, 1)
    p2.agregar_termino(2, 0)

    print("Polinomio 1:", p1)
    print("Polinomio 2:", p2)

    resta = p1.restar(p2)
    print("Resta:", resta)

    cociente, residuo = p1.dividir(p2)
    print("Cociente:", cociente)
    print("Residuo:", residuo)

    p1.eliminar_termino(1)
    print("Polinomio 1 después de eliminar término con exponente 1:", p1)

    existe = p1.existe_termino(2)
    print("¿Existe término con exponente 2 en Polinomio 1?", existe)