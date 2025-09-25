#Ejercicio1
# Crear lista vacía
notas = []

# Ingresar notas de 10 estudiantes
for i in range(1, 11):
    nota = float(input(f"Ingrese la nota del estudiante {i}: "))
    notas.append(nota)

# Mostrar la lista completa usando un bucle
print("\nLista de notas de los estudiantes:")
for i, nota in enumerate(notas, start=1):
    print(f"Estudiante {i}: {nota}")

# Calcular el promedio
suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)

print(f"\nPromedio de las notas: {promedio:.2f}")

# Encontrar la nota más alta y más baja
max_nota = notas[0]
min_nota = notas[0]

for nota in notas:
    if nota > max_nota:
        max_nota = nota
    if nota < min_nota:
        min_nota = nota

print(f"Nota más alta: {max_nota}")
print(f"Nota más baja: {min_nota}")

#Ejericio2
# Crear lista vacía
productos = []

# Pedir al usuario que ingrese 5 productos
for i in range(1, 6):
    producto = input(f"Ingrese el nombre del producto {i}: ")
    productos.append(producto)

# Mostrar la lista ordenada alfabéticamente usando sorted()
productos_ordenados = sorted(productos)
print("\nLista de productos ordenada alfabéticamente:")
for producto in productos_ordenados:
    print(producto)

# Preguntar qué producto desea eliminar
producto_eliminar = input("\nIngrese el nombre del producto que desea eliminar: ")

# Verificar si el producto existe y eliminarlo
if producto_eliminar in productos:
    productos.remove(producto_eliminar)
    print(f"\nProducto '{producto_eliminar}' eliminado. Lista actualizada:")
else:
    print(f"\nEl producto '{producto_eliminar}' no se encuentra en la lista.")

# Mostrar la lista actualizada
for producto in productos:
    print(producto)

#Ejericio3
import random

# Generar lista con 15 números enteros al azar entre 1 y 100
numeros = []
for _ in range(15):
    numeros.append(random.randint(1, 100))

print("Lista completa de números:")
print(numeros)

# Crear listas para pares e impares
pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Mostrar cantidad de números en cada lista
print(f"\nCantidad de números pares: {len(pares)}")
print(f"Números pares: {pares}")
print(f"\nCantidad de números impares: {len(impares)}")
print(f"Números impares: {impares}")

#Ejercicio4
# Lista con valores repetidos
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# Crear nueva lista sin elementos repetidos
lista_sin_repetidos = []
for valor in datos:
    if valor not in lista_sin_repetidos:
        lista_sin_repetidos.append(valor)

# Mostrar el resultado
print("Lista original:", datos)
print("Lista sin repetidos:", lista_sin_repetidos)

#Ejericio5
# Lista inicial con 8 estudiantes
estudiantes = ["Ana", "Juan", "María", "Pedro", "Lucía", "Carlos", "Sofía", "Diego"]

# Mostrar lista inicial
print("Lista inicial de estudiantes:")
for estudiante in estudiantes:
    print(estudiante)

# Preguntar al usuario qué acción quiere hacer
accion = input("\n¿Desea agregar un estudiante o eliminar uno existente? (agregar/eliminar): ").lower()

if accion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print(f"\nEstudiante '{nuevo}' agregado.")

elif accion == "eliminar":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print(f"\nEstudiante '{eliminar}' eliminado.")
    else:
        print(f"\nEl estudiante '{eliminar}' no se encuentra en la lista.")

else:
    print("\nAcción no reconocida. No se realizaron cambios.")

# Mostrar lista final actualizada
print("\nLista final de estudiantes:")
for estudiante in estudiantes:
    print(estudiante)

#Ejercicio6
# Lista con 7 números
numeros = [10, 20, 30, 40, 50, 60, 70]

# Guardar el último elemento
ultimo = numeros[-1]

# Mover cada elemento una posición hacia la derecha
for i in range(len(numeros)-1, 0, -1):
    numeros[i] = numeros[i-1]

# Colocar el último elemento en la primera posición
numeros[0] = ultimo

# Mostrar la lista rotada
print("Lista rotada hacia la derecha:")
print(numeros)

#Ejercicio7
# Crear matriz 7x2 con temperaturas mínimas y máximas de la semana
# Cada fila: [minima, maxima]
temperaturas = [
    [12, 22],  # Lunes
    [14, 25],  # Martes
    [10, 20],  # Miércoles
    [13, 28],  # Jueves
    [11, 23],  # Viernes
    [15, 26],  # Sábado
    [12, 24]   # Domingo
]

# Calcular promedio de mínimas y máximas
suma_min = 0
suma_max = 0

for temp in temperaturas:
    suma_min += temp[0]
    suma_max += temp[1]

promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)

print(f"Promedio de temperaturas mínimas: {promedio_min:.2f}")
print(f"Promedio de temperaturas máximas: {promedio_max:.2f}")

# Calcular el día con mayor amplitud térmica (maxima - minima)
mayor_amplitud = temperaturas[0][1] - temperaturas[0][0]
dia_mayor_amplitud = 0

for i in range(1, len(temperaturas)):
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print(f"Mayor amplitud térmica: {mayor_amplitud}°C el día {dias_semana[dia_mayor_amplitud]}")

#Ejercicio8
# Matriz con notas de 5 estudiantes en 3 materias
# Cada fila: [nota_materia1, nota_materia2, nota_materia3]
notas = [
    [7, 8, 9],   # Estudiante 1
    [6, 7, 8],   # Estudiante 2
    [9, 9, 10],  # Estudiante 3
    [5, 6, 7],   # Estudiante 4
    [8, 7, 9]    # Estudiante 5
]

# Mostrar promedio de cada estudiante
print("Promedio de cada estudiante:")
for i, estudiante in enumerate(notas, start=1):
    promedio = sum(estudiante) / len(estudiante)
    print(f"Estudiante {i}: {promedio:.2f}")

# Mostrar promedio de cada materia
print("\nPromedio de cada materia:")
num_materias = len(notas[0])
for j in range(num_materias):
    suma_materia = 0
    for i in range(len(notas)):
        suma_materia += notas[i][j]
    promedio_materia = suma_materia / len(notas)
    print(f"Materia {j+1}: {promedio_materia:.2f}")

#Ejercicio9
# Crear tablero 3x3 inicializado con guiones "-"
tablero = [["-" for _ in range(3)] for _ in range(3)]

# Función para mostrar el tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()  # Línea en blanco para separar turnos

# Mostrar tablero inicial
print("Tablero inicial:")
mostrar_tablero(tablero)

# Turnos de los jugadores (X y O)
for turno in range(9)

#Ejercicio10
# Matriz de ventas: 4 productos x 7 días
# Cada fila: ventas del producto en los 7 días
ventas = [
    [10, 12, 5, 8, 7, 9, 11],   # Producto 1
    [7, 8, 6, 5, 9, 10, 12],    # Producto 2
    [5, 6, 7, 8, 6, 5, 7],      # Producto 3
    [12, 10, 11, 9, 8, 12, 10]  # Producto 4
]

# Total vendido por cada producto
print("Total vendido por cada producto:")
total_productos = []
for i, producto in enumerate(ventas, start=1):
    total = sum(producto)
    total_productos.append(total)
    print(f"Producto {i}: {total} unidades")

# Día con mayores ventas totales
ventas_por_dia = []
for j in range(7):
    suma_dia = 0
    for i in range(4):
        suma
