
from pg2_parcial1_p1.ConversorBasico_poo import ConversorBasico

class ConversorDistancia(ConversorBasico):
    def __init__(self, valor, tipo_conversion):
        super().__init__() 
        self.valor = valor  
        self.tipo_conversion = tipo_conversion  

    def calcular(self):
      
        if self.tipo_conversion == "m_a_cm":
            self.operacion = "Metros a Centímetros"
            self._resultado = self.m_a_cm()

        elif self.tipo_conversion == "cm_a_km":
            self.operacion = "Centímetros a Kilómetros"
            self._resultado = self.cm_a_km()

        else:
            self.operacion = "Conversión no válida"
            self._resultado = None
            return "Error: tipo de conversión no soportado."

   

    def _mostrar_operacion(self):
        return f"{self.operacion}: {self.valor} → {self._resultado:.5f}"



