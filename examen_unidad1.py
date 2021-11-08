import random

def comprobar(listanueva,numero,repetir):
    #print('la lista nueva es: %s'%(listanueva))
    signal = False
    contador = 0

    for j in range(0,20):
        if numero == listanueva[j]:
            contador=contador+1

    if contador == repetir:
        signal = True

    return signal

lista = []

for i in range(0,20):

    lista.append(random.randint(0,9))


print(lista)

numero = int(input('Ingresa el numero a buscar: '))
repetidas = int(input('Ingrese la cantidad de veces que crees que se repite el numero: '))

resultado = comprobar(lista,numero,repetidas)

print('El resultado es %s \nLa programacion utilizada en este examen fue Programacion estructurada'%(resultado))