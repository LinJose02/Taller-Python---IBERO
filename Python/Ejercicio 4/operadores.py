""" Jose Rodriguez mayo 26, 2022.
    Actividad 6 - Creando algoritmos con tipos de datos, operadores y funciones.
    Ejercicio 4. Jugando con operadores. """

print ('Hola este algoritmo te ayudara a realizar una operacion matematica entre numeros decimales, la cual puede ser (+,-,* o /)')
#asignacion de valores a variables
num1, num2 = input('Hola por favor ingresa dos numeros a operar separados por espacio y preferiblemete decimal; ejemplo (12.5 25.6) ').split()
num1, num2 = float(num1), float(num2)
#elecion de operador
operador = input('Ahora introduce el operador a usar, +,-,* o / ')
#condicionales para los operadores y posteriormente operacion a realizar con los números introducidos
if operador == '+':
    resultado = (num1) + (num2)
elif operador == '-':
    resultado = (num1) - (num2)
elif operador == '*':
    resultado = (num1) * (num2)
elif operador == '/':
    resultado = (num1) / (num2)


print(f'el resultado de la operacion entre {num1} y {num2} con operador {operador} da como resultado {resultado:,.2f}')
