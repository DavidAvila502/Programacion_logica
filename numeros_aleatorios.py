#Tarea 02
#Generar numeros aleatorios e indicar el mayor de ellos

import random #Importamos la libreria

#Generamos los 3 numero aleatorios

numero1 = random.randint(0,9)

numero2 = random.randint(0,9)

numero3 = random.randint(0,9)

#Usamos condicionales para saber cual fue el numero mayor de los 3



if(numero1 == numero2 and numero1 == numero3):
    print("Todos los numeros son iguales, no hay mayor...")


elif(numero1 > numero2):
    if(numero1 > numero3):
        print('El numero mayor es: %s'%(numero1))
    else:
        print('El numero mayor es: %s'%(numero3))

else:
    if(numero2 > numero3):
        print('El numero mayor es: %s'%(numero2))
    else:
        print('El numero mayor es: %s'%(numero3))

#Imprimimos los 3 numeros generados

print('Los 3 numeros fueron: %s,%s,%s'%(numero1,numero2,numero3))