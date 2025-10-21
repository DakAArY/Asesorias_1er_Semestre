turno = input("En que turno trabajas? (mañana, tarde o noche): ")
turno_limpio = (
    turno.lower().strip()
)  # el input se convierte a minusculas y despues se quitan espacios al inicio y al final

if turno_limpio == "mañana":  # Se comprueba la cadena ya limpia
    print("Buenos dias !")

elif turno_limpio == "tarde":
    print("Buenas tardes!")

elif turno_limpio == "noche":
    print("Buenas noches!")

else:
    print("No has introducido un turno valido")
