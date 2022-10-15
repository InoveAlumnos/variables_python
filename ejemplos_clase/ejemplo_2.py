# Tipos de variables [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplos varialbles de texto
texto_1 = 'Hola'
texto_2 = 'Mundo'

# Imprimimos los textos directo a consola
print(texto_1, texto_2)

# Vemos que los textos aparecen separadas en la consola
# Esto es porque el print agrega espacios entre cada
# variable o texto separada por coma

# Operación de unir textos (concatenar o sumar texto)
# Creamos una variable llamada suma que almacena
# el contenido de las variables texto_1 y texto_2
# separadas por un espacio

suma = texto_1 + texto_2  # Operamos la suma
# Imprimimos en consola el resultado
print('El resultado de la suma es', suma)

# Operación de unir textos (concatenar o sumar texto)
# Creamos una variable llamada mensaje que almacena
# el contenido de las variables texto_1 y texto_2
# separadas por un espacio

mensaje = texto_1 + ' ' + texto_2
print('El resultado de la suma con espacio es', suma)
print(mensaje)

# Duplicando el texto
texto_duplicado = texto_1 * 2
print('Duplicar texto', texto_1, ':', texto_duplicado)
