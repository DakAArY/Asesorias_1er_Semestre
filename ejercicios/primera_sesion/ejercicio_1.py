letra = input("Introduce una sola letra: ")
letra_minuscula = letra.lower()  # Con .lower() se convierte todo a minusculas

if (
    letra_minuscula in "aeiou"
):  # Se comprueba que la letra se encuentre dentro de la cadena "aeiou"
    print("Es una vocal")  # En caso de que sea true (este dentro) ejecutamos esto

else:
    print("No es una vocal")  # Caso contrario, ejecutamos esto
