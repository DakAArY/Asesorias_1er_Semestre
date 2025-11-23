# Operaciones con grupos de estudiantes

matematicas = set()
fisica = set()

while True:
    print("\n=== GESTIÓN DE CLASES ===")
    print("1. Agregar estudiante a Matemáticas")
    print("2. Agregar estudiante a Física")
    print("3. Ver estudiantes")
    print("4. Estudiantes en ambas clases")
    print("5. Estudiantes solo en Matemáticas")
    print("6. Salir")
    
    opcion = input("\nElige opción: ")
    
    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        matematicas.add(nombre)
        print("[OK] Estudiante agregado a Matemáticas")
    
    elif opcion == "2":
        nombre = input("Nombre del estudiante: ")
        fisica.add(nombre)
        print("[OK] Estudiante agregado a Física")
    
    elif opcion == "3":
        print(f"\nMatemáticas ({len(matematicas)}): {matematicas}")
        print(f"Física ({len(fisica)}): {fisica}")
    
    elif opcion == "4":
        comun = matematicas.intersection(fisica)
        print(f"Estudiantes en ambas: {comun if comun else 'Ninguno'}")
    
    elif opcion == "5":
        solo_mate = matematicas.difference(fisica)
        print(f"Solo en Matemáticas: {solo_mate if solo_mate else 'Ninguno'}")
    
    elif opcion == "6":
        break
