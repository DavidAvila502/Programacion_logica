#Programa 03
#Programa que determine si una palabra es un palindromo

#Metodo para eliminar los acentos
def eliminar_tildes(cadena):

    cadena_nueva = cadena
    cadena_nueva = cadena_nueva.replace('á','a')
    cadena_nueva = cadena_nueva.replace('é','e')
    cadena_nueva = cadena_nueva.replace('í','i')
    cadena_nueva = cadena_nueva.replace('ó','o')
    cadena_nueva = cadena_nueva.replace('ú','u')

    return cadena_nueva
    
    #Metodo para eliminar signos de puntuacion
def eliminar_signos_puntuacion(cadena):
    palabra = cadena
    palabra = palabra.lower()#Volvemos minuscula la palabra

    palabra = palabra.replace(" ","")#Eliminamos los espacios de la palabra 

    palabra = palabra.replace(",","")#Eliminamos comas 

    palabra = palabra.replace(".","")#Eliminamos puntos 

    return palabra

palabra =input("Ingrese una palabra: ")#Pedimos la palabra al usuario

palabra = eliminar_tildes(palabra)#Eliminamos los acentos

palabra = eliminar_signos_puntuacion(palabra)#Elimina los signos de puntuacion

palabra_invertida = palabra[::-1]#Creamos palabra invertida

#Comparamos si ambas palabras son iguales 
if(palabra == palabra_invertida):
    print('Es un palindromo') #Caso verdadero es palindromo

else:
    print('No es un palindromo')#Caso contrario no es palindromo

