""" Jose Rodriguez mayo 22, 2022.
    Actividad 6 - Creando algoritmos con tipos de datos, operadores y funciones.
    Ejercicio 1. Jugando con operadores.
    Punto 2. """

print("Hola, este algoritmo validara si dos números son iguales o no. En caso de NO serlo se sumaran entre si, a la suma se le \nrestara el segundo dato y su resultado se dividira en 2, arojando el producto y el residuo")

dato1 = int(input("por favor ingrese el primer número "))#ingreso de datos
dato2 = int(input("por favor ingrese el segundo número "))
sum = 0
if dato1 != dato2:#funcion si, si los datos son diferentes se realizaran las operaciones
    print(f'los datos introducidos {dato1} y {dato2} no son iguales')
    sum += dato1 + dato2 #suma
    print("suma ",sum)
    sum -= dato2 #resta
    print("resta ",sum) 
    sum /= 2 #division
    print("division ",sum)
    sum %= 2 #residuo o modulo
    print("producto ",sum)
else:
    print("los datos introducidos no son diferentes, fin del algoritmo.\nSugiero introducir dos números diferentes para aprovechar el potencial del algoritmo")