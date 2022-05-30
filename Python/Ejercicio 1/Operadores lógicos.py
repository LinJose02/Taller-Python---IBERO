""" Jose Rodriguez mayo 22, 2022.
    Actividad 6 - Creando algoritmos con tipos de datos, operadores y funciones.
    Ejercicio 1. Jugando con operadores.
    Punto 4. """


print("Hola, este algoritmo validara si tienes la edad suficiente para crear una cuenta de red social")
#ingreso de datos
edad = int(input('Por favor ingresa tu edad '))
nacion = int(input("indica si eres colombiano o no, por favor indroduce el número (1) si eres de colombia o el número (2) si eres ectranjer@ "))
#condicional de si es o no mayor de edad
if (edad >= 18) and (nacion == 1):
    print ("Puedes abrir tu cuenta")
if (edad < 18) or (nacion == 2):
    print("Es probable que no sea mayor de edad o que no seas colombiano, intenta nuevamente")
