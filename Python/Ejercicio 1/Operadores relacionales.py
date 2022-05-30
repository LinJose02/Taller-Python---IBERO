""" Jose Rodriguez mayo 22, 2022.
    Actividad 6 - Creando algoritmos con tipos de datos, operadores y funciones.
    Ejercicio 1. Jugando con operadores.
    Punto 3. """

print("Hola, este algoritmo validara si 5 numeros enteros son iguales, diferentes, menor, menor o igual y mayor o igual.\n(solo se mostraran las condiciones que se cumplan)")
#ingreso de datos
num1 = int(input("introduce el primer número "))
num2 = int(input("introdce el segundo numero "))
#condiciones que evaluaran los dos numeros y mostraran el resultado de esa evaluacion
if num1 == num2:
    print(f'{num1} y {num2} son iguales')
if num1 != num2:
    print (f'{num1} y {num2} son diferentes')
if num1 < num2:
    print(f'{num1} es menor que {num2}')
if num1 <= num2:
    print (f'{num1} es menor o igual a {num2}')
if num1 >= num2:
    print(f'{num1} es mayor o igual a {num2}')