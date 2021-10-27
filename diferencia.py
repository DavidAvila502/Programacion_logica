#Pre examen
# Generar una lista dinamica de 10 elementos aleatorios y recorrer el arreglo,
# verificando la diferencia entre la posicion actual y el siguiente, la mayor diferencia
# es el numero que debe ser impreso

import random

lista=[]

for k in range(0,10):
    lista.append(random.randint(0,100))

print(lista)

diferencia_anterior=0
diferencia_1 =0
diferencia_2=0
final=''

for j in range(0,8):

    #Sacamos primera diferencia
    diferencia_1 = lista[j] -lista[j+1]
    #sacamos segunda diferencia
    diferencia_2 = lista[j+1] - lista[j+2]

    
    if diferencia_1 > diferencia_anterior:
        if diferencia_1 > diferencia_2:
            diferencia_anterior= diferencia_1
            final ='los numeros son: %s,%s y la mayor diferencia es de: %s'%(lista[j],lista[j+1],diferencia_anterior)
        else:
             diferencia_anterior = diferencia_2
             final ='los numeros son: %s,%s y la mayor diferencia es de: %s'%(lista[j+1],lista[j+2],diferencia_anterior) 

    else:
       if diferencia_2 > diferencia_anterior:
           diferencia_anterior = diferencia_2
           final ='los numeros son: %s,%s y la mayor diferencia es de: %s'%(lista[j+1],lista[j+2],diferencia_anterior) 
  
print(final)



