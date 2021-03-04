#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def numbers():
    # Ejemplos varialbles numéricas
    numero_1 = 2
    numero_2 = 4

    suma = numero_1 + numero_2   # Operamos la suma
    # Imprimimos en consola el resultado
    print('El resultado de la suma es', suma)

    resta = numero_1 - numero_2  # Operamos la resta

    # Imprimimos en consola el resultado con dos métodos distintos
    print('El resultado de restar', numero_1, 'y', numero_2, 'es', resta)

    # ¿Qué sucede si una variable no fue definida e intento imprimir su valor?
    # print('El valor de numero es',numero)

    # Ahora realizaremos ejemplos con números reales
    numero_3 = 3.0
    numero_4 = 4.5

    suma = numero_3 + numero_4  # Operamos la suma
    # Imprimimos en consola el resultado
    print('El resultado de la suma es', suma)

    resta = numero_4 - numero_3  # Operamos la resta

    # Imprimimos en consola el resultado con dos métodos distintos
    print('El resultado de restar', numero_4, 'y', numero_3, 'es', resta)

    # Ahora realizaremos un ejemplo numérico mixto

    suma = numero_3 + numero_1   # Operamos la suma
    # Imprimimos en consola el resultado
    print('El resultado sumar', numero_3, 'y', numero_1, 'es', suma)

    resta = numero_3 - numero_1  # Operamos la resta

    # Imprimimos en consola el resultado con dos métodos distintos
    print('El resultado de restar', numero_3, 'y', numero_1, 'es', resta)

    # Ensayo de división de números decimales
    division = numero_1 / numero_2
    print('El resultado dividir', numero_1, 'y', numero_2, 'es', division)


def strings():
    # Ejemplos varialbles de texto
    texto_1 = 'Hola'
    texto_2 = 'Mundo'

    suma = texto_1 + texto_2  # Operamos la suma
    # Imprimimos en consola el resultado
    print('El resultado de la suma es', suma)

    suma = texto_1 + ' ' + texto_2  # Operamos la suma
    # Imprimimos en consola el resultado
    print('El resultado de la suma es', suma)

    # Imprimimos los textos directo a consola
    print(texto_1, texto_2)

    mensaje = texto_1 + ' ' + texto_2
    print(mensaje)

    # Duplicando el texto
    texto_duplicado = texto_1 * 2
    print('Duplicar texto', texto_1, ':', texto_duplicado)

 
def consola():
    # Ejemplos capturando información desde la consola

    # Comencemos a ingresar datos por medio de la consola
    # Primero mostraremos en pantalla el dato deseado a ingresar
    # y luego esperaremos por el
    print('Ingrese su nombre:')
    nombre = str(input())
    print('Nombre ingresado:', nombre)

    print('Ingrese cuantos años tiene:')
    edad = int(input())
    print('Edad ingresada:', edad)

    print('Ingrese su altura en metros:')
    altura = float(input())
    print('Altura ingresada:', altura)


def operador_corchetes():
    # Una cadena de texto (string) está compuesta de Nº caracteres
    # ¿Cuántos caracteres tiene el Argentina?
    pais = 'Argentina'
    argentina_len = len(pais)
    print(pais, 'tiene', argentina_len, 'caracteres')

    # ¿Puedo acceder a cada uno de esos caracteres individualmente?
    # Claro que si!

    # Accedo al caracter inicial, el índice siempre empieza an cero [0]
    caracter_inicial = pais[0]
    print(caracter_inicial)

    # Accedo al caracter final, si la palabra tiene 9 letras,
    # el índice de la letra final será 8
    caracter_final = pais[8]
    caracter_final = pais[argentina_len-1]  # len=9, len-1 = 8 [MÉTODO CORRECTO]
    caracter_final = pais[-1]  # Índice negativo recorre la lista al reves [MÉTODO CORRECTO]
    print(caracter_final)

    # Puedo acceder a todos los caracteres individualmente
    print(pais[0], pais[1], pais[2],
          pais[3], pais[4]
          )

    # Puedo acceder a una serie de caracteres todos juntos
    # Se especifica el intervalo de índices con ':' --> inicial:final
    # El intervalo va desde le inicial inclusive hasta
    # el anterior al marcado como el final
    sub_text = pais[0:5]   # Obtendré los primeros 5 caracteres
    sub_text = pais[:5]    # Obtendré los primeros 5 caracteres [MÉTODO CORRECTO]
    print(sub_text)

    sub_text = pais[2:9]   # Obtendré desde el tercer caracter hasta el 8
    print(sub_text)

    # Obtendré desde el tercer caracter hasta el final
    sub_text = pais[2:argentina_len]
    # Obtendré desde el tercer caracter hasta el final
    sub_text = pais[2:len(pais)]
    # Obtendré desde el tercer caracter hasta el final [MÉTODO CORRECTO]
    sub_text = pais[2:]
    print(sub_text)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    numbers()
    strings()
    consola()
    operador_corchetes()
