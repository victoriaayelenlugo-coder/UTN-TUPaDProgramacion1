# =========================================================
# 1) Agregar frutas al diccionario
# =========================================================
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario con nuevas frutas:", precios_frutas)


# =========================================================
# 2) Actualizar precios
# =========================================================
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Diccionario con precios actualizados:", precios_frutas)


# =========================================================
# 3) Lista con solo las frutas
# =========================================================
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)


# =========================================================
# 4) Agenda telefónica
# =========================================================
telefonos = {}

for i in range(5):
    nombre = input("Nombre del contacto: ")
    numero = input("Número telefónico: ")
    telefonos[nombre] = numero

consulta = input("Ingresá un nombre para buscar su número: ")

if consulta in telefonos:
    print(f"El número de {consulta} es {telefonos[consulta]}")
else:
    print("Ese contacto no existe.")


# =========================================================
# 5) Palabras únicas y frecuencia
# =========================================================
frase = input("Ingresá una frase: ").lower()
palabras = frase.split()

palabras_unicas = set(palabras)

frecuencia = {}
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Frecuencia de palabras:", frecuencia)


# =========================================================
# 6) Promedio de alumnos
# =========================================================
alumnos = {}

for i in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Ingresá la nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} tiene un promedio de {promedio:.2f}")


# =========================================================
# 7) Aprobados de parciales
# =========================================================
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)


# =========================================================
# 8) Stock de productos
# =========================================================
stock = {'Arroz': 10, 'Fideos': 20, 'Pan': 15}

producto = input("Ingresá un producto: ")

if producto in stock:
    print(f"Hay {stock[producto]} unidades de {producto}.")
    agregar = int(input("¿Cuántas unidades querés agregar? "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("El producto no existe. Ingresá su cantidad inicial: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)


# =========================================================
# 9) Agenda de eventos
# =========================================================
agenda = {
    ('Lunes', '10:00'): 'Gimnasio',
    ('Martes', '14:00'): 'Clases',
    ('Miércoles', '18:00'): 'Reunión'
}

dia = input("Ingresá un día: ")
hora = input("Ingresá una hora (ej: 10:00): ")

evento = agenda.get((dia, hora), "No hay actividades en ese horario.")
print(evento)


# =========================================================
# 10) Invertir diccionario (países y capitales)
# =========================================================
paises = {'Argentina': 'Buenos Aires', 'Chile': 'Santiago', 'Perú': 'Lima'}

capitales = {capital: pais for pais, capital in paises.items()}

print("Diccionario invertido:", capitales)
