from pg2_parcial1_p1.Conversordistancia import ConversorDistancia

def main():
    print("=== Conversor de Distancia ===")
    print("1. metros  a centimetros")
    print("2. centimetros a Kilómetros")
    opcion = input("Elige una opción (1 o 2): ")

    try:
        valor = float(input("Ingresa la distancia: "))
        conversor = ConversorDistancia(valor)

        if opcion == "1":
            resultado = conversor.m_a_cm()
            print(f"{valor} km = {resultado:.2f} millas")
        elif opcion == "2":
            resultado = conversor.cm_a_km()
            print(f"{valor} millas = {resultado:.2f} km")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Entrada no válida. Ingresa un número.")

if __name__ == "__main__":
    main()
