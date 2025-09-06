#Ejercicio1 Solicita la edad al usuario
edad = int(input("Ingrese su edad: "))

# Verifica si es mayor de 18
if edad > 18:
    print("Es mayor de edad")

#Ejercicio2 
     Solicita la nota al usuario
nota = float(input("Ingrese su nota: "))
# Verifica si aprobó o desaprobó
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
    #Ejercio3
    # Programa que permite ingresar solo números pares

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
      
#Ejercicio4
# Programa que clasifica la edad del usuario en categorías

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#ejercicio5
# Programa que valida la longitud de una contraseña

contraseña = input("Ingrese una contraseña: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

 #ejercicio6
 import random
from statistics import mean, median, multimode

# Generar lista
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

# Calcular estadísticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
modas = multimode(numeros_aleatorios)  # devuelve lista de modas (1 o más)

# Mostrar resumen (no imprimo toda la lista para no llenar la pantalla)
print("Media:", media)
print("Mediana:", mediana)
print("Modas:", modas)

# Clasificar según el criterio dado
eps = 1e-9  # tolerancia para comparar igualdad de floats

if len(modas) != 1:
    print("Hay más de una moda (muestra multimodal); con el criterio dado la clasificación es inconclusa.")
else:
    moda = modas[0]
    if media > mediana > moda:
        print("La distribución tiene sesgo positivo (a la derecha).")
    elif media < mediana < moda:
        print("La distribución tiene sesgo negativo (a la izquierda).")
    elif abs(media - mediana) < eps and abs(mediana - moda) < eps:
        print("La distribución no tiene sesgo (media = mediana = moda).")
    else:
        print("La distribución no cumple exactamente con los criterios de sesgo definidos.")

#ejercicio7
# Pedimos al usuario que ingrese una frase o palabra
texto = input("Escribí una palabra o frase: ")

# Verificamos si el último carácter es una vocal
if texto[-1] in "aeiouAEIOU":
    texto = texto + "!"  # Agregamos un signo de exclamación

# Mostramos el resultado
print(texto)

#ejercicio8
# Pedimos al usuario que ingrese su nombre
nombre = input("Ingresá tu nombre: ")

# Pedimos que elija una opción
opcion = input("Elegí una opción (1: mayúsculas, 2: minúsculas, 3: primera letra mayúscula): ")

# Convertimos el nombre según la opción
if opcion == "1":
    nombre = nombre.upper()   # Todas las letras en mayúscula
elif opcion == "2":
    nombre = nombre.lower()   # Todas las letras en minúscula
elif opcion == "3":
    nombre = nombre.title()   # Primera letra en mayúscula
else:
    print("Opción no válida")

# Mostramos el resultado
print("Resultado:", nombre)

#ejercicio9
# Pedimos al usuario que ingrese la magnitud del terremoto
magnitud = float(input("Ingresá la magnitud del terremoto: "))

# Clasificamos según la magnitud
if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)"
else:  # magnitud >= 7
    categoria = "Extremo (puede causar graves daños a gran escala)"

# Mostramos el resultado
print("Categoría del terremoto:", categoria)

#ejercicio10
# Pedimos al usuario que ingrese su hemisferio, mes y día
hemisferio = input("Ingresá tu hemisferio (N/S): ").upper()  # convertimos a mayúscula para evitar errores
mes = int(input("Ingresá el mes (1-12): "))
dia = int(input("Ingresá el día (1-31): "))

# Inicializamos la estación
estacion = ""

# Determinamos la estación según hemisferio
if hemisferio == "N":  # Hemisferio Norte
    if (mes == 12 and dia >= 21) or (mes <= 3 and (mes != 3 or dia <= 20)):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes <= 6 and (mes != 6 or dia <= 20)):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes != 9 or dia <= 20)):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes <= 12 and (mes != 12 or dia <= 20)):
        estacion = "Otoño"
elif hemisferio == "S":  # Hemisferio Sur
    if (mes == 12 and dia >= 21) or (mes <= 3 and (mes != 3 or dia <= 20)):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes <= 6 and (mes != 6 or dia <= 20)):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes != 9 or dia <= 20)):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes <= 12 and (mes != 12 or dia <= 20)):
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

# Mostramos el resultado
print("La estación actual es:", estacion)

