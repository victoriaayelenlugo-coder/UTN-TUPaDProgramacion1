# practica_archivos.py
# Práctica: Archivos - manejo de productos (texto, CSV simple)

from pathlib import Path

RUTA = Path("productos.txt")

def crear_archivo_inicial():
    """Crea productos.txt con 3 productos si no existe."""
    if not RUTA.exists():
        lineas = [
            "Lapicera,120.5,30\n",
            "Cuaderno,450.0,50\n",
            "Regla,35.0,100\n"
        ]
        RUTA.write_text("".join(lineas), encoding="utf-8")
        print("Archivo 'productos.txt' creado con 3 productos iniciales.")

def leer_productos_desde_archivo():
    """Lee el archivo y devuelve lista de lineas crudas."""
    productos = []
    with RUTA.open("r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            partes = linea.split(",")
            # validación básica: espera 3 partes
            if len(partes) != 3:
                print(f"Advertencia: línea con formato inesperado: {linea}")
                continue
            nombre = partes[0].strip()
            try:
                precio = float(partes[1].strip())
            except ValueError:
                print(f"Advertencia: precio inválido en línea: {linea}")
                continue
            try:
                cantidad = int(partes[2].strip())
            except ValueError:
                print(f"Advertencia: cantidad inválida en línea: {linea}")
                continue
            productos.append({
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            })
    return productos

def mostrar_productos(productos):
    """Muestra los productos con el formato pedido."""
    if not productos:
        print("No hay productos para mostrar.")
        return
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

def agregar_producto_a_archivo(nombre, precio, cantidad):
    """Agrega un producto al archivo sin borrar el contenido previo."""
    linea = f"{nombre},{precio},{cantidad}\n"
    with RUTA.open("a", encoding="utf-8") as f:
        f.write(linea)

def buscar_producto_por_nombre(productos, nombre_buscar):
    """Busca (case-insensitive) y devuelve la lista de coincidencias."""
    nombre_buscar = nombre_buscar.strip().lower()
    encontrados = [p for p in productos if p["nombre"].lower() == nombre_buscar]
    return encontrados

def guardar_productos(productos):
    """Sobrescribe el archivo con la lista de productos proporcionada."""
    lineas = [f"{p['nombre']},{p['precio']},{p['cantidad']}\n" for p in productos]
    with RUTA.open("w", encoding="utf-8") as f:
        f.writelines(lineas)

def pedir_producto_por_teclado():
    """Pide nombre, precio y cantidad validando los datos."""
    nombre = input("Ingrese nombre del producto: ").strip()
    while not nombre:
        nombre = input("Nombre vacío. Ingrese nombre del producto: ").strip()

    while True:
        precio_str = input("Ingrese precio (ej: 120.5): ").strip()
        try:
            precio = float(precio_str)
            break
        except ValueError:
            print("Precio inválido. Intente de nuevo.")

    while True:
        cantidad_str = input("Ingrese cantidad (entera): ").strip()
        try:
            cantidad = int(cantidad_str)
            break
        except ValueError:
            print("Cantidad inválida. Intente de nuevo.")

    return {"nombre": nombre, "precio": precio, "cantidad": cantidad}

def main():
    crear_archivo_inicial()

    # 2 & 4: Leer y cargar en lista de diccionarios
    productos = leer_productos_desde_archivo()
    print("\nProductos cargados desde archivo:")
    mostrar_productos(productos)

    # 3: Agregar productos desde teclado (opcional)
    respuesta = input("\n¿Desea agregar un nuevo producto? (s/n): ").strip().lower()
    if respuesta == "s":
        nuevo = pedir_producto_por_teclado()
        # Agregamos al archivo inmediatamente (sin borrar)
        agregar_producto_a_archivo(nuevo["nombre"], nuevo["precio"], nuevo["cantidad"])
        # También lo agregamos a la lista en memoria
        productos.append(nuevo)
        print("\nProducto agregado correctamente.")

    # 5: Buscar producto por nombre
    busq = input("\nIngrese el nombre del producto a buscar (o deje vacío para omitir): ").strip()
    if busq:
        resultados = buscar_producto_por_nombre(productos, busq)
        if resultados:
            print("\nProducto/s encontrado/s:")
            mostrar_productos(resultados)
        else:
            print("Producto no encontrado.")

    # 6: Guardar los productos actualizados sobrescribiendo el archivo
    respuesta_guardar = input("\n¿Desea sobrescribir el archivo con los productos actuales en memoria? (s/n): ").strip().lower()
    if respuesta_guardar == "s":
        guardar_productos(productos)
        print("Archivo sobrescrito con la lista actualizada de productos.")
    else:
        print("No se sobrescribió el archivo. Los cambios previos (si agregó) ya quedaron en el archivo por append.")

    print("\nEjecución finalizada.")

if __name__ == "__main__":
    main()
