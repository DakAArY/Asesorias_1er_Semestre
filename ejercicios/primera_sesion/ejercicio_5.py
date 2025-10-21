usuario = input("Introduce tu nombre de usuario: ")

if len(usuario) < 5 or len(usuario) > 15:  # Comparamos longitudes de la cadena
    print("Error: El nombre de usuario debe tener entre 5 y 15 caracteres")

elif " " in usuario:  # Si hay un espacio damos un error
    print("Error: el nombre de usuario no debe contener espacios")

elif not usuario[0].isalpha():  # Si el primer caracter no es una letra
    print("Error: el nombre de usuario debe comenzar con una letra.")

else:  # En caso de que no haya errores, todo bien
    print(f"'{usuario}' es un nombre de usuario valido")
