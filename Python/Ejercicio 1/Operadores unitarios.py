""" Jose Rodriguez mayo 22, 2022.
    Actividad 6 - Creando algoritmos con tipos de datos, operadores y funciones.
    Ejercicio 1. Jugando con operadores.
    Punto 1. """

print("Hola, este algorimo recibira un valor incial, al cual se le sumara, restara, multiplicara y dividira los valores introducidos por el usuario. (todos los valores deben ser enteros")
#se pide un valor del cual se efectuaran las operaciones
valor_inicial = int(input('Introduce el valor incial ')) #Se recibe el valor al que se efectuaran las sumas y restas
#se piden un valores y se procesara en cada una de las operaciones para luego mostrar el valor final
valor1 = int(input('Introduce el valor a sumar ')) #suma de un valor introducido por el ususario dos veces
valor_inicial = valor_inicial + valor1
print(valor_inicial)

valor2 = int(input('Introduce el valor a restar ')) #resta un valor introducido por el usuario dos veces
valor_inicial = valor_inicial - valor2
print(valor_inicial)

valor3 = int(input('Introduce el valor a multiplicar ')) #multiplica de un valor introducido por el ususario dos veces
valor_inicial = valor_inicial * valor3
print(valor_inicial)

valor4 = int(input('Introduce el valor a dividir ')) #divide de un valor introducido por el ususario dos veces
valor_inicial = valor_inicial / valor4


print(f'el valor final es de {int(valor_inicial)}') #resultado