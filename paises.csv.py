import csv

# --- CONSTANTES ---
# Nombre del archivo CSV donde se guardan los datos
NOMBRE_ARCHIVO_CSV = "paises.csv"

# Campos de cada país
CAMPOS_PAIS = ["nombre", "poblacion", "superficie", "continente"]

# Menú principal del programa
MENU_PRINCIPAL = """
===== MENÚ PRINCIPAL =====
1. Agregar país
2. Actualizar país
3. Buscar país
4. Filtrar por continente
5. Filtrar por población
6. Filtrar por superficie
7. Ordenar por nombre
8. Ordenar por población
9. Ordenar por superficie
10. Estadísticas
11. Guardar y salir
"""

# --- FUNCIONES DE VISUALIZACIÓN ---
def mostrar_pais(registro_pais):
    """Imprime un país de forma legible."""
    print(f"  {registro_pais['nombre']:<15} | "
          f"Población: {registro_pais['poblacion']:<15,} | "
          f"Superficie: {registro_pais['superficie']:<15,} km² | "
          f"Continente: {registro_pais['continente']}")

def mostrar_lista_paises(lista_paises):
    """Imprime una lista de países."""
    if not lista_paises:
        print("No se encontraron resultados.")
        return
    print("\n--- RESULTADOS ---")
    for pais in lista_paises:
        mostrar_pais(pais)
    print("------------------")

# --- GESTIÓN DE ARCHIVOS CSV ---
def cargar_datos(ruta_archivo):
    """Carga los datos desde un CSV y convierte los campos a enteros."""
    with open(ruta_archivo, newline='', encoding="utf-8") as archivo_csv:
        lector_diccionario = csv.DictReader(archivo_csv)
        lista_paises = [
            {
                "nombre": fila_registro["nombre"],
                "poblacion": int(fila_registro["poblacion"]),
                "superficie": int(fila_registro["superficie"]),
                "continente": fila_registro["continente"]
            }
            for fila_registro in lector_diccionario
        ]
    return lista_paises

def guardar_datos(ruta_archivo, lista_paises):
    """Guarda la lista de países en el CSV."""
    with open(ruta_archivo, "w", newline='', encoding="utf-8") as archivo_csv:
        escritor_diccionario = csv.DictWriter(archivo_csv, fieldnames=CAMPOS_PAIS)
        escritor_diccionario.writeheader()
        escritor_diccionario.writerows(lista_paises)

# --- FUNCIONES CRUD Y VALIDACIONES ---
def agregar_pais(lista_paises):
    """Agrega un país validando campos vacíos y formato numérico."""
    print("\n--- AGREGAR NUEVO PAÍS ---")
    nombre_nuevo = input("Nombre del país: ").strip()
    str_poblacion = input("Población: ").strip()
    str_superficie = input("Superficie: ").strip()
    nombre_continente = input("Continente: ").strip()

    if not nombre_nuevo or not nombre_continente or not str_poblacion or not str_superficie:
        print("Error: Ningún campo puede estar vacío.")
        return
    if nombre_nuevo.isdigit():
        print("Error: El nombre del país no puede ser solo numérico.")
        return
    if not str_poblacion.isdigit() or not str_superficie.isdigit():
        print("Error: Población y Superficie deben ser números enteros.")
        return

    nuevo_pais = {
        "nombre": nombre_nuevo.title(),
        "poblacion": int(str_poblacion),
        "superficie": int(str_superficie),
        "continente": nombre_continente.title()
    }
    lista_paises.append(nuevo_pais)
    print("País agregado correctamente.")

def actualizar_pais(lista_paises):
    """Actualiza población y superficie de un país existente."""
    nombre_buscado = input("Ingrese nombre del país a actualizar: ").lower().strip()
    if not nombre_buscado:
        print("Error: El nombre del país no puede estar vacío.")
        return

    pais_encontrado = False
    for registro_pais in lista_paises:
        if nombre_buscado in registro_pais["nombre"].lower():
            str_nueva_pob = input(f"Nueva población para {registro_pais['nombre']} (dejar vacío para no cambiar): ").strip()
            str_nueva_sup = input(f"Nueva superficie para {registro_pais['nombre']} (dejar vacío para no cambiar): ").strip()

            if str_nueva_pob and not str_nueva_pob.isdigit():
                print("Error: La nueva población debe ser un número entero.")
                return
            if str_nueva_sup and not str_nueva_sup.isdigit():
                print("Error: La nueva superficie debe ser un número entero.")
                return

            if str_nueva_pob:
                registro_pais["poblacion"] = int(str_nueva_pob)
            if str_nueva_sup:
                registro_pais["superficie"] = int(str_nueva_sup)

            print(f"Datos de {registro_pais['nombre']} actualizados.")
            pais_encontrado = True
            break
    if not pais_encontrado:
        print("País no encontrado.")

