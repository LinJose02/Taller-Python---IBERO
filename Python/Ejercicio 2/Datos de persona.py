""" Jose Rodriguez mayo 22, 2022.
    Actividad 6 - Creando algoritmos con tipos de datos, operadores y funciones.
    Ejercicio 2. Jugando con operadores. """
#llamado de funciones
import funcion_edad
import funcion_peso


# Mensaje
print("Hola, este algoritmo almacenara tu informacion a modo de base de datos, para luego presentarla por pantalla al final")

# Captura de tipo de documento int
documentos = ['(CC) Cédula de ciudadania', '(TI) tarjeta de identidad',
                '(PA) Pasaporte', '(RC) Registro civil']#lista a mostrar 
print("Selecciona tu tipo de documento de identidad", documentos)
tipo_de_documento = int(
    input("(0) si es CC (1) si es TI (2) si es PA (3) si es RC \n"))
doc_selecionado = (documentos[tipo_de_documento])

# captura de datos tipo str, int y float
numero_de_documento = int(input("Digita tu número de documento "))

nombre = str(input("Ingresa tu nombre y apellido "))

# funcion edad
edad = int(input("Ingresa tu edad "))
if funcion_edad.edad_adecuada(edad):# la funcion edad evalua si es no mayor de edad y guarda la respuesta para luego ser mostrada
    edad_evaluada = "Mayor de edad ", edad
else:
    edad_evaluada = "Menor de edad ", edad

sexo = str(input("Escribe tu género "))

peso_kg = float(input("Dita tu peso en kg "))

#listas a mostrar segun la edad que se introduzca, de ese valor escogido se3 efectuara la operacion del peso ideal
edad_1 = [0.68, 0.69, 0.70, 0.71, 0.72, 0.73,0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.80, 0.81]
edad_2 = [0.80, 0.81, 0.82, 0.83, 0.84, 0.85,0.86, 0.87, 0.88, 0.89, 0.90, 0.91, 0.92, 0.93]
edad_3 = [0.87, 0.88, 0.89, 0.90, 0.91, 0.92, 0.93,0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.00, 1.01, 1.02]
edad_4 = [0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.00,1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09]
edad_6 = [1.06, 1.07, 1.08, 1.09, 1.10, 1.11, 1.12, 1.13, 1.14,1.15, 1.16, 1.17, 1.18, 1.19, 1.20, 1.21, 1.22, 1.23, 1.24]
edad_8 = [1.19, 1.20, 1.21, 1.22, 1.23, 1.24, 1.25, 1.26, 1.27,1.28, 1.29, 1.30, 1.31, 1.32, 1.33, 1.34, 1.35, 1.36, 1.37]
edad_10 = [1.27, 1.28, 1.29, 1.30, 1.31, 1.32, 1.33, 1.34, 1.35, 1.36, 1.37,1.38, 1.39, 1.40, 1.41, 1.42, 1.43, 1.44, 1.45, 1.46, 1.47, 1.48, 1.49]
edad_12 = [1.39, 1.40, 1.41, 1.42, 1.43, 1.44, 1.45, 1.46, 1.47, 1.48, 1.49,1.50, 1.51, 1.52, 1.53, 1.54, 1.55, 1.56, 1.57, 1.58, 1.59, 1.60, 1.61]
edad_14 = [1.49, 1.50, 1.51, 1.52, 1.53, 1.54, 1.55, 1.56, 1.57, 1.58, 1.59, 1.60, 1.61, 1.62, 1.63, 1.64, 1.65, 1.66, 1.67, 1.68, 1.69, 1.70, 1.71, 1.72, 1.73, 1.74, 1.75, 1.76]
edad_16 = [1.52, 1.53, 1.54, 1.55, 1.56, 1.57, 1.58, 1.59, 1.60, 1.61, 1.62, 1.63, 1.64, 1.65, 1.66, 1.67,1.68, 1.69, 1.70, 1.71, 1.72, 1.73, 1.74, 1.75, 1.76, 1.77, 1.78, 1.79, 1.80, 1.81, 1.82, 1.83, 1.84, 1.85]
edad_18 = [1.52, 1.53, 1.54, 1.55, 1.56, 1.57, 1.58, 1.59, 1.60, 1.61, 1.62, 1.63, 1.64, 1.65, 1.66, 1.67, 1.68, 1.69, 1.70, 1.71, 1.72, 1.73, 1.74, 1.75,1.76, 1.77, 1.78, 1.79, 1.80, 1.81, 1.82, 1.83, 1.84, 1.85, 1.86, 1.87, 1.88, 1.89, 1.90, 1.91, 1.92, 1.93, 1.94, 1.95, 1.96, 1.97, 1.98, 1.99, 2.00]

