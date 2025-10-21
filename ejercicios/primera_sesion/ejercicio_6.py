palabra_original = input("Introduce una palabra para verificar si es palindromo: ")

palabra = palabra_original.strip().lower()  # Limpiamos la palabra

palabra_invertida = palabra[::-1]  # La leemos al reves

if palabra == palabra_invertida:  # comprobamos que sea igual que al reves
    print(f"{palabra_original} si es un palindromo")

else:  # Si no es palindromo se ejecuta esto:
    print(f"{palabra_original} NO es un palindromo")
