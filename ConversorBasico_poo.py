class ConversorBasico:
    def __init__(self):
        self._resultado = 0
        self.operacion = ""

    def conversor_generica(self, valor, tipo_conversion):

        if tipo_conversion == "m_a_cm":
            self.operacion = "Metros a Centímetros"
            self._resultado = valor * 100

        elif tipo_conversion == "cm_a_km":
            self.operacion = "Centímetros a Kilómetros"
            self._resultado = valor / 100000
        else:
            self.operacion = "Conversión no válida"
            self._resultado = None
            return "Error: tipo de conversión no soportado."
        return self._mostrar(valor)

    def _mostrar(self, valor):
        return f"{self.operacion}: {valor} → {self._resultado:.5f}"

    
    
