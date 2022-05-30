""" Jose Rodriguez mayo 24, 2022.
    Actividad 6 - Creando algoritmos con tipos de datos, operadores y funciones.
    Ejercicio 2. Jugando con operadores. """

#desde: https://www.nivea.es/consejos/estilo-de-vida/como-calcular-indice-de-masa-corporal-imc-0NRP0

'''El Índice de Masa Corporal (IMC) es el resultado de dividir tu peso entre tu estatura al cuadrado, es decir que el cálculo sería IMC = KG/M2'''

'''La obesidad se subdivide en tres niveles: obesidad grado 1 de bajo riesgo (la puntuación del IMC oscila entre 24 y 30 en mujeres; entre 25 y 30 en hombres), obesidad grado 2 de riesgo moderado (IMC en hombres y mujeres entre 30 y 40) y obesidad grado 3 severa (IMC en mujeres y hombres superior a 40).'''

#desde: https://www.cdc.gov/healthyweight/spanish/assessing/index.html#:~:text=Si%20su%20IMC%20es%20menos,dentro%20del%20rango%20de%20obesidad.

'''Si su IMC es menos de 18.5, se encuentra dentro del rango de peso insuficiente.
Si su IMC es entre 18.5 y 24.9, se encuentra dentro del rango de peso normal o saludable.
Si su IMC es entre 25.0 y 29.9, se encuentra dentro del rango de sobrepeso.
Si su IMC es 30.0 o superior, se encuentra dentro del rango de obesidad.'''

IMC_list = ['Su IMC es menos de 18.5, se encuentra dentro del rango de peso insuficiente.', 'su IMC es entre 18.5 y 24.9, se encuentra dentro del rango de peso normal o saludable.', 'su IMC es entre 25.0 y 29.9, se encuentra dentro del rango de sobrepeso.', 'su IMC es 30.0 o superior, se encuentra dentro del rango de obesidad.']

#funcion peso que tomara dos valores, los dividira y elevara a 2 devolvera ese valor 

def peso_adecuado (peso_kg, alt_selecionada):
    IMC = int(peso_kg)/float(alt_selecionada)**2
    return IMC