""" Jose Rodriguez mayo 26, 2022.
    Actividad 6 - Creando algoritmos con tipos de datos, operadores y funciones.
    Ejercicio 4. Jugando con operadores. """

#from math import factorial


print('Hola, este algoritmo esta diseñado para mostrar un valor factorial de un valor introducido')
valor = int(input('Por favor ingresa el valor del cual deseas conocer su factorial '))
#condiciones en caso de que los valores sean 0 o menor que 0
if valor <0:
    print(f'El valor no se puede encontrar al ser {valor} negativo')
elif valor == 0:
    print (' el valor factorial de (0) es 1')


else:
    fact = 1
    for y in range (1, valor + 1):#ciclo for donde se fijan los parametros y se efectua la operacion con cada valor de la iteracion (y) y la variable fact
        fact *= y
print (f'el factorial del numero {valor} es {fact}')
   