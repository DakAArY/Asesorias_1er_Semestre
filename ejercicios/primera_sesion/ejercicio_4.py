palabra = input("Introduce una palabra: ")

if len(palabra) > 0:  # Observamos que no este vacia la entrada
    ultimo_caracter = palabra[
        -1
    ]  # con [-1] accedemos al ultimo indice o caracter en este caso

    if (
        ultimo_caracter == "s" or ultimo_caracter == "S"
    ):  # comprobamos una de las dos condiciones
        print("La palabra esta en plural")

    else:
        print("La palabra parece estar en singular")

else:
    print("No has introducido ninguna palabra")