#condicionales para el valor introducido en edad y asigna la lista que corresponde a una variable general que se mostrara
if edad == 1:
    lista_medidas = edad_1
elif edad == 2:
    lista_medidas = edad_2
elif edad == 3:
    lista_medidas = edad_3
elif edad == 4:
    lista_medidas = edad_4
elif edad == 5:
    lista_medidas = edad_6
elif edad == 6:
    lista_medidas = edad_6
elif edad == 7:
    lista_medidas = edad_8
elif edad == 8:
    lista_medidas = edad_8
elif edad == 9:
    lista_medidas = edad_10
elif edad == 10:
    lista_medidas = edad_10
elif edad == 11:
    lista_medidas = edad_12
elif edad == 12:
    lista_medidas = edad_12
elif edad == 13:
    lista_medidas = edad_14
elif edad == 14:
    lista_medidas = edad_14
elif edad == 15:
    lista_medidas = edad_16
elif edad == 16:
    lista_medidas = edad_16
elif edad == 17:
    lista_medidas = edad_18
elif edad >= 18:
    lista_medidas = edad_18

print('Lista de medidas en metros para ', edad, ' años ', lista_medidas)
print(len(lista_medidas))
altura = int(input("Segun la lista medidas digite su altura eligiendo desde el (0) al ultimo dato, siendo (0) el primer elemento \n")) #elecion de altura

alt_selecionada = (lista_medidas [altura])

#Funcion peso
IMC_list = ['Su IMC es menos de 18.5, se encuentra dentro del rango de peso insuficiente.', 'su IMC es entre 18.5 y 24.9, se encuentra dentro del rango de peso normal o saludable.', 'su IMC es entre 25.0 y 29.9, se encuentra dentro del rango de sobrepeso.', 'su IMC es 30.0 o superior, se encuentra dentro del rango de obesidad.']#lista a mostrar
#condional sobre el peso una vez realizada la operacion entra altura y el peso introducido, segun ese valor se mostrara la valoracion de ese resultadod
if funcion_peso.peso_adecuado(peso_kg, alt_selecionada) <= 18:
    peso_imc = (peso_kg),(IMC_list [0])
elif funcion_peso.peso_adecuado(peso_kg, alt_selecionada) >= 18.5 <=24.9:
    peso_imc = (peso_kg),(IMC_list [1])
elif funcion_peso.peso_adecuado(peso_kg, alt_selecionada) >= 25.0 <=29.9:
    peso_imc = (peso_kg),(IMC_list [2])
elif funcion_peso.peso_adecuado(peso_kg, alt_selecionada) >= 30.0:
    peso_imc = (peso_kg),(IMC_list [3])
    

# Se muestra informacion registrada por medio de una tabla
usuario = [[],[],[],[],[],[],[]]#define la cantidad de datos a almacenar
tamaño = 1# define la cantidad de usuarios, en este caso 1

for i in range(tamaño): #ciclo for para guardar la informacion en una tabla

    usuario [0].append(doc_selecionado)# asignacion de informacion a lista
    usuario [1].append(numero_de_documento)
    usuario [2].append(nombre)
    usuario [3].append(edad_evaluada)
    usuario [4].append(sexo)
    usuario [5].append(peso_imc)
    usuario [6].append(alt_selecionada)

for i in range( tamaño):#muestra informacion de la tabla
    print("Tipo de documento:   ", usuario[0])
    print("Número de documento: ", usuario[1])
    print("Nombre:              ", usuario[2])
    print("Edad:                ", usuario[3], 'años')
    print("Sexo:                ", usuario[4])
    print("Peso:                ", usuario[5], ' Kg')
    print("Altura:              ", usuario[6], ' m')







