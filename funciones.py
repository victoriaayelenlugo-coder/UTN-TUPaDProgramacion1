"""
Práctico 2: Funciones en Python
Archivo: practico2_funciones.py
Descripción: Implementación de las 10 actividades solicitadas en un solo archivo.
Cada función está documentada y hay un menú interactivo para probarlas.
"""
import math


def imprimir_hola_mundo():
    """Imprime "Hola Mundo!"""
    print("Hola Mundo!")


def saludar_usuario(nombre: str) -> str:
    """Devuelve un saludo personalizado para el nombre dado.

    Args:
        nombre: Nombre de la persona.

    Returns:
        Saludo en formato "Hola <nombre>!".
    """
    return f"Hola {nombre}!"


def informacion_personal(nombre: str, apellido: str, edad: int, residencia: str) -> None:
    """Imprime la información personal en una frase.

    Ejemplo: "Soy Juan Pérez, tengo 30 años y vivo en Córdoba".
    """
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


def calcular_area_circulo(radio: float) -> float:
    """Devuelve el área de un círculo con el radio dado.

    Área = pi * r^2
    """
    return math.pi * radio ** 2


def calcular_perimetro_circulo(radio: float) -> float:
    """Devuelve el perímetro (circunferencia) de un círculo con el radio dado.

    Perímetro = 2 * pi * r
    """
    return 2 * math.pi * radio


def segundos_a_horas(segundos: float) -> float:
    """Convierte segundos a horas (valor en punto flotante)."""
    return segundos / 3600.0


def tabla_multiplicar(numero: int) -> None:
    """Imprime la tabla de multiplicar del 1 al 10 para el número dado."""
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def operaciones_basicas(a: float, b: float):
    """Devuelve una tupla con (suma, resta, multiplicacion, division).

    Si la división no es posible (b == 0) devuelve None en el cuarto elemento.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = None
    try:
        division = a / b
    except ZeroDivisionError:
        division = None
    return suma, resta, multiplicacion, division


def calcular_imc(peso: float, altura: float) -> float:
    """Calcula el Índice de Masa Corporal (IMC).

    IMC = peso (kg) / (altura (m))^2
    """
    if altura <= 0:
        raise ValueError("La altura debe ser mayor que 0")
    return peso / (altura ** 2)


def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte Celsius a Fahrenheit.

    F = C * 9/5 + 32
    """
    return celsius * 9.0 / 5.0 + 32.0


def calcular_promedio(a: float, b: float, c: float) -> float:
    """Devuelve el promedio de tres números."""
    return (a + b + c) / 3.0


# --- Programa principal con un pequeño menú para probar cada función ---

def pedir_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Intenta de nuevo con un número.")


def pedir_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Intenta de nuevo con un número entero.")


def main():
    while True:
        print("\n--- Práctico 2: Funciones en Python ---")
        print("1 - Imprimir 'Hola Mundo'")
        print("2 - Saludar usuario")
        print("3 - Información personal")
        print("4 - Área y perímetro de un círculo")
        print("5 - Segundos a horas")
        print("6 - Tabla de multiplicar")
        print("7 - Operaciones básicas")
        print("8 - Calcular IMC")
        print("9 - Celsius a Fahrenheit")
        print("10 - Calcular promedio de tres números")
        print("0 - Salir")

        opcion = input("Elige una opción (0-10): ")

        if opcion == "1":
            imprimir_hola_mundo()

        elif opcion == "2":
            nombre = input("Ingresa tu nombre: ")
            print(saludar_usuario(nombre))

        elif opcion == "3":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = pedir_int("Edad: ")
            residencia = input("Residencia: ")
            informacion_personal(nombre, apellido, edad, residencia)

        elif opcion == "4":
            radio = pedir_float("Radio del círculo: ")
            area = calcular_area_circulo(radio)
            perimetro = calcular_perimetro_circulo(radio)
            print(f"Área: {area:.4f}")
            print(f"Perímetro: {perimetro:.4f}")

        elif opcion == "5":
            segundos = pedir_float("Cantidad de segundos: ")
            horas = segundos_a_horas(segundos)
            print(f"Equivalente en horas: {horas:.6f} h")

        elif opcion == "6":
            numero = pedir_int("Número para la tabla de multiplicar: ")
            tabla_multiplicar(numero)

        elif opcion == "7":
            a = pedir_float("Ingresa el primer número (a): ")
            b = pedir_float("Ingresa el segundo número (b): ")
            suma, resta, mult, div = operaciones_basicas(a, b)
            print(f"Suma: {suma}")
            print(f"Resta: {resta}")
            print(f"Multiplicación: {mult}")
            if div is None:
                print("División: No se puede dividir por cero")
            else:
                print(f"División: {div}")

        elif opcion == "8":
            peso = pedir_float("Peso (kg): ")
            altura = pedir_float("Altura (m): ")
            try:
                imc = calcular_imc(peso, altura)
                print(f"IMC: {imc:.2f}")
            except ValueError as e:
                print(e)

        elif opcion == "9":
            celsius = pedir_float("Temperatura en Celsius: ")
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius} °C = {fahrenheit:.2f} °F")

        elif opcion == "10":
            a = pedir_float("Número 1: ")
            b = pedir_float("Número 2: ")
            c = pedir_float("Número 3: ")
            promedio = calcular_promedio(a, b, c)
            print(f"Promedio: {promedio}")

        elif opcion == "0":
            print("Saliendo. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()