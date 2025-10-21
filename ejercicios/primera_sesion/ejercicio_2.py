nombre = input("Introduce tu nombre: ")
longitud = len(nombre)  # Con len() contamos la cantidad de elementos que contiene algo

if longitud >= 8:  # Si es mayor o igual...
    print("Tu nombre es largo")  # Imprimimos esto

elif (
    longitud >= 3
):  # Aqui ya sabemos que es menor que ocho, entonces si es mayor o igual que 3...
    print("Tu nombre tiene una longitud normal")  # Ejecutamos esto otro

else:
    print("Tu nombre es demasiado corto")  # En caso de que lo demás haya dado false
