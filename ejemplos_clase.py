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

    # Esta forma NO la utilizaremos, ya que la clase que viene veremos una forma
    # más simple de poder armar un mensaje con formato
    print('El resultado de restar %d y %d es %d' % (numero_1, numero_2, resta))

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

    # Dada una serie de direcciones, queremos saber si son provincias Argentinas
    direccion_1 = 'Mendoza, Argentina'
    direccion_2 = 'Córdoba, Argentina'
    direccion_3 = 'La Paz, Bolivia'

    # Ensayemos algunos casos de ejemplo con la primera direccion
    es_direccion_argentina = 'Argentina' in direccion_1
    # es_direccion_argentina es un resultado tipo Bool (True,False)
    print(direccion_1, 'es una dirección Argentina?', es_direccion_argentina)

    # Ensayemos con la dirección 2, pero ahora utilizando puras variables
    pais_objetivo = 'Argentina'
    es_direccion_argentina = pais_objetivo in direccion_2
    print(direccion_2, 'es una dirección Argentina?', es_direccion_argentina)

    # ¿Qué pasa si realizo la operación al reves?
    es_direccion_argentina = direccion_2 in pais_objetivo
    # Está claro que el orden de los factores importa:
    print(direccion_2, 'es una dirección Argentina?', es_direccion_argentina)

    # Ya se imaginarán el resultado con la dirección 3
    es_direccion_argentina = pais_objetivo in direccion_3
    print(direccion_3, 'es una dirección Argentina?', es_direccion_argentina)

    # Una cadena de texto (string) está compuesta de Nº caracteres
    # ¿Cuántos caracteres tiene el Argentina?
    argentina_len = len(pais_objetivo)
    print(pais_objetivo, 'tiene', argentina_len, 'caracteres')

    # ¿Puedo acceder a cada uno de esos caracteres individualmente?
    # Claro que si!

    # Accedo al caracter inicial, el índice siempre empieza an cero [0]
    caracter_inicial = pais_objetivo[0]
    print(caracter_inicial)

    # Accedo al caracter final, si la palabra tiene 9 letras,
    # el índice de la letra final será 8
    caracter_final = pais_objetivo[8]
    caracter_final = pais_objetivo[argentina_len-1]  # len=9, len-1 = 8 [MÉTODO CORRECTO]
    caracter_final = pais_objetivo[-1]  # Índice negativo recorre la lista al reves [MÉTODO CORRECTO]
    print(caracter_final)

    # Puedo acceder a todos los caracteres individualmente
    print(pais_objetivo[0], pais_objetivo[1], pais_objetivo[2],
          pais_objetivo[3], pais_objetivo[4]
          )

    # Puedo acceder a una serie de caracteres todos juntos
    # Se especifica el intervalo de índices con ':' --> inicial:final
    # El intervalo va desde le inicial inclusive hasta
    # el anterior al marcado como el final
    sub_text = pais_objetivo[0:5]   # Obtendré los primeros 4 caracteres
    sub_text = pais_objetivo[:5]    # Obtendré los primeros 4 caracteres [MÉTODO CORRECTO]
    print(sub_text)

    sub_text = pais_objetivo[2:9]   # Obtendré desde el tercer caracter hasta el 8
    print(sub_text)

    # Obtendré desde el tercer caracter hasta el final
    sub_text = pais_objetivo[2:argentina_len]
    # Obtendré desde el tercer caracter hasta el final
    sub_text = pais_objetivo[2:len(pais_objetivo)]
    # Obtendré desde el tercer caracter hasta el final [MÉTODO CORRECTO]
    sub_text = pais_objetivo[2:]
    print(sub_text)

    # ¿Cómo puedo obtener un intervalo pero de a pasos de a 2 letras?
    # Esto puede resultar muy confuso,
    # recién le sacaremos provecho en cursos avanzados
    sub_text = pais_objetivo[0:argentina_len:2]
    print(sub_text)


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


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    numbers()
    strings()
    consola()
