# 1) Factorial recursivo
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo: factoriales desde 1 hasta un número ingresado
num = int(input("Ingrese un número para calcular factoriales: "))
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")


# 2) Fibonacci recursivo
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

pos = int(input("Ingrese la posición hasta la cual generar Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(pos + 1):
    print(fibonacci(i), end=" ")
print()


# 3) Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

b = int(input("Ingrese la base: "))
e = int(input("Ingrese el exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")


# 4) Decimal a binario recursivo
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

num_bin = int(input("Ingrese un número decimal para convertir a binario: "))
binario = decimal_a_binario(num_bin)
print(f"Binario: {binario if binario else '0'}")


# 5) Palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

pal = input("Ingrese una palabra para verificar si es palíndromo: ").lower()
print("Es palíndromo:", es_palindromo(pal))


# 6) Suma de dígitos recursiva
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

num_suma = int(input("Ingrese un número para sumar sus dígitos: "))
print("Suma de dígitos:", suma_digitos(num_suma))


# 7) Contar bloques de una pirámide
def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)

bloques = int(input("Ingrese cantidad de bloques del nivel más bajo: "))
print("Total bloques necesarios:", contar_bloques(bloques))


# 8) Contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

num_contar = int(input("Ingrese un número: "))
dig = int(input("Ingrese el dígito a contar: "))
print(f"El dígito {dig} aparece {contar_digito(num_contar, dig)} veces.")
