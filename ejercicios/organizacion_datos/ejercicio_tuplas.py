# Coordenadas geográficas

import math

puntos = []

while True:
    print("\n=== PUNTOS EN EL PLANO ===")
    print("1. Agregar punto")
    print("2. Ver puntos")
    print("3. Calcular distancia entre dos puntos")
    print("4. Ver punto medio")
    print("5. Salir")
    
    opcion = input("\nElige opción: ")
    
    if opcion == "1":
        x = float(input("Coordenada x: "))
        y = float(input("Coordenada y: "))
        puntos.append((x, y))
        print(f"[OK] Punto agregado: ({x}, {y})")
    
    elif opcion == "2":
        if not puntos:
            print("No hay puntos")
        else:
            for i, (x, y) in enumerate(puntos):
                print(f"{i}. ({x}, {y})")
    
    elif opcion == "3":
        if len(puntos) < 2:
            print("Necesitas al menos 2 puntos")
        else:
            for i, punto in enumerate(puntos):
                print(f"{i}. {punto}")
            i1 = int(input("Primer punto: "))
            i2 = int(input("Segundo punto: "))
            x1, y1 = puntos[i1]
            x2, y2 = puntos[i2]
            distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            print(f"Distancia: {distancia:.2f}")
    
    elif opcion == "4":
        if len(puntos) < 2:
            print("Necesitas al menos 2 puntos")
        else:
            for i, punto in enumerate(puntos):
                print(f"{i}. {punto}")
            i1 = int(input("Primer punto: "))
            i2 = int(input("Segundo punto: "))
            x1, y1 = puntos[i1]
            x2, y2 = puntos[i2]
            medio = ((x1 + x2) / 2, (y1 + y2) / 2)
            print(f"Punto medio: {medio}")
    
    elif opcion == "5":
        break
