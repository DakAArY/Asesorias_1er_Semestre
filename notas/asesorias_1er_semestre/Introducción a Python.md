Primeramente, Bienvenid@s al mundo de la programación, así que antes de comenzar a programar hablemos un poco del lenguaje que vamos a aprender.

## Que es Python? ----------------------------------------
Imaginemos que tenemos un robot muy obediente y eficaz (en nuestro caso nuestra computadora) y queremos darle instrucciones de lo que queremos hacer, como nuestro robot no entiende español, no podemos simplemente decirle "Haz esto.", así que tenemos que aprender a hablar su idioma para poder darle instrucciones, aquí es donde entran los lenguajes de programación, en este caso, *Python*.

*Pero, Qué hace especial a Python?*
- **Python es un lenguaje de alto nivel:** Esto significa que se parece mas al lenguaje natural que usamos nosotros como seres humanos (como por ejemplo, el ingles), en lugar de acercarse al lenguaje de unos y ceros que entienden las maquinas, Python es mas fácil de entender y aprender.
```python
#Este codigo es mas facil de entender para un humano
if edad > 18: #Si la edad es mayor que 18...
	print("Es mayor de edad.") #Imprimimos que es mayor de edad.
```


- **Python es un lenguaje de propósito general:** Python es como una navaja suiza. No sirve para una sola cosa, Sirve para muchísimas. Se usa para crear paginas web, en ciencia de datos, para inteligencia artificial, para crear videojuegos y mucho más. Es una herramienta super versátil

## Tipos de datos básicos -----------------------------------
Para construir cualquier cosa se necesitan materiales, en la programación nuestros materiales son *Los Datos*. Python es muy listo y sabe que tipo de dato es cada cosa sin que se lo tengas que decir explicita-mente.

##### Los números (`int` y `float`):
- **Enteros (`int`):** Son números completos, sin ningún decimal. Son perfectos para contar cosas.
```python
# Ejemplo: Cuantas manzanas tienes?
manzanas_en_cesta = 5 #Variable con el numero 5 como dato
print(f"Tengo {manzanas_en_cesta} manzanas.") # Imprimimos cuantas manzanas tenemos
```

- **Flotantes (`float`):** Son números con decimales. Ideales para cosas que se pueden medir o para precios.
```python
# Ejemplo: CUanto cuesta un refresco?
precio_refresco = 12.50
print(f"El refresco cuesta: {precio_refresco}$")
```

- **El Texto (`str`):** Cualquier cosa que vaya entre comillas dobles o simples (`"` o `'`) es un texto o también conocido como cadena de texto.
```python
# Ejemplo: Un saludo
texto = "Hola Mundo!" # Tambien se puede escribir 'Hola mundo' (con comillas simples)
print(texto)
```

- **Interruptores (`bool`):** Pensemos en ellos como un interruptor de luz, solo puede estar *Encendido* (`True`) o *Apagado* ( `False`)
```python
esta_lloviendo = True #Iniciamos la variable con un valor verdadero

if esta_lloviendo == True: # Si esta lloviendo...
	print("LLevar paraguas") # Llevamos paraguas
else: # En caso de que no llueva...
	print("No llevar paraguas") #Pues no llevamos paraguas

# Resultado del ejercicio
# Como la variable era verdadera, el programa mostrara el mensaje de llevar paraguas
```


## Los Condicionales: Tomando Decisiones ---------------
Un programa es más útil si puede reaccionar a distintas situaciones o casos. Es como pensamos: 
"*Sí* llueve, *Entonces* llevo paraguas".

### if / else (El plan A y el plan B)

*Si* (`if`) la condición se cumple, haz una cosa. *Si no* (`else`) haz otra.
```python
# Ejemplo: Aprobé el examen?
calificación = 8 # La variable calificacion tiene el numero 8 como valor

if calificación >= 7: # Pedimos que para que el caso se cumpla, el numero sea igual o mayor a 7
	print("Felicidades, aprobaste!") # Ejecutamos si la condicion es verdadera
else: # En caso de que no sea verdadero el if, se ejecuta el else
	print("Mala suerte, a estudiar para la proxima")
```

Si queremos abarcar más condiciones podemos hacer uso del `elif` 
```python
num = 5

if num > 10: # Como num no es mayor que diez, no se cumple el if
	print(f"El numero {num} es mayor que diez")
elif num == 5: #Pero como es igual a 5, el elif si se cumple
	print(f"El numero {num} es igual a 5")
else: # Y se ignora el else
	print(f"No es un numero!!")
```

## Los ciclos (y Bucles): Repitiendo Tareas------------------

Los ciclos hacen el trabajo repetitivo por nosotros para no tener que escribir la misma instrucción 100 veces.

### Ciclo `for` (Repetir para cada elemento)
El ciclo `for` es perfecto para recorrer (iterar) elementos, uno por uno
```python
# Ejemplo: Saludar a todos en una lista
invitados = ["Ailyn", "Juan Pablo", "Liliana"] # Una lista con cadenas de texto (strings)

print("Bienvenidos a la sesion de estudios!")
for persona in invitados: # Por cada elemento que encuentre va a repetir una accion
	print(f"Hola, {persona}!") # Saluda al Elemento encontrado

# La salida de este programa sería:
# Bienvenidos a la sesion de estudios!
# Hola Ailyn!
# Hola Juan Pablo!
# Hola Liliana!
```

### Ciclo `while` (Repetir mientras algo sea Verdad)
Este ciclo se sigue ejecutando **mientras** su condición sea `True`. Debes asegurarte de que la condición en algún momento cambie a `False` para que el ciclo no sea infinito!

```python
# Ejemplo: Cuenta regresiva para un cohete
numero = 5

print("Iniciando cuenta regresiva...")
while numero > 0: # Mientras el numero sea mayor a cero, se repite, cuando sea cero, termina
    print(numero)
    numero = numero - 1 # ¡Esta línea es clave para que el ciclo termine! (se resta por cada repeticion para que en algun momento llegue a cero)

print("¡Despegue!")
```