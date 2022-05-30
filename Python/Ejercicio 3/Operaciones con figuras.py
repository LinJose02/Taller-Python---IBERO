""" Jose Rodriguez mayo 26, 2022.
    Actividad 6 - Creando algoritmos con tipos de datos, operadores y funciones.
    Ejercicio 3. Jugando con operadores. """

print ('Hola, este algoritmo te ayudara a obtener el area de una de tres figuras geometricas, las cuales son circulo, triangulo y cuadrado')
#elecion de tipo de figura
seleccion = int(input('Por favor seleciona una figura: (1) triángulo, (2) para cuadrado y (3) para circulo '))
#validacion del valor introducido
if (seleccion >= 1) and (seleccion <= 3):
    #validacion del tipo de medida y elecion del tipo de medida
    tipo_medida = int(input('Por favor indica si la medida es en metros o centimetros: (1) para metros y (2) para centimentros '))
    if (tipo_medida >= 1) and (tipo_medida <=2):
        if tipo_medida == 1:
            tipo = 'm^2'
        if tipo_medida == 2:
            tipo = 'cm^2'
        #condicionales para los valores introducidos y operaciones con los datos requeridos segun la elecion
        if (seleccion == 1):
                print (f'Tu selecion es {seleccion} vamos a obtener el area del triángulo segun la formula (base * altura) / 2.')
                base = float(input(('Para hallar el area de un triángulo es necesario conocer la base y su altura, por favor digita la medida de la base ')))
                altura = float(input('Ahora digita la medida de la altura '))
                area = (base * altura) / 2
                print (f'El area del triangulo es {area:,} {tipo}')
        elif seleccion == 2:
                print (f'Tu selecion es {seleccion} vamos a obtener el area del cuadrado segun la formula (lado * lado).')
                lado = float(input(('Para hallar el area de un cuadrado es necesario conocer la medida de uno de los lados, por favor digita la medida de uno de los lados ')))
                area = lado*lado 
                print (f'El area del cuadrado es {area:,} {tipo}')
        elif seleccion == 3:
                print (f'Tu selecion es {seleccion} vamos a obtener el area del circulo segun la formula (radio^2) * PI(3.1416).')
                radio = float(input(('Para hallar el area de un circulo es necesario conocer el radio de la circunferencia, por favor digita la medida del radio ')))
                area = (radio**2) * 3.1416
                print (f'El area del circulo es {area:,} {tipo}')

    else:
        print('Entrada erronea, intenta nuevamente con 1 o 2')

    
else:
    print ('Tu seleccion es invalida, por favor intenta nuevamente, con 1, 2 o 3. Sigue las instrucciones.')