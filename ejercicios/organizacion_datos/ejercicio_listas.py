# Gestor de tareas

tareas = []

while True:
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Ver pendientes")
    print("5. Salir")
    
    opcion = input("\nElige opción: ")
    
    if opcion == "1":
        descripcion = input("Descripción: ")
        tareas.append(descripcion)
        print("[OK] Tarea agregada")
    
    elif opcion == "2":
        if not tareas:
            print("No hay tareas")
        else:
            for i, tarea in enumerate(tareas):
                print(f"{i}. {tarea}")
    
    elif opcion == "3":
        for i, tarea in enumerate(tareas):
            print(f"{i}. {tarea}")
        indice = int(input("Número de tarea a completar: "))
        if 0 <= indice < len(tareas):
            tareas[indice] = f"[X] {tareas[indice]}"
        else:
            print("Índice inválido")
    
    elif opcion == "4":
        pendientes = [t for t in tareas if not t.startswith("[X]")]
        print(f"Tareas pendientes: {len(pendientes)}")
        for tarea in pendientes:
            print(f"- {tarea}")
    
    elif opcion == "5":
        break
