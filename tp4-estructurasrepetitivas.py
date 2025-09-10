#Ejercicio1
# Programa que imprime los números del 0 al 100, uno por línea

for i in range(0, 101):   # range(0, 101) va desde 0 hasta 100 inclusive
    print(i)

#Ejercicio2
# Programa que solicita un número entero y determina la cantidad de dígitos

numero = int(input("Ingrese un número entero: "))

# Convertimos el número a cadena para contar sus dígitos
cantidad_digitos = len(str(abs(numero)))   # abs() para que ignore el signo negativo

print("El número tiene", cantidad_digitos, "dígitos.")

#Ejercicio3
# Programa que suma todos los números enteros entre dos valores dados (excluyéndolos)

# Pedimos los dos valores al usuario
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

# Nos aseguramos de que 'a' sea el menor y 'b' el mayor
menor = min(a, b)
mayor = max(a, b)

# Sumamos los valores comprendidos entre 'menor' y 'mayor' (sin incluirlos)
suma = 0
for i in range(menor + 1, mayor):
    suma += i

print("La suma de los números comprendidos entre", a, "y", b, "es:", suma)
 
 #Ejercicio4
 # Programa que suma números enteros ingresados por el usuario
# Se detiene cuando el usuario ingresa un 0

suma = 0

while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print("La suma total acumulada es:", suma)

#Ejercicio5
# Juego de adivinanza: el usuario debe adivinar un número aleatorio entre 0 y 9

import random

# Generamos un número aleatorio entre 0 y 9
secreto = random.randint(0, 9)

intentos = 0
acertado = False

while not acertado:
    numero = int(input("Adivine el número (entre 0 y 9): "))
    intentos += 1
    if numero == secreto:
        acertado = True

print("¡Correcto! El número era", secreto)
print("Número de intentos necesarios:", intentos)

#Ejercicio6
# Programa que imprime los números pares entre 0 y 100 en orden decreciente

for i in range(100, -1, -2):   # Empieza en 100, termina en 0, de 2 en 2
    print(i)

#Ejericio7
# Programa que calcula la suma de todos los números comprendidos entre 0 y un número dado

n = int(input("Ingrese un número entero positivo: "))

suma = 0
for i in range(1, n):   # desde 1 hasta n-1 (excluye 0 y n)
    suma += i

print("La suma de los números comprendidos entre 0 y", n, "es:", suma)

#Ejercicio8
# Programa que analiza 100 números ingresados por el usuario

# Cantidad de números a ingresar (se puede cambiar fácilmente)
cantidad = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    
    # Contamos pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Contamos positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

#Ejercicio9
# Programa que calcula la media de 100 números enteros ingresados por el usuario

# Cantidad de números a ingresar (se puede cambiar fácilmente)
cantidad = 100

suma = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero

media = suma / cantidad
print("La media de los números ingresados es:", media)

#Ejercicio10
# Programa que invierte el orden de los dígitos de un número

numero = input("Ingrese un número entero: ")

# Invertimos la cadena y la mostramos
numero_invertido = numero[::-1]

print("El número invertido es:", numero_invertido)