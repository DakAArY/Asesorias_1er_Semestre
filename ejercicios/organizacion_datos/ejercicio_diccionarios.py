# Inventario de tienda

inventario = {}

while True:
    print("\n=== INVENTARIO ===")
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Buscar por categoría")
    print("4. Actualizar stock")
    print("5. Salir")
    
    opcion = input("\nElige opción: ")
    
    if opcion == "1":
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        categoria = input("Categoría: ")
        inventario[codigo] = {'nombre': nombre, 'precio': precio, 'stock': stock, 'categoria': categoria}
        print("[OK] Producto agregado")
    
    elif opcion == "2":
        if not inventario:
            print("Inventario vacío")
        else:
            for cod, prod in inventario.items():
                print(f"{cod}: {prod['nombre']} - ${prod['precio']} - Stock: {prod['stock']} - {prod['categoria']}")
    
    elif opcion == "3":
        categoria = input("Categoría a buscar: ")
        productos = {cod: prod for cod, prod in inventario.items() if prod['categoria'] == categoria}
        if productos:
            for cod, prod in productos.items():
                print(f"- {prod['nombre']}")
        else:
            print("No hay productos en esa categoría")
    
    elif opcion == "4":
        codigo = input("Código del producto: ")
        if codigo in inventario:
            cantidad = int(input("Cantidad a sumar (negativo para restar): "))
            inventario[codigo]['stock'] += cantidad
            print(f"[OK] Nuevo stock: {inventario[codigo]['stock']}")
        else:
            print("Producto no encontrado")
    
    elif opcion == "5":
        break