# --- FUNCIONES DE BÚSQUEDA Y FILTROS ---
def buscar_pais(lista_paises):
    """Busca un país por nombre (coincidencia parcial)."""
    nombre_buscado = input("Buscar país: ").lower().strip()
    if not nombre_buscado:
        print("El campo de búsqueda no puede estar vacío.")
        return
    resultados_busqueda = [pais for pais in lista_paises if nombre_buscado in pais["nombre"].lower()]
    mostrar_lista_paises(resultados_busqueda)

def filtrar_por_continente(lista_paises):
    """Filtra países por continente."""
    continente_filtro = input("Ingrese continente: ").lower().strip()
    if not continente_filtro:
        print("El continente no puede estar vacío.")
        return
    paises_filtrados = [pais for pais in lista_paises if pais["continente"].lower() == continente_filtro]
    mostrar_lista_paises(paises_filtrados)

def filtrar_por_poblacion(lista_paises):
    """Filtra países por rango de población."""
    str_minimo = input("Población mínima: ").strip()
    str_maximo = input("Población máxima: ").strip()
    if not str_minimo.isdigit() or not str_maximo.isdigit():
        print("Error: Los límites deben ser números enteros.")
        return
    min_pob = int(str_minimo)
    max_pob = int(str_maximo)
    paises_filtrados = [pais for pais in lista_paises if min_pob <= pais["poblacion"] <= max_pob]
    mostrar_lista_paises(paises_filtrados)

def filtrar_por_superficie(lista_paises):
    """Filtra países por rango de superficie."""
    str_minimo = input("Superficie mínima: ").strip()
    str_maximo = input("Superficie máxima: ").strip()
    if not str_minimo.isdigit() or not str_maximo.isdigit():
        print("Error: Los límites deben ser números enteros.")
        return
    min_sup = int(str_minimo)
    max_sup = int(str_maximo)
    paises_filtrados = [pais for pais in lista_paises if min_sup <= pais["superficie"] <= max_sup]
    mostrar_lista_paises(paises_filtrados)

# --- FUNCIONES DE ORDENAMIENTO Y ESTADÍSTICAS ---
def ordenar_paises_por_clave(lista_paises, clave_ordenamiento, es_descendente=False):
    """Ordena la lista de países según la clave y orden indicado."""
    paises_ordenados = sorted(lista_paises, key=lambda pais: pais[clave_ordenamiento], reverse=es_descendente)
    mostrar_lista_paises(paises_ordenados)

def estadisticas(lista_paises):
    """Calcula y muestra estadísticas globales."""
    if not lista_paises:
        print("No hay datos cargados.")
        return
    pais_mayor_pob = max(lista_paises, key=lambda pais: pais["poblacion"])
    pais_menor_pob = min(lista_paises, key=lambda pais: pais["poblacion"])
    promedio_pob = sum(pais["poblacion"] for pais in lista_paises) / len(lista_paises)
    promedio_sup = sum(pais["superficie"] for pais in lista_paises) / len(lista_paises)
    conteo_continentes = {}
    for pais in lista_paises:
        cont = pais["continente"]
        conteo_continentes[cont] = conteo_continentes.get(cont, 0) + 1

    print("\n--- ESTADÍSTICAS GLOBALES ---")
    print(f"País con mayor población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']:,})")
    print(f"País con menor población: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']:,})")
    print(f"Promedio de población: {promedio_pob:,.2f}")
    print(f"Promedio de superficie: {promedio_sup:,.2f} km²")
    print("Cantidad de países por continente:")
    for cont, count in conteo_continentes.items():
        print(f"  - {cont}: {count}")
    print("----------------------------")

# --- MENÚ PRINCIPAL ---
def menu_principal():
    """Bucle principal que muestra el menú y ejecuta opciones hasta salir."""
    lista_paises = cargar_datos(NOMBRE_ARCHIVO_CSV)
    while True:
        print(MENU_PRINCIPAL)
        opcion_seleccionada = input("Seleccione opción: ")
        match opcion_seleccionada:
            case "1": agregar_pais(lista_paises)
            case "2": actualizar_pais(lista_paises)
            case "3": buscar_pais(lista_paises)
            case "4": filtrar_por_continente(lista_paises)
            case "5": filtrar_por_poblacion(lista_paises)
            case "6": filtrar_por_superficie(lista_paises)
            case "7": ordenar_paises_por_clave(lista_paises, "nombre")
            case "8":
                es_desc = input("¿Descendente? (s/n): ").lower() == "s"
                ordenar_paises_por_clave(lista_paises, "poblacion", es_descendente=es_desc)
            case "9":
                es_desc = input("¿Descendente? (s/n): ").lower() == "s"
                ordenar_paises_por_clave(lista_paises, "superficie", es_descendente=es_desc)
            case "10": estadisticas(lista_paises)
            case "11":
                guardar_datos(NOMBRE_ARCHIVO_CSV, lista_paises)
                print("Datos guardados. Saliendo...")
                break
            case _: print("Opción inválida.")

# --- INICIO DEL PROGRAMA ---
# Descomentar la siguiente línea para ejecutar la aplicación:
# menu_principal()
