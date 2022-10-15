# Tipos de variables [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplos capturando información desde la consola

# - Comencemos a ingresar datos por medio de la consola
# Input nos permite mostrar en pantalla un texto
# y luego la consola se queda esperado por un dato
# a ingresar por nosotros
# - En este caso ingresaremos texto, por lo que
# transformaremos el dato ingresado por consola a texto --> str
nombre = str(input('Ingrese su nombre:'))
print('Nombre ingresado:', nombre)

# Utilizamos "int" cuando lo que se desea ingresar
# es un número entero (sin coma)
edad = int(input('Ingrese cuantos años tiene:'))
print('Edad ingresada:', edad)

# Utilizamos "float" cuando lo que se desea ingresar
# es un número decimal (con coma)
altura = float(input('Ingrese su altura en metros:'))
print('Altura ingresada:', altura)
