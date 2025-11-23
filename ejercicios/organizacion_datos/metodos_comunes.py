# Métodos comunes de estructuras de datos en Python

print("\n" + "=" * 60)
print(" " * 20 + "LISTAS")
print("=" * 60)

numeros = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\n>>> Lista original: {numeros}\n")

numeros.append(8)
print(f"   append(8) → {numeros}")

numeros.insert(2, 99)
print(f"   insert(2, 99) → {numeros}")

numeros.remove(1)
print(f"   remove(1) → {numeros}")

ultimo = numeros.pop()
print(f"   pop() → Elemento: {ultimo}, Lista: {numeros}")

numeros.sort()
print(f"   sort() → {numeros}")

numeros.reverse()
print(f"   reverse() → {numeros}")

print(f"\n   count(1) → {numeros.count(1)}")
print(f"   index(5) → {numeros.index(5)}")

copia = numeros.copy()
print(f"   copy() → {copia}")

numeros.clear()
print(f"   clear() → {numeros}")

print("\n\n" + "=" * 60)
print(" " * 18 + "DICCIONARIOS")
print("=" * 60)

persona = {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid'}
print(f"\n>>> Diccionario original: {persona}\n")

persona['profesion'] = 'Ingeniera'
print(f"   persona['profesion'] = 'Ingeniera' → {persona}")

print(f"\n   get('nombre') → {persona.get('nombre')}")
print(f"   get('telefono', 'No existe') → {persona.get('telefono', 'No existe')}")

print(f"\n   keys() → {list(persona.keys())}")
print(f"   values() → {list(persona.values())}")
print(f"   items() → {list(persona.items())}")

persona.update({'edad': 26, 'pais': 'España'})
print(f"\n   update({{'edad': 26, 'pais': 'España'}}) → {persona}")

profesion = persona.pop('profesion')
print(f"   pop('profesion') → Valor: {profesion}, Dict: {persona}")

ultimo = persona.popitem()
print(f"   popitem() → {ultimo}, Dict: {persona}")

edad = persona.setdefault('edad', 30)
print(f"\n   setdefault('edad', 30) → {edad}")

telefono = persona.setdefault('telefono', '123456')
print(f"   setdefault('telefono', '123456') → {telefono}, Dict: {persona}")

persona.clear()
print(f"   clear() → {persona}")

print("\n\n" + "=" * 60)
print(" " * 20 + "TUPLAS")
print("=" * 60)

coordenadas = (10, 20, 30, 20, 40)
print(f"\n>>> Tupla original: {coordenadas}\n")

print(f"   count(20) → {coordenadas.count(20)}")
print(f"   index(30) → {coordenadas.index(30)}")

x, y, *resto = coordenadas
print(f"\n   Desempaquetado → x: {x}, y: {y}, resto: {resto}")

print(f"\n   Acceso [0] → {coordenadas[0]}")
print(f"   Slice [1:3] → {coordenadas[1:3]}")
print(f"   len() → {len(coordenadas)}")

tupla_concatenada = coordenadas + (50, 60)
print(f"\n   Concatenación + (50, 60) → {tupla_concatenada}")

tupla_repetida = (1, 2) * 3
print(f"   Repetición (1, 2) * 3 → {tupla_repetida}")

print("\n\n" + "=" * 60)
print(" " * 21 + "SETS")
print("=" * 60)

colores1 = {'rojo', 'azul', 'verde', 'amarillo'}
colores2 = {'azul', 'verde', 'naranja', 'morado'}
print(f"\n>>> Set 1: {colores1}")
print(f">>> Set 2: {colores2}\n")

colores1.add('negro')
print(f"   add('negro') → {colores1}")

colores1.remove('negro')
print(f"   remove('negro') → {colores1}")

colores1.discard('blanco')
print(f"   discard('blanco') → {colores1}")

print(f"\n   'rojo' in colores1 → {'rojo' in colores1}")

print(f"\n   union() → {colores1.union(colores2)}")
print(f"   intersection() → {colores1.intersection(colores2)}")
print(f"   difference() → {colores1.difference(colores2)}")
print(f"   symmetric_difference() → {colores1.symmetric_difference(colores2)}")

colores3 = colores1.copy()
print(f"\n   copy() → {colores3}")

colores1.update(['rosa', 'gris'])
print(f"   update(['rosa', 'gris']) → {colores1}")

elemento = colores1.pop()
print(f"   pop() → Elemento: {elemento}, Set: {colores1}")

colores1.clear()
print(f"   clear() → {colores1}")

print("\n\n" + "=" * 60)
print(" " * 16 + "MÉTODOS COMPARTIDOS")
print("=" * 60)

lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
conjunto = {1, 2, 3, 4, 5}
diccionario = {'a': 1, 'b': 2, 'c': 3}

print("\n>>> Función len():")
print(f"   len(lista) → {len(lista)}")
print(f"   len(tupla) → {len(tupla)}")
print(f"   len(conjunto) → {len(conjunto)}")
print(f"   len(diccionario) → {len(diccionario)}")

print("\n>>> Funciones matemáticas:")
print(f"   max(lista) → {max(lista)}")
print(f"   min(lista) → {min(lista)}")
print(f"   sum(lista) → {sum(lista)}")

print("\n>>> Operador in:")
print(f"   3 in lista → {3 in lista}")
print(f"   3 in tupla → {3 in tupla}")
print(f"   3 in conjunto → {3 in conjunto}")
print(f"   'a' in diccionario → {'a' in diccionario}")

print("\n\n" + "=" * 60)
print(" " * 12 + "LIST COMPREHENSIONS Y OPERACIONES")
print("=" * 60)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\n>>> Lista: {numeros}\n")

pares = [n for n in numeros if n % 2 == 0]
print(f"   [n for n in numeros if n % 2 == 0] → {pares}")

cuadrados = [n**2 for n in numeros]
print(f"   [n**2 for n in numeros] → {cuadrados}")

dict_cuadrados = {n: n**2 for n in numeros if n <= 5}
print(f"\n   {{n: n**2 for n in numeros if n <= 5}} → {dict_cuadrados}")

set_pares = {n for n in numeros if n % 2 == 0}
print(f"\n   {{n for n in numeros if n % 2 == 0}} → {set_pares}")

print("\n" + "=" * 60 + "\n")
