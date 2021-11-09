#Calculadora en programacion logica

#Funciones de operaciones basicas
def suma(numero1,numero2):
    return numero1 + numero2

def resta(numero1,numero2):
    return numero1 - numero2

def multiplicar(numero1,numero2):
    return numero1 * numero2

def dividir(numero1,numero2):
    return numero1 / numero2

#funcion secundaria
def operar(funcion,numero1,numero2):
    
    resultado = funcion(numero1,numero2)

    return resultado




#Funcion principal
def run():

    numero1 = int(input('Ingrese un numero: '))
    numero2 = int(input('Ingrese un numero: '))

    resultado = operar(suma,numero1,numero2)

    print('La suma fue: %s'%(resultado))
    
    
    resultado = operar(resta,numero1,numero2)

    print('El La resta fue: %s'%(resultado))

    
    resultado = operar(multiplicar,numero1,numero2)

    print('La multiplicaicon fue: %s'%(resultado))
   
    resultado = operar(dividir,numero1,numero2)

    print('la division fue: %s'%(resultado))



if __name__ == '__main__':
    run()
