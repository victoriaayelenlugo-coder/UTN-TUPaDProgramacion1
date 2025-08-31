#ejercicio1: crear un programa que imprima "Hola Mundo!"
print("Hola Mundo!")

#ejercicio2:crear un programa que  pida al usuario su nombre e imprima "Hola, nombre]!".
nombre= input("cual es tu nombre?")

#ejercicio3: pedir datos al usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
# Mostrar los datos en una sola oración
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#ejercicio4:pedir al usuario el area de un circulo e imprimir su area y perimetro
import math  # Para usar el valor de pi
# Pedir el radio al usuario
radio = float(input("Ingresa el radio del círculo: "))
# Calcular área y perímetro
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio
# Mostrar resultados
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

#ejercicio5:pedir al usuario una cantidad de segundos e imprimir su equivalente en horas
# Pedir cantidad de segundos
segundos = int(input("Ingresa la cantidad de segundos: "))
# Calcular cuántas horas son
horas = segundos / 3600  # 1 hora = 3600 segundos
# Mostrar resultado
print(f"{segundos} segundos equivalen a {horas} horas.")

#ejercicio6:pedir al usuario un numero e imprima por pantalla la tabla de multiplicar de dicho numero
# Pedir número al usuario
numero = int(input("Ingresa un número: "))
# Imprimir la tabla de multiplicar
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

    #ejercicio7:pedir al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos,dividirlos,multiplicarlos y restarlos
# Pedir los dos números
num1 = int(input("Ingresa el primer número (distinto de 0): "))
num2 = int(input("Ingresa el segundo número (distinto de 0): "))
# Verificar que no sean cero
if num1 != 0 and num2 != 0:
    # Operaciones
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    # Mostrar resultados
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")
else:
    print("Error: Los números deben ser distintos de 0.")

#ejercicio8:pedir al usuario su altura y peso e imprimir su IMC
# Pedir datos al usuario
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
# Calcular IMC
imc = peso / (altura ** 2)
# Mostrar resultado
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

#ejercicio9:pedir al usuario una temperatura en grados Celsius e imprimir su equivalete en grados Fahrenheit 
# Pedir temperatura en Celsius
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
# Convertir a Fahrenheit
fahrenheit = (9/5) * celsius + 32
# Mostrar resultado
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

#ejercicio10:pedir al usuario 3 numeros e imprima el promedio de dichos numeros
# Pedir los tres números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
# Calcular promedio
promedio = (num1 + num2 + num3) / 3
# Mostrar resultado
print(f"El promedio de los tres números es: {promedio:.2f}")


