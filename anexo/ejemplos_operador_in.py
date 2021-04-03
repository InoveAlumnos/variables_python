
# Tipos de variables [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplos del operador IN

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