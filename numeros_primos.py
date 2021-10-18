#Programa 05
#Ingresar un numero y determinar  si es primo o no

def evaluar_numero(entero):#funcion que divide el numero con sus antecesores y retorna valor booleano
    primo = True

    for k in range(entero-1,1,-1):
        
        if entero % k ==0:
            primo = False
            break

    return primo

#Intentamos ejecutar el siguiente codigo
try:

    numero = int(input('Ingresa un numero entero: '))

    #numero ingresado debe ser mayor que 1
    if numero >1:
        resultado = evaluar_numero(numero)#Usamos nuestra funcion evaluar_numero
        #Comparamos resultado de nuestra funcion
        if resultado == True:
            print('El numero es primo')
        else:
            print('El numero no es primo')

    #Si no es mayor a 1 lanzar mensaje
    else:
       print('El numero debe ser mayor a 1')

    
#En caso de que haya un error en el codigo lanzar el mensaje
except:
    print('El numero ingresado es invalido')



