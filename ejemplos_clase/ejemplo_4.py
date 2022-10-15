# Tipos de variables [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 3.0

# Ejemplos con el operador corchetes

# Una cadena de texto (string) está compuesta de Nº caracteres
# ¿Cuántos caracteres tiene la palabra Argentina?
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