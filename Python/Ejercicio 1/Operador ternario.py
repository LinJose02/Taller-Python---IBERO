""" Jose Rodriguez mayo 22, 2022.
    Actividad 6 - Creando algoritmos con tipos de datos, operadores y funciones.
    Ejercicio 1. Jugando con operadores.
    Punto 5. """

#Mensaje
print("Hola este algoritmo hara validaciones de sentencias a modo de test, dando a conocer si son verdaderas o falsas,\nintroduce solo numeros enteros y ten en cuenta mayúscula inicial y tilde")
#Preguntas tipo test
pregunta1 = str(input("¿Cual es la capital de Colombia? "))
pregunta2 = str(input("¿De que color es el cielo? "))
pregunta3 = int(input("¿Cuantas caras tiene un dado? "))
pregunta4 = int(input("Cuantos centímetros hay en un metro? "))
pregunta5 = str(input("¿Que símbolo identifica a todos los correos electónicos? "))
#Condición, si las preguntas son respondidas corecctamente
if (pregunta1 == 'Bogotá') and (pregunta2 == 'Azul') and (pregunta3 == 6) and (pregunta4 == 100) and ('@' in pregunta5):
    print ('Respondiste correctamente todas las preguntas')
else:
    print ('Desafortunadamente alguna de tus respuestas no fue correta, la respuestas son: Bogotá, Azul, 6, 100 y @')